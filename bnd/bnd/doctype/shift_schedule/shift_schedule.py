# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
import datetime
from frappe import utils
now = datetime.datetime.now()

class ShiftSchedule(Document):
	def validate(self):
		self.validate_linked_data()
		self.validate_duplicate_record()
		self.validate_shift_type()
		self.shift_schedule()

	def validate_linked_data(self):
		if self.employee:
			self.employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")	
		if self.shift_time:
			self.start_time = frappe.db.get_value("Shift Time", self.shift_time, "start_time")	
			self.end_time = frappe.db.get_value("Shift Time", self.shift_time, "end_time")	


	def validate_shift_type(self):
		shift_type = frappe.db.get_value("Employee", self.employee, "shift_type")	
		if shift_type != "Rotational":
			frappe.throw("Shift Type for Employee {0} should be Rotational".format(self.employee))

	def validate_duplicate_record(self):
		res = frappe.db.sql("""select name 
			from `tabShift Schedule` where employee = %s 
				and attendance_date = %s
				and name != %s and docstatus = 1""",
			(self.employee, self.attendance_date, self.name))
		if res:
			frappe.throw(_("Shift Schedule for employee {0} is already created").format(self.employee))
	def shift_schedule(self):
		attendance_date = self.attendance_date
		date = frappe.utils.nowdate()
		if attendance_date < date:
			frappe.throw("Attendance Date Can Not Less Than To Todays Date")
		