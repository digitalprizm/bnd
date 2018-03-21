from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

#get emp list - store

#name pass or enrollement no

@frappe.whitelist(allow_guest=True)
def get_employee_details(id=None):
	if id:
		employee_details = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
		shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    from `tabEmployee` WHERE name='{0}' """.format(id),as_dict=1)
	else:
		employee_details = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
		shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    from `tabEmployee`""".format(employee_name),as_dict=1)

	return employee_details


@frappe.whitelist(allow_guest=True)
def get_shift_schedule_list(shift_name=None):
	if shift_name:
		shift_schedule_details = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    	from `tabShift Time` WHERE shift_name='{0}'""".format(shift_name),as_dict=1)
	else:
		shift_schedule_details = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    	from `tabShift Time`""".format(shift_name),as_dict=1)

	return shift_schedule_details


#store api

@frappe.whitelist(allow_guest=True)
def get_store_list(store_name=None):
	if store_name:
		store_list = frappe.db.sql("""select store_name, store_id, shift_timing1, shift_timing2, sun, mon, tue, wed, thu, fri, sat, store_address
			from `tabStore` WHERE store_name='{0}' """.format(store_name),as_dict=1)
	else:
		store_list = frappe.db.sql("""select store_name, store_id, shift_timing1, shift_timing2, sun, mon, tue, wed, thu, fri, sat, store_address\
			from `tabStore`""".format(store_name), as_dict=1)

	return store_list


#get hr parameter