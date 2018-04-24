# Copyright (c) 2013, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

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
	query="""Select  employee, salutation,employee_name, full_name_arabic, user_id, date_of_joining, date_of_birth, branch, department, designation, gender, status, holiday_list, scheduled_confirmation_date, final_confirmation_date, contract_end_date, date_of_retirement, company, employment_type,
	enroll_number, shift_type, eligible_week_off_days, store, weekly_off_day1, weekly_off_day2 from `tabEmployee` """
	
	
	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl

def  get_colums():
	columns = ["Id:Data:100"]+["Salutation:Data:100"]+["Full Name:Data:100"]+["Full Name Arabic:Data:100"]+["User ID:Data:100"]+["Date of Joining:Date:120"]+["Date of Birth:Date:120"]+["Branch:Data:140"]\
	+["Department:Data:100"]+["Designation:Data:120"]+["Gender:Data:100"]+["Status:Data:100"]+["Holiday List:Data:100"]\
	+["Offer Date:Date:100"]+["Confirmation Date:Date:100"]+["Contract End Date:Date:100"]+["Date Of Retirement:Date:100"]\
	+["Company:Data:100"]+["Employee Type:Data:100"]+["Enroll Number:Data:100"]\
	+["Shift Type:Data:100"]+["Eligible Week Off Days:Data:100"]+["Store:Data:100"]\
	+["Weekly Off Day1:Data:100"]+["Weekly Off Day2:Data:100"]
	return columns
