# -*- coding: utf-8 -*-
import os
import string
import subprocess

from methods import *
from .model  import MesasModel as Model

class Mesas:
	URL = "mesas"

	def index(self,**kw):
		Model.start()
		
		q          = kw["q"].encode("utf-8") if "q" in kw else None
		az_current = q[:-1] if q and q.endswith("*") and len(q) == 2 else None
		p          = kw["p"]  if "p"  in kw else None
		id         = kw["id"] if "id" in kw else 0

		return view().get_template("index.html").render(
			id        = id,
			form      = Model.form(id),
			table     = Model.table(q,p),
			title     = self.URL.capitalize(),
			search    = "/" + self.URL + "/",
			menu      = self.URL
		)

	def add(self,**kw):
		try:
			if int(kw["id"]) == 0:
				Model(
					nome       = kw["nome"],
					cliente_id = int(kw["cliente_id"]),
					produto    = kw["matutino"],
					obs        = kw["vespertino"]
				)
			else:
				Model.get(int(kw["id"])).set(
					nome       = kw["nome"],
					cliente_id = int(kw["cliente_id"]),
					produto    = kw["matutino"],
					obs        = kw["vespertino"]
				)
			return "go:/mesas/"
		except Exception as err:
			return u"" + str(err)

	def remove(self,**kw):
		try:
			Model.delete(int(kw["id"]))
			return "Apagado com sucesso!"
		except Exception as err:
			return u"" + str(err)