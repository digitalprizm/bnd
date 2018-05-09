import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond
import json
from datetime import datetime


def load_data():
    vdict = {}
    employee = frappe.db.sql("SELECT name,employee_name,enroll_number FROM `tabEmployee` ;", as_dict=1)
    vdict["emp"] = employee
    return vdict