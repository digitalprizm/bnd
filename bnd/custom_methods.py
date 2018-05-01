from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, add_days 
from frappe import _

@frappe.whitelist()
def salary_slip(doc,method):
	query="""Select sum(deduction_days), sum(deduction_amount)
	from `tabAttendance Violation` where (attendance_date between '{0}' and '{1}') and employee='{2}'""".format(doc.start_date, doc.end_date, doc.employee)
	deduction_data = frappe.db.sql(query,as_list=1,debug=1)
	if deduction_data:
		deduction = deduction_data[0]
		doc.deduction_days = deduction[0]
		doc.deduction_amount = deduction[1]
		frappe.msgprint('Deduction days:'+ str(doc.deduction_days) )
		frappe.msgprint('Deduction amount:'+ str(doc.deduction_amount) )

	mycheck = False
	for i in doc.deductions:
		if i.salary_component == "Attendance Violation":
			mycheck = True
			i.amount = doc.deduction_amount
	if mycheck:
		pass
	else:
		row = doc.append('deductions', {})
		row.salary_component = "Attendance Violation"
		row.amount =doc.deduction_amount
	doc.reload()