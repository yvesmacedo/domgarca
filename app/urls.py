# -*- coding: utf-8 -*-
import os
import cherrypy

itens = []
for mvc in os.listdir("mvc"):
	if mvc.startswith("__"):
		x = __import__(mvc)
		itens.append(x)

def setup_urls(**kw):
	d = cherrypy.dispatch.RoutesDispatcher()

	for i in itens:
		for u in i.urls():
			d.connect(u["nome"],u["url"],u["def"],**kw)

	return d