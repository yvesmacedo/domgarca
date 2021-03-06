# -*- coding: utf-8 -*-
import os
from methods   import *
from sqlobject import *

from __1_produtos.model import ProdutosModel 

__connection__ = "sqlite:" + appdata() + "\\database.db"

ORDER_BY = "nome ASC"
SINGULAR = "Mesa"
PLURAL   = SINGULAR + "s"
ACTION   = PLURAL.lower()

class MesasModel(SQLObject):
	nome       = IntCol()#numero da mesa
	cliente_id = IntCol()
	produtos   = StringCol()
	obs        = StringCol()

	@classmethod
	def start(self,**kw):
		if not self.tableExists():
			self.createTable()

	@classmethod
	def form(self,id):
		c = False
		if not id == 0:
			c = self.get(id)
	
		ProdutosModel.start()#verificar se a tabela existe
		lista_de_produtos = ProdutosModel.select().orderBy(["nome ASC"])

		fields = [{
			"type" :"hidden",
			"name" :"id",
			"value":id,
			"class":""
		},{
			"type" :"text",
			"label":"Número da Mesa",
			"name" :"nome",
			"value":c.nome if c else "",
			"class":""
		},{
			"type" :"view",
			"label":"Produtos",
			"name" :"produtos",
			"value":c.produtos if c else "",
			"class":"",
			"view" :"produtos.html",
			"list" :lista_de_produtos
		},{
			"type" :"textarea",
			"label":"Observações",
			"name" :"obs",
			"value":c.obs if c else "",
			"class":""
		}]

		return {
			"action":"/" + ACTION + "_add/",
			"method":"post",
			"class" :"add_form",
			"title" :"Adicionar " + SINGULAR if id == 0 else u"Editar " + SINGULAR,
			"fields":fields
		}

	@classmethod
	def table(self, q, p, qt = 50):
		num_rows   = False
		num_start  = False
		num_end    = False
		num_next   = False
		num_before = False

		if q:
			if q.startswith("*"):
				q = q.replace("*","")
				itens = self.select(self.q.nome.endswith(q)).orderBy(["nome ASC"])
			elif q.endswith("*"):
				q = q.replace("*","")
				itens = self.select(self.q.nome.startswith(q)).orderBy(["nome ASC"])
			else:
				itens = self.select(self.q.nome.contains(q)).orderBy(["nome ASC"])
		else:
			itens = self.select().orderBy(["nome ASC"])

		try:
			p = int(p)
			start = qt * (p - 1)
		except:
			p = 1
			start = 0

		num_rows = itens.count()
		itens    = itens[start:(start + qt)]

		num_start  = start + 1
		num_end    = num_rows if (start + qt) > num_rows else (start + qt)
		num_next   = p + 1
		num_before = p - 1

		lines = []
		for i in itens:
			lines.append([
				i.id,
				[i.nome]
			])

		t = {
			"head"   :["Nome"],
			"body"   :lines,
			"start"  :num_start,
			"end"    :num_end,
			"total"  :num_rows,
			"next"   :num_next,
			"before" :num_before,
			"url"    :"/" + ACTION + "/?",
			"buttons":[
				{
					"btn"   :"primary",
					"icon"  :"search",
					"action":"get_id_and_go(this,'/" + ACTION + "/?id=')",
				},{
					"btn"   :"danger",
					"icon"  :"close",
					"action":"get_id_and_ask_before_go(this,'Deseja realmente apagar este item?','/" + ACTION + "_remove/?id=')",
				}
			]
		}

		return t