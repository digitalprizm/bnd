frappe.ui.form.on("Salary Slip", "validate", function(frm) { 
		deduction_amount = cur_frm.doc.deduction_amount;
		frappe.msgprint(deduction_amount);
	var row = frappe.model.add_child(cur_frm.doc, "Salary Slip", "deductions");
	    row.salary_component = "Attendance Violation";
	    row.amount = Math.round(deduction_amount);
		refresh_field("deductions");
});