// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt
cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
frappe.ui.form.on('Attendance Violation', {
	refresh: function(frm) {
	cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
	in_time= cur_frm.doc.in_time;
	out_time=cur_frm.doc.out_time;
	cur_frm.set_value("new_in_time",in_time);
	cur_frm.set_value("new_out_time",out_time);
	}
});
