from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, add_days 
from frappe import _

@frappe.whitelist()
def hello(doc,method):
	# query="""Select deduction_days, deduction_amount
	# from `tabAttendance Violation` where (attendance_date between '{0}' and '{1}')""".format(("start_date"),("end_date"))

	query="""Select deduction_days
	from `tabAttendance Violation`"""
	
	query1="""Select deduction_amount
	from `tabAttendance Violation`"""

	dl = frappe.db.sql(query,as_list=1,debug=1)
	d = frappe.db.sql(query1,as_list=1,debug=1)

	# print ("\n\n\n\n")
	# frappe.msgprint (dl)
	# frappe.msgprint (d)

	frappe.msgprint('Deduction days:'+str(dl[0]))
	frappe.msgprint('Deduction amount:'+str(d[0]))