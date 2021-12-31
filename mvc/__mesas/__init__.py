# -*- coding: utf-8 -*-
from .controller import Mesas as Controller

def nav():
	return [{
		"0-position":0,
		"id"        :Controller.URL,    
		"url"       :"/" + Controller.URL + "/",
		"label"     :Controller.URL.capitalize()
	}]

def urls():
	return [{
		"nome":Controller.URL,
		"url" :"/" + Controller.URL + "/",
		"def" :Controller().index
	},{
		"nome":Controller.URL + "_add",
		"url" :"/" + Controller.URL + "_add/",
		"def" :Controller().add
	},{
		"nome":Controller.URL + "_remove",
		"url" :"/" + Controller.URL + "_remove/",
		"def" :Controller().remove
	}]