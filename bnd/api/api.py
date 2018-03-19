from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"


#device api
@frappe.whitelist(allow_guest=True)
def get_device_list(device_no=None):
	if device_no:
		device_details = frappe.db.sql("""select device_name, device_model, device_no, store, ip_address, port, common_key
			from `tabDevice` WHERE device_no='{0}' """.format(device_no),as_dict=1)
	else:
		device_details = frappe.db.sql("""select device_name, device_model, device_no, store, ip_address, port, common_key
			from `tabDevice`""".format(device_no),as_dict=1)

	return device_details

#end device

#store api
@frappe.whitelist(allow_guest=True)
def get_store_list():
	store_list = frappe.db.sql("select name from `tabStore`", as_dict=1)

	return store_list

@frappe.whitelist(allow_guest=True)
def get_store_details(name=None):
	store_details = frappe.db.sql("""select store_name, store_id, shift_timing1, shift_timing2, sun, mon, tue, wed, thu, fri, sat, store_address
		from `tabStore` WHERE name='{0}' """.format(name),as_dict=1)

	return store_details

#end store api




#emp api

@frappe.whitelist(allow_guest=True)
def get_employee_list():
	employee_list = frappe.db.sql("select employee_name, store, shift_id from `tabEmployee`", as_dict=1)

	return employee_list

@frappe.whitelist(allow_guest=True)
def get_employee_details(employee_name=None):
	employee_details = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
		shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    from `tabEmployee` WHERE employee_name='{0}' """.format(employee_name),as_dict=1)

	return employee_details

#end emp

#shif time api


@frappe.whitelist(allow_guest=True)
def get_shift_time_list():
	shift_time_list = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    from `tabShift Time`""",as_dict=1)

	return shift_time_list

@frappe.whitelist(allow_guest=True)
def get_shift_time_details(shift_name=None):
	shift_time_details = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    from `tabShift Time` WHERE shift_name='{0}' """.format(shift_name),as_dict=1)

	return shift_time_details

#end shift time

#store shift schedule
#date filter most imp
#employee filter
@frappe.whitelist(allow_guest=True)
def get_shift_schedule_list():
	shift_schedule_list = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    from `tabShift Time`""",as_dict=1)

	return shift_schedule_list

@frappe.whitelist(allow_guest=True)
def get_shift_schedule_details(shift_name=None):
	shift_schedule_details = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    from `tabShift Time` WHERE shift_name='{0}'""".format(shift_name),as_dict=1)

	return shift_schedule_details

#end shift schedule

#attendance api
@frappe.whitelist(allow_guest=True)
def get_attendance_list():
	attendance_list = frappe.db.sql("select name from `tabAttendance`", as_dict=1)

	return attendance_list

@frappe.whitelist(allow_guest=True)
def get_attendance_details(employee=None):
	attendance_details = frappe.db.sql("""select employee, employee_name, status, leave_type, attendance_date, company, in_store, in_time, out_time, out_store, amended_from
		from `tabAttendance` WHERE employee='{0}' """.format(employee),as_dict=1)

	return attendance_details

@frappe.whitelist(allow_guest=True)
def create_attendance(employee=None, attendance_date='',in_store='',out_store='',in_time='',out_time='',company=''):

	attendance_doc = frappe.new_doc("Attendance")
	attendance_doc.employee = employee
	attendance_doc.attendance_date = attendance_date
	attendance_doc.in_store = in_store
	attendance_doc.out_store = out_store
	attendance_doc.in_time = in_time
	attendance_doc.out_time = out_time
	attendance_doc.company = company
	attendance_doc.insert(ignore_permissions=True)
	attendance_doc.save(ignore_permissions=True)
	frappe.db.commit()
	return { "message":"New Attendance {0} Is Created".format(employee),
			"status": "success","user_message":"New Attendance {0} Is Created".format(employee)}


#end attendance

#attendance_violation api
@frappe.whitelist(allow_guest=True)
def get_attendance_violation_details(employee=None):
	attendance_violation_details = frappe.db.sql("""select  store, in_date, violation_type, in_time, out_time, out_date, out_store, 
		deduction_days, violation_remark, amended_in_date, amended_in_time, amended_out_time, amended_out_store, amended_out_date,
		working_hours, attendance_status, amended_status, deduction_amount, approver_comment, amended_from
	    from `tabAttendance Violation` WHERE employee='{0}' """.format(employee),as_dict=1)

	return attendance_violation_details

@frappe.whitelist(allow_guest=True)
def get_attendance_violation_list():
	attendance_violation_list = frappe.db.sql("""select  store, in_date, violation_type, in_time, out_time, out_date, out_store, 
		deduction_days, violation_remark, amended_in_date, amended_in_time, amended_out_time, amended_out_store, amended_out_date
	    from `tabAttendance Violation`""",as_dict=1)

	return attendance_violation_list


@frappe.whitelist(allow_guest=True)
def create_attendance_violation(employee=None, attendance_date='',company='',store='',deduction_days='',
	in_date='',violation_type='',in_time='', out_time='',out_date='',out_store='',violation_remark='',
	amended_in_date='',amended_in_time='',amended_out_time='', amended_out_store='',amended_out_date='',working_hours='',attendance_status='',
	amended_status='',deduction_amount='',approver_comment=''):

	attendance_doc = frappe.new_doc("Attendance Violation")
	attendance_doc.employee = employee
	attendance_doc.attendance_date = attendance_date
	attendance_doc.company = company

	attendance_doc.store= store
	attendance_doc.deduction_days = deduction_days
	attendance_doc.in_date = in_date
	attendance_doc.violation_type = violation_type
	attendance_doc.in_time = in_time
	attendance_doc.out_time = out_time
	attendance_doc.out_date = out_date
	attendance_doc.out_store = out_store
	attendance_doc.violation_remark = violation_remark

	attendance_doc.amended_in_date = amended_in_date
	attendance_doc.amended_in_time = amended_in_time
	attendance_doc.amended_out_time  = amended_out_time
	attendance_doc.amended_out_store = amended_out_store
	attendance_doc.amended_out_date = amended_out_date
	attendance_doc.working_hours = working_hours
	attendance_doc.attendance_status = attendance_status
	attendance_doc.amended_status = amended_status
	attendance_doc.deduction_amount = deduction_amount
	attendance_doc.approver_comment = approver_comment

	attendance_doc.insert(ignore_permissions=True)
	attendance_doc.save(ignore_permissions=True)
	frappe.db.commit()
	return { "message":"New Attendance {0} Is Created".format(employee),
			"status": "success","user_message":"New Attendance {0} Is Created".format(employee)}


#end attendance violation