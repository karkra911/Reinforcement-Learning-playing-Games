import os
import subprocess

# Create folders for Python 2 and Python 3
python2_folder = "python2"
python3_folder = "python3"
os.makedirs(python2_folder, exist_ok=True)
os.makedirs(python3_folder, exist_ok=True)

# Install Python 2
subprocess.run(["pyenv", "install", "2.7.18"], cwd=python2_folder)
subprocess.run(["pyenv", "global", "2.7.18"], cwd=python2_folder)
subprocess.run(["pyenv", "exec", "pip", "install", "--upgrade", "pip"], cwd=python2_folder)

# Install Python 3
subprocess.run(["pyenv", "install", "3.9.6"], cwd=python3_folder)
subprocess.run(["pyenv", "global", "3.9.6"], cwd=python3_folder)
subprocess.run(["pyenv", "exec", "pip", "install", "--upgrade", "pip"], cwd=python3_folder)
