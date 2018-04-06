# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, getdate
from frappe import msgprint, _
from calendar import monthrange

def execute(filters=None):
	if not filters: filters = {}

	# conditions, filters = get_conditions(filters)
	columns = get_columns(filters)
	att_map = get_shift_schedule_list(filters)
	# emp_map = get_employee_details()

	# holiday_list = [emp_map[d]["holiday_list"] for d in emp_map if emp_map[d]["holiday_list"]]
	# default_holiday_list = frappe.db.get_value("Company", filters.get("company"), "default_holiday_list")
	# holiday_list.append(default_holiday_list)
	# holiday_list = list(set(holiday_list))
	# holiday_map = get_holiday(holiday_list, filters["month"])

	data = []
	for i in att_map:
		row=[1,2,3,4,5,6,7,8,9,0]
		data.append(row)

	# for emp in sorted(att_map):
	# 	emp_det = emp_map.get(emp)
	# 	if not emp_det:
	# 		continue

	# 	row = [emp, emp_det.employee_name, emp_det.branch, emp_det.department, emp_det.designation, emp_det.store,
	# 		emp_det.company]

	# 	total_p = total_a = total_l = 0.0
		# for day in range(filters["total_days_in_month"]):
		# 	status = att_map.get(emp).get(day + 1, "None")
		# 	status_map = {"Present": "P", "Absent": "A", "Half Day": "HD", "On Leave": "L", "None": "<span style='color: red;'>-</span>", "Holiday":"<b>H</b>"}
		# 	if status == "None" and holiday_map:
		# 		emp_holiday_list = emp_det.holiday_list if emp_det.holiday_list else default_holiday_list
		# 		if emp_holiday_list in holiday_map and (day+1) in holiday_map[emp_holiday_list]:
		# 			status = "Holiday"
		# 	row.append(status_map[status])

		# 	if status == "Present":
		# 		total_p += 1
		# 	elif status == "Absent":
		# 		total_a += 1
		# 	elif status == "On Leave":
		# 		total_l += 1
		# 	elif status == "Half Day":
		# 		total_p += 0.5
		# 		total_a += 0.5

		# row += [total_p, total_l, total_a]

	return columns, data

def get_columns(filters):
	columns = [
		_("Employee") + ":Link/Employee:120", _("Employee Name"), 
		_("Shift Time") + ":Link/Shift Time:120",
	]

	for day in range(0,7):
		columns.append(cstr(day+1) +"::20")

	# columns += [_("Total Present") + ":Float:80", _("Total Leaves") + ":Float:80",  _("Total Absent") + ":Float:80"]
	return columns

def get_shift_schedule_list(filters):

	attendance_list = frappe.db.sql("""Select employee, shift_time, attendance_date
	    from `tabShift Schedule` where (attendance_date between '{0}' 
		and '{1}') order by  employee, attendance_date""", as_dict=1)
	# frappe.msgprint("hiii")

	# return attendance_list
	att_map = {}
	for d in attendance_list:
		att_map.setdefault(d.employee, frappe._dict()).setdefault(d.day_of_month, "")
		att_map[d.employee][d.day_of_month] = d.status

	return att_map

# def get_conditions(filters):
# 	if not (filters.get("month") and filters.get("year")):
# 		msgprint(_("Please select month and year"), raise_exception=1)

# 	filters["month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
# 		"Dec"].index(filters.month) + 1

# 	filters["total_days_in_month"] = monthrange(cint(filters.year), filters.month)[1]

# 	conditions = " and month(attendance_date) = %(month)s and year(attendance_date) = %(year)s"

# 	if filters.get("company"): conditions += " and company = %(company)s"
# 	if filters.get("employee"): conditions += " and employee = %(employee)s"

# 	return conditions, filters

# def get_employee_details():
# 	emp_map = frappe._dict()
# 	for d in frappe.db.sql("""select name, employee_name, designation, department, branch, company,
# 		holiday_list,store from `tabEmployee`""", as_dict=1):
# 		emp_map.setdefault(d.name, d)

# 	return emp_map

# def get_holiday(holiday_list, month):
# 	holiday_map = frappe._dict()
# 	for d in holiday_list:
# 		if d:
# 			holiday_map.setdefault(d, frappe.db.sql_list('''select day(holiday_date) from `tabHoliday`
# 				where parent=%s and month(holiday_date)=%s''', (d, month)))

# 	return holiday_map

# @frappe.whitelist()
# def get_attendance_years():
# 	year_list = frappe.db.sql_list("""select distinct YEAR(attendance_date) from `tabShift Schedule` ORDER BY YEAR(attendance_date) DESC""")
# 	if not year_list:
# 		year_list = [getdate().year]

# 	return "\n".join(str(year) for year in year_list)