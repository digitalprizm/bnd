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
		alist=load_data()
		#frappe.msgprint("hii")
		self.get("__onload").attendance_list = alist


@frappe.whitelist()
def calling_attendance_api():
	r = requests.get('http://192.168.16.194/subwayapi/api/AProcess?_date=20180312')
	api=r.text
	return api

	
