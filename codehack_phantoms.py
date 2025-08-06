from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os, uuid, mimetypes, subprocess
import google.generativeai as genai
import docx2txt
import fitz  # PyMuPDF
import shutil

app = Flask(__name__)
CORS(app)
load_dotenv()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def extract_text_from_resume(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        text = ""
        doc = fitz.open(filepath)
        all_links = []
        for page in doc:
            text += page.get_text()
            # Find all hyperlink objects on the page
            page_links = page.get_links()
            for link in page_links:
                # Add the URL to our list if it exists
                if 'uri' in link:
                    all_links.append(link['uri'])

        # Append the found links to the end of the extracted text
        # This makes the links available to the Gemini model
        if all_links:
            text += "\n\n--- DETECTED HYPERLINKS ---\n"
            text += "The following hyperlinks were found in the document. Please associate them with the correct projects or sections.\n"
            # Use a set to avoid duplicate links
            for link_url in sorted(list(set(all_links))):
                text += f"- {link_url}\n"
        return text
    elif ext == ".docx":
        # Note: python-docx has limited support for extracting hyperlinks.
        # This part of the function remains unchanged.
        return docx2txt.process(filepath)
    else:
        return "Unsupported format"

def call_gemini_for_latex(resume_text, job_description):
    try:
        with open("template.tex", "r") as f:
            latex_template = f.read()
    except FileNotFoundError:
        return "LaTeX template file (template.tex) not found."

    prompt = fr"""
You are a LaTeX resume expert.

Your job is to:
- Read the provided LaTeX template and ONLY fill in the content. Do not alter the template's structure, packages, or existing commands.
- Use the content from the provided RESUME and optimize it to align with the job description. The goal is to make the resume highly relevant to the job description.
- **VERY IMPORTANT: The RESUME text below may contain a special section at the end, starting with `--- DETECTED HYPERLINKS ---`. This section contains a list of all URLs extracted from the original resume file.**
- **You MUST intelligently associate these URLs with the corresponding projects, certifications, or other items mentioned in the main body of the resume.** For example, if you see a project named "Portfolio Website" and a URL like "https://khushal.dev", you should link them.
- For projects and certifications, create a LaTeX `\href` command. The display text should be "Link". For example: `\begin{{twocolentry}}{{\href{{https://example.com/project-link}}{{Link}}}}`
- For the header section (email, phone), use the `\hrefWithoutArrow` command as shown in the template.
- If a section from the template is not relevant or if the required information is not available in the resume, you must omit the entire section and its corresponding title (`\section{{...}}`). **Do not include any N/A placeholders.**
- Ensure the generated content fits seamlessly into the template and always returns a complete, valid LaTeX document that compiles without errors.
- **Your output MUST be pure LaTeX code.** Do NOT wrap the code in markdown (e.g., ```latex) or include any extra text or explanations.
- **Handle special characters properly.** Escape `&`, `%`, `$`, `#`, `_`, '{{', '}}', `~` with a backslash. Use `\&` for a literal ampersand.
- Use a double hyphen (`--`) for date ranges.


========
TEMPLATE:
{latex_template}

========
JOB DESCRIPTION:
{job_description}

========
RESUME:
{resume_text}

Now, return the complete, valid, and compilable LaTeX code based on the TEMPLATE, filled with content from the RESUME, and optimized for the JOB DESCRIPTION.
"""

    response = model.generate_content(prompt)
    generated_latex_code = response.text.strip()

    # The model is instructed to return the full LaTeX code based on the template
    # No additional insertion logic is needed here if the model follows instructions.
    # We can add a basic check to ensure the response looks like LaTeX
    if not generated_latex_code.startswith('\\documentclass') and not '\\begin{document}' in generated_latex_code:
         print("Warning: Gemini did not return a full LaTeX document. Attempting to use original template with generated content.")
         # Fallback to original insertion logic if the model doesn't return the full template
         start_marker = "% --- Content will be generated here by the model ---"
         end_marker = "% --- End of generated content ---"
         if start_marker in latex_template and end_marker in latex_template:
             before = latex_template.split(start_marker)[0] + start_marker + "\n"
             after = "\n" + end_marker + latex_template.split(end_marker)[1]
             # Assuming the model still generated only the content part in this case
             content_part = response.text.strip() # Use original response text
             generated_latex_code = before + content_part + after
         else:
             return "LaTeX template is missing the required placeholder comments for fallback.", 500

    if "begin{document}" in generated_latex_code and "\\begin{document}" not in generated_latex_code:
        generated_latex_code = generated_latex_code.replace("begin{document}", "\\begin{document}")
    if "end{document}" in generated_latex_code and "\\end{document}" not in generated_latex_code:
        generated_latex_code = generated_latex_code.replace("end{document}", "\\end{document}")

    return generated_latex_code

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

    return send_file(output_pdf, as_attachment=True, download_name="Updated_Resume.pdf")

if __name__ == "__main__":
    app.run(debug=True)

