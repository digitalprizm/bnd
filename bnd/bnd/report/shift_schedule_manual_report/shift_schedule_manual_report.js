// Copyright (c) 2016, avu and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Shift Schedule Manual Report"] = {
	"filters": [
	{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			"width": "80"
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		}

	]
}
