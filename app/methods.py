# -*- coding: utf-8 -*-
import os
import hashlib
import platform
import base64

from jinja2 import Environment, FileSystemLoader

def appdata():
	return os.path.expanduser("~") + "\\AppData\\Local\\DomGarca" if platform.system() == "Windows" else os.path.expanduser("~") + "/.DomGarca"

def porta():
	return 3000

def view(folder = "mvc"):
	return Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath("README.md")), readfile(appdata() + "\\.dir","") + folder)))

def exists(d):
	if not os.path.exists(d):
		os.makedirs(d)
	return d

def readfile(f_path,default = False):
	try:
		f = open(f_path,"r")
		conteudo = f.read()
		f.close()
		return conteudo
	except Exception as err:
		return default

def writefile(f_path,conteudo,verificar_se_existe = False):
	if verificar_se_existe:
		if(os.path.exists(f_path)):
			conteudo_do_arquivo = readfile(f_path)
			if conteudo_do_arquivo == "":
				f = open(f_path,"w")
				f.write(conteudo)
				f.close()
				return conteudo
			return conteudo_do_arquivo 
		else:
			f = open(f_path,"w")
			f.write(conteudo)
			f.close()
			return conteudo
	else:
		f = open(f_path,"w")
		f.write(conteudo)
		f.close()
		return None