# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class AttendanceViolation(Document):
	def validate(self):
		self.validate_duplicate_record()
		
	def on_submit(self):
		if self.status == "Open":
			frappe.throw(_("Only Attendance violation with status 'Approved' can be submitted"))

		self.create_attendance()

	def create_attendance(self):
		attendance_doc = frappe.new_doc("Attendance")
		if self.is_absent == 1 and self.status =="Approved":
			attendance_doc.status = "Absent"
		elif self.status == "Approved" :
			attendance_doc.status = "Present"
		else:
			print("Please check status")
		# else:
		# 	attendance_doc.status = "On leave"

		attendance_doc.employee = self.employee
		attendance_doc.employee_name = self.employee_name
		attendance_doc.attendance_date = self.attendance_date
		attendance_doc.company = self.company
		attendance_doc.attendance_violation = self.name
		attendance_doc.in_time = self.in_time
		attendance_doc.out_time = self.out_time
		attendance_doc.new_in_time = self.amended_in_time
		attendance_doc.new_out_time = self.amended_out_time
		attendance_doc.in_store = self.amended_in_store
		attendance_doc.out_store = self.amended_out_store
		attendance_doc.total_working_hours = self.total_working_hours
		attendance_doc.status1 = self.amended_status1
		attendance_doc.status2 = self.amended_status2
		attendance_doc.ot_hours = self.ot_hours
		attendance_doc.schedule_time = self.schedule_time
		attendance_doc.schedule_store = self.schedule_store
		attendance_doc.deduction_days = self.deduction_days
		attendance_doc.deduction_amount = self.deduction_amount
		attendance_doc.insert()
		attendance_doc.save()
		attendance_doc.submit()
		self.attendance = attendance_doc.name 

		frappe.msgprint("""<html> <body>New attendance <a href="#Form/Attendance/{0}">{0}</a> is created</body>
		</html>""".format(attendance_doc.name))
		
		frappe.msgprint("New Attendance {0} is created".format(attendance_doc.name))

	def on_cancel(self):
		pass

	def validate_duplicate_record(self):
		res = frappe.db.sql("""select name 
			from `tabAttendance Violation` where employee = %s 
				and attendance_date = %s
				and name != %s and docstatus = 1""",
			(self.employee, self.attendance_date, self.name))
		if res:
			frappe.throw(_("Attendance Violation for employee {0} is already created").format(self.employee))
