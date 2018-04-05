# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from avunewbnd.api.devicelist import load_devices

class DeviceProcess(Document):
	def onload(self):
		device_list = load_devices(self.process_date)
		self.get("__onload").device_list = load_devicelist(self.process_date)
		#frappe.msgprint(self)

		
@frappe.whitelist()
def load_devicelist(process_date):
	dlist = load_devices(process_date)
	#frappe.msgprint(self)
	#self.get("__onload").device_list = dlist
	return dlist
		
		
		
			

	# def fetch_device_info(self, devicedocname):

	# 	frappe.msgprint(devicedocname)

	# 	dr = frappe.get_doc("Device", devicedocname)

	# 	return dr
