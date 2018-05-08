# -*- coding: utf-8 -*-.
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, add_days, date_diff
from frappe import _
from frappe.utils.csvutils import UnicodeWriter
from frappe.model.document import Document
import datetime
class UploadShiftSchedule(Document):
	pass


