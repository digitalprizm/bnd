from __future__ import unicode_literals
import frappe, os, json
from frappe.utils import cstr, now_datetime, cint, flt, get_time


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"


#device api
@frappe.whitelist(allow_guest=True)
def get_device_list(device_no=None):
	if device_no:
		device_details = frappe.db.sql("""select device_name, device_model, device_no, store,store_name, ip_address, port, common_key
			from `tabDevice` WHERE device_no='{0}' """.format(device_no),as_dict=1)
	else:
		device_details = frappe.db.sql("""select device_name, device_model, device_no, store,store_name, ip_address, port, common_key
			from `tabDevice`""".format(device_no),as_dict=1)

	return device_details


#end device

#store api

@frappe.whitelist(allow_guest=True)
def get_store_details_list(store_name=None):
	if store_name:
		store_list = frappe.db.sql("""select store_name, store_id, 
			area,multi_unit_manager,store_open_time, store_close_time, total_no_of_hours,
			od.operating_days,od.shift_timing1,od.shift_timing2,od.shift_timing3 
			store_address
			from `tabStore`, `tabOperational Day` od 
			WHERE store_name='{0}' and od.parent=tabStore.name""".format(store_name),as_dict=1)
	else:
		store_list = frappe.db.sql("""select store_name, store_id, 
			area,multi_unit_manager, store_open_time, store_close_time, total_no_of_hours,
			od.operating_days,od.shift_timing1,od.shift_timing2,od.shift_timing3 ,
			store_address
			from `tabStore`, `tabOperational Day` od 
			where od.parent=tabStore.name""".format(store_name), as_dict=1)

	import itertools 
	category_details = {}
	a_list = store_list
	a_dict = {}
	for i in a_list:
		a_dict[i['store_name']] = []
		#a_dict[i['store_name']].append({"store_id":"store_id","multi_unit_manager":"multi_unit_manager","area":"area","store_name":"store_name"})

	for i in a_list:
		mydict = {"operating_days":i['operating_days'],"shift_timing1":i['shift_timing1'],"shift_timing2":i['shift_timing2'],"shift_timing3":i['shift_timing3']}
		print i
		a_dict[i['store_name']].append(mydict)

	return a_dict

@frappe.whitelist(allow_guest=True)
def get_store_list(store_name=None):
	if store_name:
		store_list = frappe.db.sql("""select store_name, store_id, 
			area,multi_unit_manager, 
			store_address, store_close_time, store_open_time, total_no_of_hours
			from `tabStore` 
			WHERE store_name='{0}' """.format(store_name),as_dict=1)
	else:
		store_list = frappe.db.sql("""select store_name, store_id,area, multi_unit_manager, store_open_time, store_close_time, total_no_of_hours,store_address
			from `tabStore`""".format(store_name), as_dict=1)

	return store_list

#end store api

#emp api

#name pass or enrollment no
@frappe.whitelist(allow_guest=True)
def get_employee_list(id=None,enroll_number=None):

	if id:
		employee_list = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2,
			subscriber_no, gosi_no, nationality, national_id_no, country, iqama_no, iqama_issue_date, iqama_expiry_hijri, iqama_expiry_english,
			driving_license_no, driving_license_issue_date, driving_license_expiry_date, baladiya_card_no, exam_date, training_expiry_date, baladiya_medical_center,muqeem_status, muqeem_status, store,
			passport_number, date_of_issue,
			branch, department, salary_mode, designation, occupation, company_email, notice_number_of_days,
			status, employment_type, holiday_list, scheduled_confirmation_date, final_confirmation_date, contract_end_date, date_of_retirement
			from `tabEmployee` WHERE name='{0}'and where `tabEmployee`.user_id = `tabStore`.multi_unit_manager """.format(id),as_dict=1)
	elif enroll_number:
		employee_list = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2,
			subscriber_no, gosi_no, nationality, national_id_no, country, iqama_no, iqama_issue_date, iqama_expiry_hijri, iqama_expiry_english,
			driving_license_no, driving_license_issue_date, driving_license_expiry_date, baladiya_card_no, exam_date, training_expiry_date, baladiya_medical_center,muqeem_status, muqeem_status, store,
			passport_number, date_of_issue,
			branch, department, salary_mode, designation, occupation, company_email, notice_number_of_days,
			status, employment_type, holiday_list, scheduled_confirmation_date, final_confirmation_date, contract_end_date, date_of_retirement
	    	from `tabEmployee` WHERE enroll_number='{0}'""".format(enroll_number),as_dict=1)
	else:
		employee_list = frappe.db.sql("""select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
			shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2,
			subscriber_no, gosi_no, nationality, national_id_no, country, iqama_no, iqama_issue_date, iqama_expiry_hijri, iqama_expiry_english,
			driving_license_no, driving_license_issue_date, driving_license_expiry_date, baladiya_card_no, exam_date, training_expiry_date, baladiya_medical_center,muqeem_status, muqeem_status, store,
			passport_number, date_of_issue,
			branch, department, salary_mode, designation, occupation, company_email, notice_number_of_days,
			status, employment_type, holiday_list, scheduled_confirmation_date, 
final_confirmation_date, contract_end_date, date_of_retirement
	    	from `tabEmployee` """,as_dict=1)

	return employee_list

