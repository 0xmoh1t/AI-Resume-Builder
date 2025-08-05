from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os, uuid, mimetypes, subprocess
import google.generativeai as genai
import docx2txt
import fitz  # PyMuPDF

app = Flask(__name__)
CORS(app)
load_dotenv()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

def extract_text_from_resume(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        text = ""
        doc = fitz.open(filepath)
        for page in doc:
            text += page.get_text()
        return text
    elif ext == ".docx":
        return docx2txt.process(filepath)
    else:
        return "Unsupported format"

def call_gemini_for_latex(resume_text, job_description):
    try:
        with open("template.tex", "r") as f:
            latex_template = f.read()
    except FileNotFoundError:
        return "LaTeX template file (template.tex) not found."

    prompt = f"""
You are a LaTeX resume expert.

Your job is to:
- Read the LaTeX template provided below.
- ONLY modify the content **inside** the following two comment markers:
    % --- Content will be generated here by the model ---
    % --- End of generated content ---
- Do NOT modify or regenerate any other part of the LaTeX file.
- Do NOT include any LaTeX preamble like \\documentclass, \\begin{{document}}, \\usepackage, etc.
- Do NOT repeat the entire LaTeX template. Just generate the content that belongs between the two comment markers.
- Keep the formatting consistent with the LaTeX template.
- Use and improve content from the resume below.
- Optimize it to align with the job description provided (aim for ≥80% relevance).

========
TEMPLATE: 
{latex_template}

========
JOB DESCRIPTION:
{job_description}

========
RESUME:
{resume_text}

Now, return ONLY the content that should go between:
    % --- Content will be generated here by the model ---
    and
    % --- End of generated content ---

Do NOT include any other text or explanations. Only return valid LaTeX content.
"""

    response = model.generate_content(prompt)
    generated_content = response.text.strip()

    # Replace content inside the LaTeX template between placeholders
    start_marker = "% --- Content will be generated here by the model ---"
    end_marker = "% --- End of generated content ---"
    if start_marker in latex_template and end_marker in latex_template:
        before = latex_template.split(start_marker)[0] + start_marker + "\n"
        after = "\n" + end_marker + latex_template.split(end_marker)[1]
        final_latex_code = before + generated_content + after
    else:
        return "LaTeX template is missing the required placeholder comments."

    return final_latex_code


def latex_to_pdf(latex_code, output_filename="resume"):
    tex_file = f"{output_filename}.tex"
    pdf_file = f"{output_filename}.pdf"

    # Write the LaTeX code to file
    with open(tex_file, "w") as f:
        f.write(latex_code)

    # Compile using pdflatex (ensure it's installed and in PATH)
    subprocess.run(["pdflatex", tex_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return pdf_file if subprocess.run(["pdflatex", tex_file]).returncode == 0 else "PDF generation failed"

@app.route("/", methods=["GET"])
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html><body>
    <h2>AI Resume Builder</h2>
    <form method="POST" action="/process" enctype="multipart/form-data">
        <p><b>Upload your Resume (PDF or DOCX):</b><br><input type="file" name="resume" required></p>
        <p><b>Paste Job Description:</b><br><textarea name="job_description" rows="8" cols="80" required></textarea></p>
        <button type="submit">Submit</button>
    </form>
    </body></html>
    ''')

@app.route("/process", methods=["POST"])
def process_resume():
    file = request.files['resume']
    job_desc = request.form['job_description']

    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    resume_text = extract_text_from_resume(path)
    if resume_text == "Unsupported format":
        return "Only PDF or DOCX allowed", 400

    latex_code = call_gemini_for_latex(resume_text, job_desc)
    if "LaTeX template file (template.tex) not found." in latex_code:
        return latex_code, 500 # Return an error if the template file is not found

    output_pdf = latex_to_pdf(latex_code)

    return send_file(output_pdf, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

    #hello-world