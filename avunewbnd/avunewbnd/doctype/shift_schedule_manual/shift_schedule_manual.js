// Copyright (c) 2018, avu and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shift Schedule Manual', {
	refresh: function(frm) {
cur_frm.disable_save();
if (!cur_frm.doc.__islocal) {
		$(frm.fields_dict['schedule'].wrapper)
				.html(frappe.render_template("data_list", cur_frm.doc.__onload));
		
}

	}
});
