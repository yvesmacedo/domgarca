import os
import cherrypy
import platform
import methods
import urls

class Server():
	def __init__(self):
		logger = cherrypy.log.access_log
		logger.removeHandler(logger.handlers[0])

		cherrypy.config.update({
			"log.screen":True,
			"server.socket_port":methods.porta(),
			"enviroment":"production"
		})

		public_dir = os.path.dirname(os.path.abspath("README.md"))
		public_dir += "\\public" if platform.system() == "Windows" else "/public"

		conf = {}
		conf["/"]       = {"request.dispatch":urls.setup_urls()}
		conf["/public"] = {"tools.staticdir.on":True,"tools.staticdir.dir":public_dir}
		cherrypy.quickstart(cherrypy.tree.mount(None, config = conf))