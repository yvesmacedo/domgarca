import os
import cherrypy
import settings
import urls

class Server():
	def __init__(self):
		diretorio_atual = os.path.dirname(os.path.abspath("README.md"))

		logger = cherrypy.log.access_log
		logger.removeHandler(logger.handlers[0])

		cherrypy.config.update({
			"log.screen":True,
			"server.socket_port":settings.PORTA,
			"enviroment":"production"
		})

		conf = {}
		conf["/"]       = {"request.dispatch":urls.setup_urls()}
		conf["/public"] = {"tools.staticdir.on":True,"tools.staticdir.dir":diretorio_atual + "\\public"}
		cherrypy.quickstart(cherrypy.tree.mount(None, config = conf))