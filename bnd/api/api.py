from __future__ import unicode_literals
import frappe, os, json


@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"



@frappe.whitelist(allow_guest=True)
def get_device_list():
	device_list = frappe.db.sql("select name from `tabDevice`", as_dict=1)

	return device_list