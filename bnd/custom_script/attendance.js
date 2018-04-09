
cur_frm.add_fetch('employee', 'company', 'company');
cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
frappe.ui.form.on("Attendance", "validate", function(frm) { 
	in_time= cur_frm.doc.in_time;
	out_time=cur_frm.doc.out_time;
	cur_frm.set_value("new_in_time",in_time);
	cur_frm.set_value("new_out_time",out_time);
 });

