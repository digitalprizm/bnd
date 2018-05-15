import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond
import json
from datetime import datetime

@frappe.whitelist()
def load_data(process_date):
    vdict = {}
    employee = frappe.db.sql("""SELECT EMP.name,EMP.employee_name,EMP.enroll_number ,(select count(0) from `tabAttendance Violation` as VIO where VIO.employee=EMP.name and VIO.attendance_date < '{0}') as violationcount FROM `tabEmployee` as EMP  where EMP.enroll_number is not null and EMP.status='Active' ;""".format(process_date), as_dict=1)
    process_date=frappe.utils.data.getdate (process_date)
    process_date=frappe.utils.data.formatdate (process_date, 'YYYY-MM-dd')
    vdict["emp"] = employee
    vdict["process_date"]=process_date
    return vdict


   