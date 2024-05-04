import os 
import sys
import platform

print("Installions des modules requis pour le MassDm:")
if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install --upgrade pip install psutil")
    os.system("pip install --upgrade pip install pip install colorama")

if sys.platform.startswith("linux"):
    "LINUX"
    os.system("pip install --upgrade pip install psutil")
    os.system("pip install --upgrade pip install pip install discord.py")
