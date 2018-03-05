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
					"name": "Shift",
					"description": _("Information about shift attendance."),
				},
				
				
			]
		},
		
		]
	