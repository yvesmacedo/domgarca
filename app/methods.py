# -*- coding: utf-8 -*-
import os
import hashlib
import base64
from settings import APPDATA
from jinja2   import Environment, FileSystemLoader

def view(folder = False):
	path = readfile(APPDATA + "\\.dir","")
	if not folder:
		folder = path + "mvc"
	else:
		folder = path + "mvc/" + folder + "/views"
	return Environment(loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath("README.md")),folder)))

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