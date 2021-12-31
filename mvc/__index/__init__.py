# -*- coding: utf-8 -*-
from . import controller

def nav():
	return []

def urls():
	return [{
		"nome":"index",
		"url" :"/",
		"def" :controller.Index().index
	},{
		"nome":"img",
		"url" :"/img/",
		"def" :controller.Index().img
	}]