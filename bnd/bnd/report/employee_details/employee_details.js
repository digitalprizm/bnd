// Copyright (c) 2016, Digitalprizm and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Details"] = {
	"filters": [
		{
            "fieldname":"Store",
			"label": __("Store"),
			"fieldtype": "Link",
			"options": "Store",
        },
	]
}
