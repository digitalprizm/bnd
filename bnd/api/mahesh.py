from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def get_leave_application(employee='',date=''):
	leave_list = ''
	
	if employee and date:
		leave_list = frappe.db.sql("""select employee,status, leave_type,leave_balance, from_date, to_date, total_leave_days,
			description, leave_approver, posting_date, company, half_day_date
			from `tabLeave Application`
			WHERE employee='{0}' and ('{1}' between from_date and to_date) """.format(employee,date),as_dict=1)
	elif employee :
		leave_list = frappe.db.sql("""select employee, status,leave_type, leave_balance, from_date, to_date, total_leave_days ,description, leave_approver, posting_date, company, half_day_date 
		from `tabLeave Application` WHERE employee='{0}'""".format(employee),as_dict=1)
	elif date :
		leave_list = frappe.db.sql("""select employee,status, leave_type,leave_balance, from_date, to_date, total_leave_days,
			description, leave_approver, posting_date, company, half_day_date
			from `tabLeave Application`
			WHERE  ('{0}' between from_date and to_date) """.format(date),as_dict=1)
	return leave_list 

@frappe.whitelist(allow_guest=True)
def get_employee_list(id=None,enroll_number=None):
	if id:
		employee_list = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    	from `tabEmployee` WHERE name='{0}' and `tabEmployee`.employee = `tabStore`.multi_unit_manager """.format(id),as_dict=1)
	elif enroll_number:
		employee_list = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    	from `tabEmployee` WHERE enroll_number='{0}'""".format(enroll_number),as_dict=1)
	else:
		employee_list = frappe.db.sql("""select  employee_name, 
			employee, 
			case when (1=1)
				then (select store_name from `tabEmployee` 
				where `tabEmployee`.employee = `tabStore`.multi_unit_manager)
				else 0
				end as store_name,
			name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    	from `tabEmployee` WHERE attendance_date='{0}'""".format(id),as_dict=1)
	return employee_list




# """select  employee_name, 
# 			employee, 
# 			case when (1=1)
# 				then (select store_name from `tabEmployee` 
# 				where `tabEmployee`.name = `tabStore`.multi_unit_manager)
# 				else 0
# 				end as store_name,
# 			name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
# 			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
# 	    	from `tabEmployee` WHERE attendance_date='{0}'""".format(id),as_dict=1
