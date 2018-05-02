frappe.ui.form.on("Salary Slip", "validate", function(frm) { 
	setTimeout(function(){ 
		cur_frm.reload_doc();
		 },
		  3000);
})