# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "BnD",
			"color": "#019941",
			"icon": "fa fa-subway",
			"type": "module",
			"label": _("BND")
		},
		{
			"module_name": "Store",
			"_doctype": "Store",
			"color": "#0f9155",
			"icon": "fa fa-truck",
			"type": "link",
			"link": "List/Store"
		},

		{
			"module_name": "Device",
			"_doctype": "Device",
			"color": "#cb3fcd",
			"icon": "fa fa-server",
			"type": "link",
			"link": "List/Device"
		},
		{
			"module_name": "Shift Time",
			"_doctype": "Shift Time",
			"color": "#600080",
			"icon": "fa fa-calendar-plus-o",
			"type": "link",
			"link": "List/Shift Time"
		},
		{
			"module_name": "Shift Schedule",
			"_doctype": "Shift Schedule",
			"color": "#4dab9e",
			"icon": "fa fa-calendar",
			"type": "link",
			"link": "List/Shift Time"
		},
	]
