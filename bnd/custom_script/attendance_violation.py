from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

@frappe.whitelist()
def cancel_attedance_violation(self):
		frappe.msgprint("test")
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
	frappe.msgprint("test")
	frappe.msgprint("test")