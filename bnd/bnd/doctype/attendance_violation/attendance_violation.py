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
			frappe.throw(_("Only Attendance violation with status 'Approved' and 'Rejected' can be submitted"))

		self.create_attendance()

	def create_attendance(self):
		attendance_doc = frappe.new_doc("Attendance")
		if self.status == "Approved":
			attendance_doc.status = "Present"
		elif self.status == "Rejected":
			attendance_doc.status = "Absent"
		attendance_doc.employee = self.employee
		attendance_doc.employee_name = self.employee_name
		attendance_doc.attendance_date = self.attendance_date
		attendance_doc.company = self.company
		attendance_doc.attendance_violation = self.name
		attendance_doc.insert()
		attendance_doc.save()
		attendance_doc.submit()
		self.attendance = attendance_doc.name 

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
