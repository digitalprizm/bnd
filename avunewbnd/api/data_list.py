
import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond
import json
from datetime import datetime






def load_data():
    """Loads Devices list in `__onload`"""
    #Get devices
    vdict = {}
    employee = frappe.db.sql("SELECT name,employee_name,company FROM `tabEmployee` ;", as_dict=1)
    storelist = frappe.db.sql("SELECT name FROM `tabStore` ;", as_list=1)
    shiftlist = frappe.db.sql("SELECT shift_name FROM `tabShift Time` ;", as_list=1)
    # frappe.throw(lastweekdetails)
    # if lastweekdetails:
    #     for i in range(0,len(lastweekdetails)):
    #         a = lastweekdetails[i]["attendance_date"]
    #         b = str(a)
    #         lastweekdetails[i]["attendance_date"]=b
        # frappe.throw(str(lastweekdetails)

        
    #frappe.msgprint(str(employee[0]["employee_name"]));
    #frappe.msgprint(str(len(employee)));
    #{'emp': [['test'], ['Pranali'], ['suvarna'], ['suresh']], 'store': [['andheri'], ['dadar'], ['ghatkopar']], 'shift': [['Morning'], ['night']]}
    vdict["emp"] = employee
    vdict["store"] = storelist
    vdict["shift"] = shiftlist
    #frappe.msgprint(str(len(vdict["emp"])))
    #frappe.msgprint(str(vdict["emp"][0]["employee_name"]));
    return vdict



