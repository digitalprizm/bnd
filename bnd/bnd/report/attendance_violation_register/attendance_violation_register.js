// Copyright (c) 2016, Digitalprizm and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Violation Register"] = {
	"filters": [
		{
			"fieldname":"employee_name",
			"label": __("Employee Name"),
			"fieldtype": "Link",
			"options": "Employee"
			
		}
	]
}
