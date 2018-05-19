# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from bnd.api.attendance_list import load_data
import json
import requests

class AttendanceProcess(Document):
	def onload(self):
		r=requests.get('http://120.88.36.10:560/subtest/api/Aprocess/LastProcessDate')
		api=json.loads(r.text)
		process_date=api["_date"]
		alist=load_data(process_date)
		self.get("__onload").attendance_list = alist

