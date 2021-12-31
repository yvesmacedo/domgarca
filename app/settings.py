# -*- coding: utf-8 -*-
import os

PORTA    = 3000
APPDATA  = os.path.expanduser("~") + "\\AppData\\Local\\DomGarca"

if not os.path.exists(APPDATA):
	os.makedirs(APPDATA)