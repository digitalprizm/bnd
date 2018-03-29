// Copyright (c) 2016, Digitalprizm and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Shift Schedule Exception Details"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_end_date"),
			"reqd": 1
		},		
		{
			"fieldname": "store",
			"label": __("Store"),
			"fieldtype": "Link",
			"options": "Store",
		},
		{
			"fieldname":"employee",
			"label":__("Employee"),
			"fieldtype":"Link",
			"options": "Employee",
		}

	]
}
