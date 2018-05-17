# Copyright (c) 2013, avu and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _





def execute(filters=None):
	if not filters: filters = {}

	conditions= get_conditions(filters)
	columns = get_columns(filters)
	data = get_shift_schdule(conditions,filters)

	return columns, data



def get_columns(filters):
	columns = [
		_("Employee id") + ":Link/Employee:120", _("Employee Name") + ":Data:200", _("Company")+ ":Link/Company:120",
		_("Store") + ":Link/Store:120"
	]
	from_date=filters.get("from_date")
	to_date=filters.get("to_date")
	while(from_date<=to_date):
		datecolumn= frappe.utils.data.formatdate (from_date, "dd-MM-yyyy")
		columns.append(datecolumn+":Link/Shift Time:120")
		from_date=frappe.utils.data.add_days (from_date,1)

	return columns




def get_conditions(filters):
	if not (filters.get("from_date") and filters.get("to_date")):
		frappe.msgprint(_("Please select From Date and To Date"), raise_exception=1)

	conditions = ""


	if filters.get("from_date"):
		f="\"{0}\"".format(str((filters.get("from_date"))))
		conditions += " and attendance_date>={0}".format(f)
	if filters.get("to_date"):
		t="\"{0}\"".format(str((filters.get("to_date"))))
		conditions += " and attendance_date<={0}".format(t)

	return conditions


def get_shift_schdule(conditions,filters):
	data = []
	firstcolumndate=frappe.utils.data.getdate (filters.get("from_date"))
	lastcolumndate=frappe.utils.data.getdate (filters.get("to_date"))
	
	employee_list = frappe.db.sql("""select employee,employee_name,company,store 
		from `tabEmployee` where status={0}""".format("\"Active\"") , as_dict=1)

	
	for i in range(0,len(employee_list)):
		emp=employee_list[i]
		row = [emp['employee'], emp['employee_name'],emp['company'], emp['store']]
		empname="\"{0}\"".format(str(emp['employee_name']))
		schedule_list = frappe.db.sql("""select employee,employee_name,company,store,attendance_date,
		shift_time from `tabShift Schedule` where docstatus = 1 and employee_name={0} {1} order by attendance_date""".format(empname,conditions), as_dict=1)
		#frappe.throw(str(schedule_list))
		for t in range(0,len(schedule_list)):
			shift=schedule_list[t]
			currentdatecolumn=firstcolumndate
			while(currentdatecolumn<=lastcolumndate):
				
				if shift['attendance_date']==currentdatecolumn:
					row+=[shift['shift_time']]
					break
				currentdatecolumn=frappe.utils.data.add_days (currentdatecolumn,1)
				

		data.append(row)
	return data
			
		
		