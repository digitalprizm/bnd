# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ShiftSchedule(Document):
	def validate(self):
		self.validate_linked_data()
	def validate_linked_data(self):
		frappe.msgprint(self.employee)
		if self.employee:
			self.employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")	
		if self.shift_time:
			self.start_time = frappe.db.get_value("Shift Time", self.shift_time, "start_time")	
			self.end_time = frappe.db.get_value("Shift Time", self.shift_time, "end_time")	
