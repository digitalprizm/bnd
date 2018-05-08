# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
import requests

class AttendanceProcess(Document):
	pass


@frappe.whitelist()
def calling_attendance_api():
	r = requests.get('http://192.168.16.194/subwayapi/api/AProcess?_date=20180312')
	api=json.loads(r.text)
	return api

	
