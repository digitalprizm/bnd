// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attendance Violation', {
	refresh: function(frm) {
	cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
	}
});
