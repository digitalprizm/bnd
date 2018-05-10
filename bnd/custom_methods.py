from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, add_days 
from frappe import _
# from frappe.utils import (flt, getdate, get_first_day, get_last_day, date_diff,
# 	add_months, add_days, formatdate, cint)

@frappe.whitelist()
def salary_slip(doc,method):
	query="""Select sum(deduction_days), sum(deduction_amount)
	from `tabAttendance` where (attendance_date between '{0}' and '{1}') and employee='{2}'""".format(doc.start_date, doc.end_date, doc.employee)
	deduction_data = frappe.db.sql(query,as_list=1,debug=1)
	if deduction_data:
		deduction = deduction_data[0]
		doc.deduction_days = deduction[0]
		doc.deduction_amount = deduction[1]
		if doc.deduction_amount >= 1 or doc.deduction_days >=1 :
			frappe.msgprint('Deduction days:'+ str(doc.deduction_days) )
			frappe.msgprint('Deduction amount:'+ str(doc.deduction_amount) )

	flag = False
	for i in doc.deductions:
		if i.salary_component == "Attendance Violation":
			flag = True
			i.amount = doc.deduction_amount
	if flag:
		pass
	elif doc.deduction_amount >= 1:
		row = doc.append('deductions', {})
		row.salary_component = "Attendance Violation"
		row.amount =doc.deduction_amount

		present="""Select count(*)
	from `tabAttendance` where (status = 'Present' and attendance_date between '{0}' and '{1}') and employee='{2}' """.format(doc.start_date, doc.end_date, doc.employee)
		attendance_present = frappe.db.sql(present,as_list=1,debug=1)
		absent="""Select count(*)
	from `tabAttendance` where (status = 'Absent' and attendance_date between '{0}' and '{1}') and employee='{2}' """.format(doc.start_date, doc.end_date, doc.employee)
		attendance_absent = frappe.db.sql(absent,as_list=1,debug=1)
		present_count=attendance_present[0]
		absent_count=attendance_absent[0]
		doc.total_present_days= str(present_count[0])
		doc.total_absent_days = str(absent_count[0])


@frappe.whitelist()
def create_attendance(doc,method):
	frappe.msgprint("hi from c m")
	attendance_doc = frappe.new_doc("Attendance")
	attendance_doc.employee = doc.employee
	#if Leave application  is for 3 days, then it will create 3 attendance
	attendance_doc.attendance_date = doc.from_date
	#frappe.db.get value from Leave type, if leave type is LWP, 
	# then mrk as absent, else mark as present
	#frappe
	# attendance_doc.status = doc.
	attendance_doc.company = doc.company
	attendance_doc.insert()
	attendance_doc.save()
	attendance_doc.submit()
	# (attendance_doc.leave_application)_refference = self.name


	leave_type = frappe.db.get_value("Leave Application","leave_type")
	if leave_type == "LWP":
	 	attendance_doc.status = "Absent"
	else:
		attendance_doc.status = "Present"
	
	# attendance_doc.employee_name = self.employee_name
	# attendance_doc.in_time = self.in_time
	# attendance_doc.out_time = self.out_time
	# attendance_doc.new_in_time = self.amended_in_time
	# attendance_doc.new_out_time = self.amended_out_time
	# attendance_doc.in_store = self.amended_in_store
	# attendance_doc.out_store = self.amended_out_store
	# attendance_doc.total_working_hours = self.total_working_hours
	# attendance_doc.status1 = self.amended_status1
	# attendance_doc.status2 = self.amended_status2
	# attendance_doc.ot_hours = self.ot_hours
	# attendance_doc.schedule_time = self.schedule_time
	# attendance_doc.schedule_store = self.schedule_store

	# attendance_doc1.employee = self.employee
	

	# self.attendance = attendance_doc.name 
	# self.attendance = attendance_doc1.name

	# frappe.msgprint("""<html> <body>New attendance <a href="#Form/Attendance/{0}">{0}</a> is created</body>
	# </html>""".format(attendance_doc.name, attendance_doc1.name))
	
	# frappe.msgprint("New Attendance {0} is created".format(attendance_doc.name, attendance_doc1.name))
