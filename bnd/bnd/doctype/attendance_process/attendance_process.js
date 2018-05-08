// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attendance Process', {
	refresh: function(frm) {
		cur_frm.disable_save();
		if (!cur_frm.doc.__islocal) {
				$(frm.fields_dict['attendance'].wrapper)
						.html(frappe.render_template("attendance_process", cur_frm.doc.__onload));
				
		}
	}
});
