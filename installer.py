import os, sys
from pathlib import Path
home = str(Path.home())

dir_path = os.path.dirname(os.path.realpath(__file__))

os.system("sudo apt install torsocks")

with open(home + "/.bashrc", "a") as myfile:
    myfile.write("\nalias lb='cd " + dir_path + " && source venv/bin/activate && python run.py'")