
# -*- coding: utf-8 -*-
# Copyright (c) 2018, pranali and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from avunewbnd.api.data_list import load_data
import ast


class ShiftScheduleManual(Document):
	def onload(self):
		dlist=load_data()
		#frappe.msgprint("hii")
		self.get("__onload").data_list = dlist








@frappe.whitelist()
def passing_templatedata_to_python(data):
	#frappe.msgprint("function is working")
	d=ast.literal_eval(data)
	action=""
	#frappe.msgprint(str(d))
	
	
	for i in range(0,len(d)):
	#date= frappe.utils.data.formatdate (d[i]["Day"], "yyyy-MM-dd")
		doc = frappe.get_doc({

  "doctype": "Shift Schedule",
     "shift_time": d[i]["Shift"],
     "employee_name":d[i]["Employee"],
     "store": d[i]["Store"],
     "attendance_date" : d[i]["Day"],
     "company": d[i]["Company"],
     "employee" : d[i]["Empid"],
     "naming_series" : "SHT-"
     
	})
		existing_data=frappe.get_all("Shift Schedule",fields=["name","attendance_date","employee_name","shift_time"],filters= {"attendance_date": d[i]["Day"],"employee_name":d[i]["Employee"]})
		if len(existing_data)!=0:
			store= d[i]["Store"]
			shift =d[i]["Shift"]
			emp=d[i]["Employee"]
			attendance_date=d[i]["Day"]
			frappe.db.sql("UPDATE `tabShift Schedule`set store=%s, shift_time=%s where employee_name=%s and attendance_date=%s",(store,shift,emp,attendance_date))
			action= "Updated"
		else:
			doc.insert()
			doc.submit()
			action= "Inserted"

	
	
	frappe.msgprint("Record "+action+" Sucessfully");
	return "Done"
	
	







@frappe.whitelist()
def load_existing_data(from_date,to_date,start_date):
	fdate = frappe.utils.data.format_datetime (from_date, "yyyyMMdd")
	tdate = frappe.utils.data.format_datetime (to_date, "yyyyMMdd")
	sdate = frappe.utils.data.format_datetime (start_date, "yyyyMMdd")
	#frappe.msgprint("fdate  "+fdate+" todate  "+tdate)
	myt_sql="CALL getschedule("+fdate+", "+tdate+", "+sdate+");"
	#frappe.msgprint(str(myt_sql))
	lastweekdetails=frappe.db.sql(myt_sql, as_dict=1)
	#frappe.msgprint(lastweekdetails)
	return lastweekdetails
