// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt
cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
cur_frm.add_fetch('shift_time', 'start_time', 'start_time');
cur_frm.add_fetch('shift_time', 'end_time', 'end_time');

frappe.ui.form.on('Shift Schedule', {
	refresh: function(frm) {

	}
});
