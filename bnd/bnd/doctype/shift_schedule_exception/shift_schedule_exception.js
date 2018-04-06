// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt
cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
frappe.ui.form.on('Shift Schedule Exception', {
	refresh: function(frm) {

	},
	get_shift_schedule: function(frm) {
		return frappe.call({
			method: "get_shift_schedule",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh_fields();
			}
		});
	},
	attendance_date: function(frm) {
		return frappe.call({
			method: "get_shift_schedule",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh_fields();
			}
		});
	},
});
