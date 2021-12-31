# -*- coding: utf-8 -*-
import os
import subprocess

from settings             import *
from methods              import *
from cherrypy.lib.static  import serve_file

class Index:
	def index(self,**kw):
		__nav = []
		for n in os.listdir("mvc"):
			if n.startswith("__"):
				x = __import__(n)
				if x.nav():
					for item in x.nav():
						__nav.append(item)

		return view().get_template("main.html").render(
			init  = kw["init"] if "init" in kw else readfile("mvc/home"),
			nav   = __nav
		)

	def img(self,**kw):
		return serve_file(readfile(APPDATA + "\\.dir","") + kw["i"])