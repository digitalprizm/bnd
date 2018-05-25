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
		#self.get_shift_schedule()
		self.validate_attendance_date()
		self.test()

	def get_shift_schedule(self):
		data=frappe.db.sql("""select employee, employee_name, 
			shift_time,attendance_date, store 
			from `tabShift Schedule` 
			where employee='{0}' and attendance_date ='{1}'and docstatus='1' limit 1
		 """.format(self.employee,self.attendance_date), as_dict=1)
		
		data1=frappe.db.sql("""select break_time,ot_hrs 
			from `tabShift Time`""", as_dict=1)
		if data1:
			self.break_time = data1[0].break_time
			self.ot_hrs = data1[1].ot_hrs
			a = self.ot_hrs
			b = self.break_time
			# frappe.msgprint("break_time"+str(b)+"<br>"+"ot_hrs"+str(a))
		
		if data:
			self.old_store_location = data[0].store
			self.shift_schedule_old_time = data[0].shift_time
			self.store_location = data[0].store
			self.shift_schedule__new_time = data[0].shift_time
			
			time = self.shift_schedule__new_time
			self.new_shift_start_time = time.split('-')[0]
			self.new_shift_end_time = time.split('-')[1]
			# if self.shift_schedule__new_time!=time:
			# 	self.new_shift_start_time = time.split('-')[0]
			# 	self.new_shift_end_time = time.split('-')[1]
			# self.new_shift_end_time= (time.split('-')[0])
			# a = self.new_shift_start_time
			# self.new_shift_end_time= (a.split('-')[0])
			# frappe.msgprint(a)
			# self.new_shift_end_time = time[7:].replace("-", ' ')
			# frappe.msgprint("New Shift Start Time"+str(time[0:7]).replace("-", ' ')+"<br>"+"New Shift End Time"+str(time[7:]).replace("-", ' '))
		else :
			frappe.msgprint("Shift schedule is Not found")
	def test(self):	
		data=frappe.db.sql("""select employee, employee_name, 
			shift_time,attendance_date, store 
			from `tabShift Schedule` 
			where employee='{0}' and attendance_date ='{1}'and docstatus='1' limit 1
		 """.format(self.employee,self.attendance_date), as_dict=1)
		time = self.shift_schedule__new_time
		if self.shift_schedule__new_time==time:
				self.new_shift_start_time = time.split('-')[0]
				self.new_shift_end_time = time.split('-')[1]
				# frappe.msgprint("not same")
		

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