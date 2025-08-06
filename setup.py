import subprocess
import sys
import os

def run(cmd):
    print(f"🔧 Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# Step 1: System dependencies (Linux only)
if sys.platform.startswith("linux"):
    print("📦 Installing system dependencies...")
    run("sudo apt-get update")
    run("sudo apt-get install -y texlive-latex-base")  # Only what's needed for pdflatex

# Step 2: Create and activate virtual environment
venv_dir = "venv"
print(f"\n📁 Creating virtual environment at ./{venv_dir} ...")
subprocess.run([sys.executable, "-m", "venv", venv_dir])

pip_path = os.path.join(venv_dir, "bin", "pip") if os.name != "nt" else os.path.join(venv_dir, "Scripts", "pip.exe")

# Step 3: Install Python dependencies
print("\n📥 Installing Python dependencies...")

packages = [
    "flask",
    "flask-cors",
    "python-dotenv",
    "Werkzeug",
    "google-generativeai",
    "docx2txt",
    "pymupdf",              # (aka fitz)
    "pdflatex",
    "jinja2"
]

run(f"{pip_path} install " + " ".join(packages))

# Step 4: Done
print("\n✅ All set!")
if os.name == "nt":
    print("🔧 Activate with: venv\\Scripts\\activate")
else:
    print("🔧 Activate with: source venv/bin/activate")
