# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime
now = datetime.datetime.now()
class ShiftScheduleException(Document):
	def validate(self):
		self.validate_duplicate_record()
		self.get_shift_schedule()
		self.validate_attendance_date()

	def get_shift_schedule(self):
		data=frappe.db.sql("""select employee, employee_name, 
			shift_time,attendance_date, store 
			from `tabShift Schedule` 
			where employee='{0}' and attendance_date ='{1}'and docstatus='1' limit 1
		 """.format(self.employee,self.attendance_date), as_dict=1)
		if data:
			self.old_store_location = data[0].store
			self.shift_schedule_old_time = data[0].shift_time
		else :
			frappe.msgprint("Shift schedule is Not found")
	def validate_duplicate_record(self):
		res = frappe.db.sql("""select name from `tabShift Schedule Exception` where employee = %s and attendance_date = %s
			and name != %s and docstatus = 1""",
			(self.employee, self.attendance_date, self.name))
		if res:
			frappe.throw(("Shift schedule exception for employee {0} is already created").format(self.employee))

		
	def validate_attendance_date(self):
		attendance_date = self.attendance_date
		date = now.strftime("%Y-%m-%d")
		if attendance_date<date:
			frappe.throw("Attendance Date Can Not Less Than To Current Date")