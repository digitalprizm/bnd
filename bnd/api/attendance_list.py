import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond
import json
from datetime import datetime

@frappe.whitelist()
def load_data():
    vdict = {}
    employee = frappe.db.sql("SELECT name,employee_name,enroll_number FROM `tabEmployee` where enroll_number is not null and status='Active' ;", as_dict=1)
    vdict["emp"] = employee
    return vdict