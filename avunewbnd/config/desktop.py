# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "avunewbnd",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("avunewbnd")
		},
{
			"module_name": "Shift Schedule Manual",
			"_doctype": "Shift Schedule Manual",
			"color": "#D13E29",
			"icon": "fa fa-upload",
			"type": "link",
			"link": "List/Shift Schedule Manual"
		}
	]
