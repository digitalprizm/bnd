from frappe import _

def get_data():
	return [
		{
			"label": _("Store"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Store",
					"description": _("Information about store."),
				},
				{
					"type": "doctype",
					"name": "Device",
					"description": _("Information about Device."),
				},
				{
					"type": "doctype",
					"name": "Shift Time",
					"description": _("Information about shift attendance."),
				},
				{
					"type": "doctype",
					"name": "Shift Schedule",
					"description": _("Information about shift attendance."),
				},
				{
					"type": "doctype",
					"name": "Shift Schedule Exception",
					"description": _("Information about shift attendance."),
				},
				{
					"type": "doctype",
					"name": "Attendance Violation",
					"description": _("Information about shift attendance."),
				},				
			]
		},
		
		]
	