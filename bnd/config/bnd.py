from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "fa fa-star",
			"items": [
				
				{
					"type": "doctype",
					"name": "Shift Schedule",
					"description": _("Shift Schedule"),
				},
				{
					"type": "doctype",
					"name": "Shift Schedule Exception",
					"description": _("Shift Schedule Exception"),
				},
				{
					"type": "doctype",
					"name": "Attendance",
					"description": _("Attendance"),
				},

				{
					"type": "doctype",
					"name": "Attendance Violation",
					"description": _("Attendance Violation"),
				},
				{
					"type": "doctype",
					"name": "HR Parameter",
					"description": _("HR Parameter"),
				},								
			]
		},
		{
			"label": _("Master"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Store",
					"description": _("Store"),
				},
				{
					"type": "doctype",
					"name": "Device",
					"description": _("Device"),
				},
								{
					"type": "doctype",
					"name": "Shift Time",
					"description": _("Shift Time"),
				},
				{
					"type": "doctype",
					"name": "Area",
					"description": _("Area"),
				},
				{
					"type": "doctype",
					"name": "HR Parameter",
					"description": ""
				},			
			]
		},
		{
			"label": _("Tools"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Upload Shift Schedule",
					"description": _("Upload Shift Schedule"),
				},
								
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Attendance Sheet",
					"doctype": "Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Details",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Shift Schedule Details",
					"doctype": "Shift Schedule"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Shift Schedule Exception Details",
					"doctype": "Shift Schedule Exception"
				},
			]
		},
		
	]