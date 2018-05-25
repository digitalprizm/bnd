# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LeaveApplicationTool(Document):
	def validate(self):
		self.html_datatable = "hiiii"
		self.testt = "kk"
	def get_details(self):
		frappe.msgprint("hi from python")