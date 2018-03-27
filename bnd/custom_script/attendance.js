
cur_frm.add_fetch('employee', 'company', 'company');
cur_frm.add_fetch('employee', 'employee_name', 'employee_name');
frappe.ui.form.on("Attendance", "validate", function(frm) { 

 });

/*def validate_duplicate_record(self):
		res = frappe.db.sql("""select name from `tabAttendance` where employee = %s and attendance_date = %s
			and name != %s and docstatus = 1""",
			(self.employee, self.attendance_date, self.name))
		if res:
			frappe.throw(_("Attendance for employee {0} is already marked").format(self.employee))

		set_employee_name(self)*/