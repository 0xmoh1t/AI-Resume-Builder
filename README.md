# 🧠 AI Resume Builder

AI Resume Builder is an open-source project that uses **AI + LaTeX** to transform your existing resume into a clean, job-optimized, ATS-friendly PDF using a customizable LaTeX template.

This was developed as part of the **IBM SkillsBuild AI Agentic Internship**, with a focus on intelligent automation, AI integration, and professional document enhancement using LaTeX and Gemini.

---

## 🚀 Features

- 📄 Upload your resume (PDF or DOCX)
- 🧠 Uses Google Gemini API to enhance your resume based on job description
- 📘 Custom LaTeX template with structured formatting
- 📤 Automatically compiles to PDF using `pdflatex`
- 🌐 Simple Flask-based web interface
- 💡 AI-powered rewriting, ATS optimization, hyperlink handling, and section prioritization

---

## 🏗️ Project Structure

```
AI-Resume-Builder/
├── static/               # Static files like CSS
├── templates/            # HTML templates (Flask frontend)
├── uploads/              # Uploaded resumes & generated PDFs
├── template.tex          # LaTeX resume template
├── codehack_phantoms.py  # Flask backend server
├── setup.py              # Python venv & pip install script
└── .env                  # Gemini API key configuration
```

---

## 📦 Requirements

- Windows 10/11 with WSL enabled
- Python 3.11+
- LaTeX (via TeX Live on Ubuntu through WSL)
- Google Gemini API Key

---

## ⚙️ Installation Guide

### 🪟 Step 1: Enable WSL and Install Ubuntu on Windows

#### 1. Open PowerShell as Administrator and run:

```powershell
wsl --install -d Ubuntu
```

This installs WSL and Ubuntu. Restart your PC if prompted.

#### 2. After restart, launch Ubuntu and create a UNIX username/password.

---

### 🐧 Step 2: Install LaTeX and Dependencies in Ubuntu (WSL)

Open your WSL (Ubuntu) terminal by command:

```bash
wsl
```

and run:

```bash
sudo apt update
sudo apt install -y texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-fonts-extra texlive-font-utils python3-venv python3-pip
```

---

### 📁 Step 3: Clone the Repository and Set Up Environment

```bash
git clone https://github.com/0xmoh1t/AI-Resume-Builder.git
cd AI-Resume-Builder
python3 setup.py
```

---

### 🔐 Step 4: Configure Gemini API Key

Create a `.env` file in the root directory with this content:

```
GEMINI_API_KEY=your_google_api_key_here
```

---

## 🧲 Run the App

```bash
source venv/Scripts/Activate
python3 codehack_phantoms.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🧠 How It Works

1. Upload your resume (PDF or DOCX)
2. Paste your target job description
3. Gemini rewrites and adapts your resume using LaTeX
4. PDF gets compiled automatically with `pdflatex`
5. Download your enhanced, job-ready resume!

---

## 🧰 Tech Stack

| Component      | Technology                  |
| -------------- | --------------------------- |
| **Backend**    | Python, Flask               |
| **Frontend**   | HTML, CSS (Flask templates) |
| **AI**         | Google Gemini API           |
| **PDF Output** | LaTeX + pdfTeX (pdflatex)   |

---

## 👨‍💼 Contributors

| Name   | GitHub Handle                                        |
| ------ | ---------------------------------------------------- |
| Mohit  | [@0xmoh1t](https://github.com/0xmoh1t)               |
| Hardik | [@HardikIsACoder](https://github.com/HardikIsACoder) |
| Moulik | [@MOULIKGANDHI03](https://github.com/MOULIKGANDHI03) |

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
