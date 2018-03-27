from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"


# get leave application you can get record employee wise and from date wise 
# http://0.0.0.0:8000/api/method/bnd.api.mahesh.get_leave_application?date=10-03-2018&&EMP/0001
@frappe.whitelist(allow_guest=True)
def get_leave_application(employee='',from_date=''):
	leave_list = ''
	
	if employee and from_date:
		leave_list = frappe.db.sql("""select employee,status, leave_type,leave_balance, from_date, to_date, total_leave_days ,description, leave_approver, posting_date, company, half_day_date
			from `tabLeave Application` WHERE employee='{0}' and from_date='{1}' """.format(employee,from_date),as_dict=1)
	elif employee :
		leave_list = frappe.db.sql("""select employee, status,leave_type, leave_balance, from_date, to_date, total_leave_days ,description, leave_approver, posting_date, company, half_day_date 
		from `tabLeave Application` WHERE employee='{0}'""".format(employee),as_dict=1)
	return leave_list 
