# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ShiftScheduleException(Document):
	def validate(self):
		self.get_shift_schedule()

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
			frappe.throw("Shift schedule is Not found")
