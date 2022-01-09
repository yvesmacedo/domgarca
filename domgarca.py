# -*- coding: utf-8 -*-
import os
import sys
import platform

ARQUIVO = "README.md"
APPDATA = os.path.expanduser("~") + "\\AppData\\Local\\DomGarca" if platform.system() == "Windows" else os.path.expanduser("~") + "/.DomGarca"

if not os.path.exists(APPDATA):
	os.makedirs(APPDATA)

f = open(APPDATA + "\\.dir","w")
f.write(os.path.join(os.path.dirname(os.path.abspath(ARQUIVO)),""))
f.close()

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(ARQUIVO)),"mvc"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(ARQUIVO)),"app"))

from servidor import Server

if __name__=="__main__":
	Server()