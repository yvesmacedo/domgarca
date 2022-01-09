# -*- coding: utf-8 -*-
from methods  import *
from .model   import ProdutosModel as Model

class Produtos:
	URL = "produtos"

	def index(self,**kw):
		Model.start()
		
		q          = kw["q"] if "q" in kw else None
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
					nome      = kw["nome"],
					descricao = kw["descricao"],
					categoria = kw["categoria"],
					variacao  = kw["variacao"],
					preco     = kw["preco"]
				)
			else:
				Model.get(int(kw["id"])).set(
					nome      = kw["nome"],
					descricao = kw["descricao"],
					categoria = kw["categoria"],
					variacao  = kw["variacao"],
					preco     = kw["preco"]
				)
			return "go:/produtos/"
		except Exception as err:
			return u"" + str(err)

	def remove(self,**kw):
		try:
			Model.delete(int(kw["id"]))
			return "Apagado com sucesso!"
		except Exception as err:
			return u"" + str(err)