#end emp

#shif time api

@frappe.whitelist(allow_guest=True)
def get_shift_time_list(shift_name=None):
	if shift_name:
		shift_time_list = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    	from `tabShift Time` WHERE shift_name='{0}' """.format(shift_name),as_dict=1)
	else:
		shift_time_list = frappe.db.sql("""select  shift_name, start_time, end_time, no_of_hours, end_time_on_next_day
	    	from `tabShift Time`""".format(shift_name),as_dict=1)

	return shift_time_list
#end shift time

#store shift schedule
#date filter most imp
#employee filter
@frappe.whitelist(allow_guest=True)
def get_shift_schedule_list(attendance_date=None,store=None,employee=None):
	if attendance_date and store:
		shift_schedule_details = frappe.db.sql("""select  employee_name, 
			employee, 
			case when (1=1)
				then (select enroll_number from `tabEmployee` 
				where `tabEmployee`.name = `tabShift Schedule`.employee)
				else 0
				end as enroll_number,
			leave_type, attendance_date, company, store, shift_time, start_time, end_time, amended_from\
	    	FROM `tabShift Schedule` 
	    	WHERE attendance_date='{0}' and store='{1}'""".format(attendance_date,store),as_dict=1)
	elif attendance_date and employee:
		shift_schedule_details = frappe.db.sql("""select  employee_name, 
			employee, 
			case when (1=1)
				then (select enroll_number from `tabEmployee` 
				where `tabEmployee`.name = `tabShift Schedule`.employee)
				else 0
				end as enroll_number,
			leave_type, attendance_date, company, store, shift_time, start_time, end_time, amended_from\
	    	FROM `tabShift Schedule` 
	    	WHERE attendance_date='{0}' and employee='{1}'""".format(attendance_date,employee),as_dict=1)
	else:
		shift_schedule_details = frappe.db.sql("""select  employee_name, employee, 
			case when (1=1)
				then (select enroll_number from `tabEmployee` 
				where `tabEmployee`.name = `tabShift Schedule`.employee)
				else 0
				end as enroll_number,
			leave_type, attendance_date, company, store, shift_time, start_time, end_time, amended_from\
	    	FROM `tabShift Schedule`""".format(attendance_date),as_dict=1)

	return shift_schedule_details

@frappe.whitelist(allow_guest=True)

#end shift schedule
#shift schedule exception list
@frappe.whitelist(allow_guest=True)
def get_shift_schedule_exception_list(attendance_date=None):
	if attendance_date:
		shift_schedule_exception_details = frappe.db.sql("""select  employee_name, 
			employee, 
			case when (1=1)
				then (select enroll_number from `tabEmployee` 
				where `tabEmployee`.name = `tabShift Schedule Exception`.employee)
				else 0
				end as enroll_number,
			attendance_date, company, amended_from, shift_schedule_old_time, 
			old_store_location, shift_schedule, shift_schedule__new_time, 
			store_location, store_location_out, new_store_location, reason, comment\
	    	from `tabShift Schedule Exception` WHERE attendance_date='{0}'""".format(attendance_date),as_dict=1)
	else:
		shift_schedule_exception_details = frappe.db.sql("""select  employee_name, 
			employee, 
			case when (1=1)
				then (select enroll_number from `tabEmployee` 
				where `tabEmployee`.name = `tabShift Schedule Exception`.employee)
				else 0
				end as enroll_number,
			attendance_date, company, amended_from, shift_schedule_old_time,
			old_store_location, shift_schedule, shift_schedule__new_time, 
			store_location, store_location_out, new_store_location, reason, comment\
	    	from `tabShift Schedule Exception`""".format(attendance_date),as_dict=1)

	return shift_schedule_exception_details
#end shift schedule exception
#get hr parameter
@frappe.whitelist(allow_guest=True)
def get_hr_parameter():
	data = frappe.db.sql("""select field, value
		from tabSingles
		where doctype ='HR Parameter'
		and (field = 'early_tolerance_limit'
			OR field ='leaving_tolerance_limit'
			OR field ='ot_minimum_time')""", as_dict=1)

	hr_parameter = {}
	for item in data:
		hr_parameter.update({item['field']: item['value']})

	return {"HR Parameter":hr_parameter}
#attendance api

@frappe.whitelist(allow_guest=True)
def get_attendance_list(attendance_date=None):
	if attendance_date:
		attendance_list = frappe.db.sql("""select employee, employee_name, status, leave_type, attendance_date,
		new_in_time,new_out_time, company, in_store, in_time, out_time, out_store, amended_from,
		status1, status2,ot_hours, schedule_time, schedule_store,schedule_status, total_working_hours 
			from `tabAttendance` WHERE attendance_date='{0}' """.format(attendance_date),as_dict=1)
	else:
		attendance_list = frappe.db.sql("""select employee, employee_name, status, new_in_time, new_out_time, leave_type, attendance_date, company, in_store, in_time, out_time, out_store, amended_from,
			status1, status2,ot_hours, schedule_time, schedule_store,schedule_status, total_working_hours
			from `tabAttendance`""".format(attendance_date),as_dict=1)

	return attendance_list

@frappe.whitelist(allow_guest=True)
def create_attendance(employee=None,employee_name='', attendance_date='',in_store='',out_store='',in_time='00:00',out_time='00:00',company='',new_in_time='00:00',new_out_time='00:00',
						status1='',status2='',total_working_hours='',ot_hours='',schedule_store='',schedule_status='',schedule_time=''):

	attendance_doc = frappe.new_doc("Attendance")
	attendance_doc.employee = employee
	attendance_doc.employee_name = employee_name
	attendance_doc.attendance_date = attendance_date
	attendance_doc.in_store = in_store
	attendance_doc.out_store = out_store
	attendance_doc.in_time = get_time(in_time)
	attendance_doc.out_time = get_time(out_time)
	attendance_doc.company = company
	attendance_doc.new_in_time = get_time(new_in_time)
	attendance_doc.new_out_time = get_time(new_out_time )
	attendance_doc.status1 = status1
	attendance_doc.status2 = status2
	attendance_doc.total_working_hours = total_working_hours
	attendance_doc.ot_hours = ot_hours
	attendance_doc.schedule_store = schedule_store
	attendance_doc.schedule_status = schedule_status
	attendance_doc.schedule_time = schedule_time

	try:
		attendance_doc.insert(ignore_permissions=True)
		attendance_doc.save(ignore_permissions=True)
		attendance_doc.submit()
		frappe.db.commit()
		return { "message":"New Attendance {0} Is Created".format(employee),
			"status": "success","user_message":"New Attendance {0} Is Created".format(employee)}
	except Exception as e:
		error = True
		return { "message":"New Attendance  Is Not Created",
			"status": "failed",
			"user_message":"New Attendance Is Not Created",
			"error": e }


# end attendance

# startattendance_violation api

@frappe.whitelist(allow_guest=True)
def get_attendance_violation_list(employee=None):
	if employee:
		attendance_violation_list = frappe.db.sql("""select  employee,employee_name,store, in_date, violation_type, in_time, out_time, out_date, out_store, 
			deduction_days, violation_remark, amended_in_date, amended_in_time, amended_out_time, amended_out_store, amended_out_date,
			working_hours, status, amended_status, deduction_amount, approver_comment, amended_from,
			status1, status2, ot_hours, schedule_time, schedule_store, schedule_status, total_working_hours,
			new_in_time, new_out_time
	    	from `tabAttendance Violation` WHERE employee='{0}' """.format(employee),as_dict=1)
	else:
		attendance_violation_list = frappe.db.sql("""select  employee,employee_name,store, in_date, violation_type, in_time, out_time, out_date, out_store, 
			deduction_days, violation_remark, amended_in_date, amended_in_time, amended_out_time, amended_out_store, amended_out_date,
			working_hours, status, amended_status, deduction_amount, approver_comment, amended_from,
			status1, status2, ot_hours, schedule_time, schedule_store, schedule_status, total_working_hours,
			new_in_time, new_out_time
	    	from `tabAttendance Violation`""".format(employee),as_dict=1)

	return attendance_violation_list
# end attendance violation

# start leave application

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
# end leave Application

@frappe.whitelist(allow_guest=True)
def create_attendance_violation(employee=None,employee_name='', attendance_date='',company='',store='',deduction_days='',
	in_date='',violation_type='',in_time='00:00', out_time='00:00',out_date='',out_store='',violation_remark='',
	amended_in_date='',amended_in_time='00:00',amended_out_time='00:00', amended_out_store='',amended_out_date='',attendance_status='',amended_in_store='',amended_status1='',amended_status2='',
	amended_status='',deduction_amount='',approver_comment='',status1='',status2='',ot_hours='',schedule_store='',schedule_status='',schedule_time=''):
# 
	attendance_violation_doc = frappe.new_doc("Attendance Violation")
	attendance_violation_doc.employee = employee
	attendance_violation_doc.employee_name = employee_name
	attendance_violation_doc.attendance_date = attendance_date
	attendance_violation_doc.company = company

	attendance_violation_doc.store= store
	attendance_violation_doc.deduction_days = deduction_days
	attendance_violation_doc.in_date = in_date
	attendance_violation_doc.violation_type = violation_type
	attendance_violation_doc.in_time = get_time(in_time)
	attendance_violation_doc.out_time = get_time(out_time)
	attendance_violation_doc.out_date = out_date
	attendance_violation_doc.out_store = out_store
	attendance_violation_doc.violation_remark = violation_remark

	attendance_violation_doc.amended_in_date = amended_in_date
	attendance_violation_doc.amended_in_time = get_time(amended_in_time)
	attendance_violation_doc.amended_out_time  = get_time(amended_out_time)
	attendance_violation_doc.amended_out_store = amended_out_store
	attendance_violation_doc.amended_out_date = amended_out_date
	attendance_violation_doc.attendance_status = attendance_status
	attendance_violation_doc.amended_status = amended_status
	attendance_violation_doc.deduction_amount = deduction_amount
	attendance_violation_doc.approver_comment = approver_comment
	attendance_violation_doc.amended_in_store = amended_in_store
	attendance_violation_doc.amended_status1 = amended_status1
	attendance_violation_doc.amended_status2 = amended_status2


	attendance_violation_doc.status1 = status1
	attendance_violation_doc.status2 = status2
	attendance_violation_doc.ot_hours = ot_hours
	attendance_violation_doc.schedule_store = schedule_store
	attendance_violation_doc.schedule_status = schedule_status
	attendance_violation_doc.schedule_time = schedule_time

	try:
		attendance_violation_doc.insert(ignore_permissions=True)
		attendance_violation_doc.save(ignore_permissions=True)
		frappe.db.commit()
		# frappe.msgprint( " Employee attedance created successfull")
		return { "message":"New Attendance Violation {0} Is Created".format(employee),
				"status": "success","user_message":"New Attendance {0} Is Created".format(employee)}

	except Exception as e:
		error = True
		return { "message":"New Attendance Violation Is Not Created",
				"status": "failed",
				"user_message":"New Attendance Is Not Created",
				"error": e }

#end attendance violation


