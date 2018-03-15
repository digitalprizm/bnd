// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Roaster Tool', {
	refresh: function(frm) {
		frm.disable_save();
	},
	onload: function(frm) {
		frm.set_value("from_date", frappe.datetime.month_start());
		frm.set_value("to_date", frappe.datetime.month_end());
	},
});
