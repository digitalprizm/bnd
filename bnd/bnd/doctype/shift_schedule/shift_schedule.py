# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _


class ShiftSchedule(Document):
	def validate(self):
		self.validate_linked_data()
		self.validate_duplicate_record()

	def validate_linked_data(self):
		if self.employee:
			self.employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")	
		if self.shift_time:
			self.start_time = frappe.db.get_value("Shift Time", self.shift_time, "start_time")	
			self.end_time = frappe.db.get_value("Shift Time", self.shift_time, "end_time")	

	def validate_duplicate_record(self):
		res = frappe.db.sql("""select name 
			from `tabShift Schedule` where employee = %s 
				and attendance_date = %s
				and name != %s and docstatus = 1""",
			(self.employee, self.attendance_date, self.name))
		if res:
			frappe.throw(_("Shift Schedule for employee {0} is already created").format(self.employee))
