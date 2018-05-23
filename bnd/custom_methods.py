from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, time_diff_in_hours, get_datetime, getdate, today, cint, add_days 
from frappe import _
from frappe.utils import cint, cstr, date_diff, flt, formatdate, getdate, get_link_to_form, \
	comma_or, get_fullname
# from frappe.utils import (flt, getdate, get_first_day, get_last_day, date_diff,
# 	add_months, add_days, formatdate, cint)

@frappe.whitelist()
def salary_slip(doc,method):
	query="""Select sum(deduction_days), sum(deduction_amount)
	from `tabAttendance` where (attendance_date between '{0}' and '{1}') and employee='{2}'""".format(doc.start_date, doc.end_date, doc.employee)
	deduction_data = frappe.db.sql(query,as_list=1,debug=1)
	if deduction_data:
		deduction = deduction_data[0]
		doc.deduction_days = deduction[0]
		doc.deduction_amount = deduction[1]
		if doc.deduction_amount >= 1 or doc.deduction_days >=1 :
			frappe.msgprint('Deduction days:'+ str(doc.deduction_days) )
			frappe.msgprint('Deduction amount:'+ str(doc.deduction_amount) )

	flag = False
	for i in doc.deductions:
		if i.salary_component == "Attendance Violation":
			flag = True
			i.amount = doc.deduction_amount
	if flag:
		pass
	elif doc.deduction_amount >= 1:
		row = doc.append('deductions', {})
		row.salary_component = "Attendance Violation"
		row.amount =doc.deduction_amount

	present="""Select count(*)
	from `tabAttendance` where (status = 'Present' and attendance_date between '{0}' and '{1}') and employee='{2}' """.format(doc.start_date, doc.end_date, doc.employee)
	attendance_present = frappe.db.sql(present,as_list=1,debug=1)
	absent="""Select count(*)
	from `tabAttendance` where (status = 'Absent' and attendance_date between '{0}' and '{1}') and employee='{2}' """.format(doc.start_date, doc.end_date, doc.employee)
	attendance_absent = frappe.db.sql(absent,as_list=1,debug=1)
	present_count=attendance_present[0]
	absent_count=attendance_absent[0]
	doc.total_present_days= str(present_count[0])
	doc.total_absent_days = str(absent_count[0])
	
	# deduction = """Select basic, housing_allow,total_deduction from `tabAttendance`"""	
	# if doc.total_absent_days:
	# 	er  = (basic-housing_allow-total_deduction)*12/360
	# 	print("\nnnnnnnnn",er)
		
	# doc.deduction = str(er[0])
	# gross_pay = frappe.db.sql(""" Select gross_pay from `tabSalary Slip`""",as_list=1)
	gross_pay = doc.gross_pay
	total_deduction = doc.total_deduction
	total_deduction_days = (gross_pay - total_deduction)*12/360
	# doc.deduction = str(total_deduction_days)
	# frappe.msgprint("Total Deduction Days Amount"+ ' : ' +str(total_deduction_days))

	ot_hours = """Select sum(ot_hours)
	from `tabAttendance` where (attendance_date between '{0}' and '{1}') and employee='{2}' """.format(doc.start_date, doc.end_date, doc.employee)
	ot_data = frappe.db.sql(ot_hours,as_list=1,debug=1)
	ot=ot_data[0]
	frappe.msgprint("OT Hours "+str(ot[0]))
	a = 0
	for i in doc.earnings:
		# print("\n",i.amount)
		# frappe.msgprint(str(i.salary_component)+str(i.amount))
		if i.salary_component!="Housing Allow":
			a =a+i.amount
	frappe.msgprint("earnings"+str(a))
	b =0
	for j in doc.deductions:
		b = b+j.amount
	frappe.msgprint("deductions"+str(b))
	total_absent_days = doc.total_absent_days
	frappe.msgprint("total_absent_days"+str(total_absent_days))
# @frappe.whitelist()
# def create_attendance(doc,method):

# 	number_of_days = date_diff(doc.to_date, doc.from_date) + 1
# 	number_of_days = int(number_of_days)
# 	leave_type = doc.leave_type
# 	for i in range(number_of_days) :
# 		attendance_doc = frappe.new_doc("Attendance")
# 		attendance_doc.employee = doc.employee
# 		attendance_doc.attendance_date = doc.from_date
# 		if leave_type == "LWP":
# 	 		attendance_doc.status = "Absent"
# 		else:
# 			attendance_doc.status = "Present"
# 		attendance_doc.insert()
# 		attendance_doc.save()
# 		attendance_doc.submit()

@frappe.whitelist()
def employee_reg_validate(doc,method):
	relieving_date = doc.relieving_date
	resignation_letter_date = doc.resignation_letter_date
	date_of_joining = doc.date_of_joining
	# frappe.msgprint(date_of_joining)
	if resignation_letter_date:
		if resignation_letter_date<=date_of_joining:
			frappe.throw("Date Of Joining Must Be Less Than Resignation Letter Date")
		
	# frappe.msgprint("relieving_date"+relieving_date+" <br>"+"resignation_letter_date"+resignation_letter_date)
	if resignation_letter_date:

		if relieving_date is None or resignation_letter_date is None:
			frappe.throw("Resignation Letter Date And Relieving Date Can Not Be None")
		# elif resignation_letter_date is None:
		# 	frappe.throw("Resignation Letter Date Can Not Be Blank")
		else:
		 if relieving_date<=resignation_letter_date:
			frappe.throw("Relieving Date must be greater than Resignation Letter Date"+'<br>'+"Relieving Date Is"+" : "+str(relieving_date)+" <br>"+"Resignation Letter Date Is"+' : '+str(resignation_letter_date))
		