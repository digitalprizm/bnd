# # Copyright (c) 2013, Digitalprizm and contributors
# # For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe.utils import getdate, nowdate, flt, cint


def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data(filters)
	validate_filters(filters)

	return columns, data

def validate_filters(filters):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))


def get_data(filters):
	query="""Select  employee,attendance_date, shift_schedule_old_time,old_store_location,
	shift_schedule,shift_schedule__new_time,store_location,store_location_out,new_store_location,reason 
	from `tabShift Schedule Exception`where (attendance_date between '{0}' and '{1}')""".format(filters.get("from_date"),filters.get("to_date"))
	

	if filters.get("store"):
		query += """	and new_store_location= '{0}'	""".format(filters.get("store"))

	if filters.get("employee"):
		query += """	and employee= '{0}'	""".format(filters.get("employee"))
	
	dl = frappe.db.sql(query,as_list=1,debug=1)
	
	return dl

def get_colums():

	columns = ["Employee:Link/Employee:100"]+["Attendance Date:Date:100"]\
	+["Shift Schedule Old Time:Link/Shift Time:100"]+["Old Store Location:Link/Store:100"]\
	+["Shift Schedule:Link/Shift Time:100"]+["Shift Schedule  New Time:Link/Shift Time:100"]+["Store Location In:Link/Store:100"]\
	+["Store Location Out:Link/Store:100"]	+["Store Location In:Link/Store:100"]+["Reason:Data:100"]

	return columns
