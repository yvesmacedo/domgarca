import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath("index.html")),"app"))

from settings import *
from cefpython3 import cefpython

f = open(APPDATA + "\\.dir","r")
URL = f.read() + "index.html"
f.close()

if __name__ == '__main__':
    cefpython.Initialize()
    cefpython.CreateBrowserSync(url = URL, window_title = "Dom Garça")
    cefpython.MessageLoop()
    cefpython.Shutdown()