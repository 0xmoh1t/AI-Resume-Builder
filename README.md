# 🧐 AI Resume Builder

AI Resume Builder is an open-source project that uses **AI + LaTeX** to transform your existing resume into a clean, job-optimized, ATS-friendly PDF using a customizable LaTeX template.

This was developed as part of the **IBM SkillsBuild AI Agentic Internship**, with a focus on intelligent automation, AI integration, and professional document enhancement using LaTeX and Gemini.

---

## 🚀 Features

- 📄 Upload your resume (PDF or DOCX)
- 🧠 Uses Google Gemini API to enhance your resume based on job description
- 📘 Custom LaTeX template with structured formatting
- 📄 Automatically compiles to PDF using `pdflatex`
- 🌐 Simple Flask-based web interface
- 💡 AI-powered rewriting, ATS optimization, hyperlink handling, and section prioritization

---

## 🏧 Project Structure

```
AI-Resume-Builder/
├── static/               # Static files like CSS
├── templates/            # HTML templates (Flask frontend)
├── uploads/              # Uploaded resumes & generated PDFs
├── template.tex          # LaTeX resume template
├── codehack_phantoms.py  # Flask backend server
├── setup.py              # All-in-one setup script (venv + dependencies)
└── .env                  # Gemini API key configuration
```

---

## 📆 Requirements

- Python 3.8+
- LaTeX (with required packages like `titlesec`, `xcolor`, etc.)
- Google Gemini API Key
- `pdflatex` installed on system (via TeX Live)

---

## ⚙️ Installation Guide

### 🐍 Step 1: Clone and Set Up Python + System Environment

```bash
git clone https://github.com/0xmoh1t/AI-Resume-Builder.git
cd AI-Resume-Builder

# Automatically creates virtualenv and installs all Python + LaTeX dependencies
python3 setup.py
```

This will:
- Create a Python virtual environment
- Install all required Python libraries
- Install required LaTeX system packages (on Linux)

---

### 🔐 Step 2: Configure Gemini API Key

Create a `.env` file in the root directory with the following content:

```
GEMINI_API_KEY=your_google_api_key_here
```

---

## 🧲 Run the App

```bash
source venv/bin/activate  # Or venv\Scripts\activate on Windows
python codehack_phantoms.py
```

Now open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🧠 How It Works

1. Upload your resume (PDF or DOCX)
2. Paste your target job description
3. Gemini rewrites and adapts your resume using LaTeX
4. PDF gets compiled automatically with `pdflatex`
5. Download your enhanced, job-ready resume!

---

## 🧰 Tech Stack

| Component      | Technology                     |
|----------------|---------------------------------|
| **Backend**    | Python, Flask                   |
| **Frontend**   | HTML, CSS (Flask templates)     |
| **AI**         | Google Gemini API               |
| **PDF Output** | LaTeX + pdfTeX (pdflatex)       |

---

## 👨‍💼 Contributors

| Name    | GitHub Handle |
|---------|----------------|
| Mohit   | [@0xmoh1t](https://github.com/0xmoh1t) |
| Hardik  | [@HardikIsACoder](https://github.com/HardikIsACoder) |
| Moulik  | [@MOULIKGANDHI03](https://github.com/MOULIKGANDHI03) |

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repository
2. Create a feature branch (`git checkout -b my-feature`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin my-feature`)
5. Open a Pull Request 🚀
