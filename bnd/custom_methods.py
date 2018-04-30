from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, add_days 
from frappe import _

@frappe.whitelist()
def hello(doc,method):
	# query="""Select deduction_days, deduction_amount
	# from `tabAttendance Violation` where (attendance_date between '{0}' and '{1}')""".format(("start_date"),("end_date"))

	query="""Select deduction_days, deduction_amount
	from `tabAttendance Violation` where (attendance_date between '{0}' and '{1}') and employee='{2}'""".format(doc.start_date, doc.end_date, doc.employee)

	dl = frappe.db.sql(query,as_list=1,debug=1)
	if dl:
		a = dl[0]
		frappe.msgprint('Deduction days:'+ str(a[0]))
		frappe.msgprint('Deduction amount:'+ str(a[1]))