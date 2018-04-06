# Copyright (c) 2013, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
import re
import functools
from frappe.utils import getdate, nowdate, flt, cint

def execute(filters):
	period_list = ["2014","2015","2016"]
	columns, data = [], []
	columns = get_columns(period_list)
	data = get_data(filters)
	validate_filters(filters)
	return columns, data


def validate_filters(filters):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))


def get_data(filters):
	query="""Select employee, employee_name, attendance_date, store, shift_time, time_format(start_time,'%H:%i'), time_format(end_time,'%H:%i')
	    from `tabShift Schedule` where (attendance_date between '{0}' 
	and '{1}')""".format(filters.get("from_date"),filters.get("to_date"))

	if filters.get("store"):
		query += """	and store= '{0}'	""".format(filters.get("store"))


	if filters.get("employee"):
		query += """	and employee= '{0}'	""".format(filters.get("employee"))

	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl

def  get_columns(period_list):
	columns = ["Employee Id:Link/Employee:95"]+["Employee Name:Data:140"]+["Attendance Date:Date:100"]\
		+["Store:Link/Store:70"]+["Shift Time:Link/Shift Time:100"]+["Start Time:Time:70"]+["End Time:Time:70"]
	return columns