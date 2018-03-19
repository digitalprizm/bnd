from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

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



