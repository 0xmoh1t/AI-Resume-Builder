<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>🧠 AI Resume Builder</h1>
  <p>
    AI-Resume-Builder is an open-source web application that leverages artificial intelligence and LaTeX templating to help users generate professional, job-ready resumes with ease. This project provides a streamlined, customizable experience for resume creation—perfect for students, professionals, and developers alike.
  </p>

  <div class="section">
    <h2>📁 <span class="repo-link">View Repository:</span> <a href="https://github.com/0xmoh1t/AI-Resume-Builder" target="_blank">github.com/0xmoh1t/AI-Resume-Builder</a></h2>
  </div>

  <div class="section">
    <h2>🏁 Project Background</h2>
    <p>
      AI Resume Builder was developed as part of the IBM SkillsBuild – AI Agentic Internship Project. The program provides immersive, hands-on training for students and early-career professionals through real-world, mentor-led projects in artificial intelligence, machine learning, and cloud computing. Participants gain globally recognized credentials and develop solutions aligned with industry needs.
    </p>
  </div>

  <div class="section">
    <h2>✨ Key Features</h2>
    <ul>
      <li>🧾 <b>Customizable LaTeX Templates:</b> Modify <code>template.tex</code> to tailor the resume design to your preferences.</li>
      <li>⚙️ <b>Automated PDF Generation:</b> Input your resume data and instantly generate a polished PDF.</li>
      <li>🌐 <b>Web-Based UI:</b> Upload your data or job description through a sleek Flask-powered frontend.</li>
      <li>🐍 <b>Python + LaTeX Stack:</b> Built using Python and LaTeX for reliability, flexibility, and extensibility.</li>
      <li>🌍 <b>Open Source:</b> Freely available for personal, educational, or commercial use.</li>
    </ul>
  </div>

  <div class="section">
    <h2>📁 Project Structure</h2>
    <pre>
AI-Resume-Builder/
├── static/               # Static files (CSS, assets)
├── templates/            # HTML templates and LaTeX resume template
├── uploads/              # Uploaded resume data and generated PDFs
├── codehack_phantoms.py  # Main Python Flask backend
├── template.tex          # Base LaTeX template
├── requirements.txt      # Dependencies (if available)
    </pre>
  </div>

  <div class="section">
    <h2>🚀 Getting Started</h2>
    <h3>🔧 Prerequisites</h3>
    <ul>
      <li>Python 3.x</li>
      <li>Flask (<code>pip install flask</code>)</li>
      <li>LaTeX distribution (e.g., TeX Live or MiKTeX)</li>
    </ul>
  </div>

  <div class="section">
    <h2>📦 Installation & Setup</h2>
    <ol>
      <li><b>Clone the repository</b>
        <pre>git clone https://github.com/0xmoh1t/AI-Resume-Builder.git
cd AI-Resume-Builder</pre>
      </li>
      <li><b>Install dependencies</b>
        <pre>pip install flask flask-cors python-dotenv google-generativeai docx2txt pymupdf</pre>
      </li>
      <li><b>Set up your <code>.env</code> file</b>
        <pre>GEMINI_API_KEY=your_google_gemini_api_key</pre>
      </li>
      <li><b>Ensure <code>pdflatex</code> is installed</b> (Required for LaTeX to PDF conversion, video for refrence: https://youtu.be/Smd9Fnsy00U?si=eulUBvdLFnz-nzvE )</li>
      <li><b>Run the app</b>
        <pre>python codehack_phantoms.py</pre>
      </li>
      <li><b>Open in browser</b>
        <a href="http://localhost:5000" target="_blank">http://localhost:5000</a>
      </li>
    </ol>
  </div>

  <div class="section">
    <h2>💡 How It Works</h2>
    <ol>
      <li>Open the app in your browser.</li>
      <li>Upload your resume or input job description text.</li>
      <li>Click to generate a clean, structured PDF resume.</li>
      <li>Download your final result instantly.</li>
    </ol>
  </div>

  <div class="section contributors">
    <h2>👥 Contributors</h2>
    <ul>
      <li>
        <img src="https://avatars.githubusercontent.com/u/104442179?v=4" alt="Mohit" height="20" width="20">
        <a href="https://github.com/0xmoh1t" target="_blank">@0xmoh1t (Mohit)</a>
      </li>
      <li>
        <img src="https://avatars.githubusercontent.com/u/105893013?v=4" alt="Hardik" height="20" width="20">
        <a href="https://github.com/HardikIsACoder" target="_blank">@HardikIsACoder (Hardik Agrawal)</a>
      </li>
      <li>
        <img src="https://avatars.githubusercontent.com/u/116234377?v=4" alt="Moulik" height="20" width="20">
        <a href="https://github.com/MOULIKGANDHI03" target="_blank">@MOULIKGANDHI03 (Moulik Gandhi)</a>
      </li>
    </ul>
  </div>

  <div class="section">
    <h2>🧪 Tech Stack</h2>
    <ul>
      <li>Backend: Python, Flask</li>
      <li>Frontend: HTML, CSS</li>
      <li>PDF Generation: LaTeX</li>
    </ul>
  </div>

  <div class="section">
    <h2>🤝 Contributing</h2>
    <p>We welcome contributions!</p>
    <ol>
      <li>Fork the repo</li>
      <li>Create a new branch (<code>git checkout -b feature-name</code>)</li>
      <li>Commit your changes</li>
      <li>Open a pull request</li>
      <li>For major changes, please open an issue first to discuss your idea.</li>
    </ol>
  </div>

  <div class="section">
    <h2>📜 License</h2>
    <p>This project is licensed under an open-source license. See the <code>LICENSE</code> file for more information.</p>
  </div>
</body>
</html>
