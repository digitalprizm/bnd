// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt

frappe.provide("erpnext.utils");

frappe.ui.form.on('Device Process', {
	refresh: function(frm) {
cur_frm.disable_save();
cur_frm.add_custom_button("Fetch All Device Data",function(){

			cur_frm.refresh();
		});
	//console.log(cur_frm.fields_dict)
		if (!cur_frm.doc.__islocal) {

			$(cur_frm.fields_dict['device'].wrapper)
				.html(frappe.render_template("device_list", cur_frm.fields_dict['__onload']));
		}


	},
		
	process_date: function(frm) {
		//frappe.msgprint("Heloo");

		
		frappe.call({
			"method": "avunewbnd.avunewbnd.doctype.device_process.device_process.load_devicelist",
			args: { 
				
				"process_date": cur_frm.doc.process_date
				
			},
			callback:function(r){ 
				//your script
				//console.log(r.message);
				if (!cur_frm.doc.__islocal) {
			$(cur_frm.fields_dict['device'].wrapper)
				.html(frappe.render_template("device_list", {device_list:r.message}));
		}
			}
		})
}



	});
