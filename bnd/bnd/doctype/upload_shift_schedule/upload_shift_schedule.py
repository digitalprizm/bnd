# -*- coding: utf-8 -*-.
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import cstr, add_days, date_diff
from frappe import _
from frappe.utils.csvutils import UnicodeWriter
from frappe.model.document import Document
import datetime
class UploadShiftSchedule(Document):
	pass

@frappe.whitelist()
def get_template():
	if not frappe.has_permission("Shift Schedule", "create"):
		raise frappe.PermissionError

	args = frappe.local.form_dict
	print("adsasd args",args)
	w = UnicodeWriter()
	w = add_header(w, args)

	w = add_data(w, args)

	# write out response as a type csv
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Shift Schedule"

@frappe.whitelist()
def get_template_with_data():
	args = frappe.local.form_dict
	print("adsasd args",args)
	
	w = UnicodeWriter()
	w = add_header_get_data(w, args)

	w = add_data(w, args)

	# write out response as a type csv
	frappe.response['result'] = cstr(w.getvalue())
	frappe.response['type'] = 'csv'
	frappe.response['doctype'] = "Shift Schedule"

def get_dates(args):
	"""get list of dates in between from date and to date"""
	no_of_days = date_diff(add_days(args["to_date"], 1), args["from_date"])
	dates = [add_days(args["from_date"], i) for i in range(0, no_of_days)]
	return dates

def add_header(w, args):
	dates = get_dates(args)
	print(dates)
	w.writerow(["Notes:"])
	w.writerow(["Please do not change the template headings"])
	
	date_range = ["","","","-"]
	for i in dates:
		date_range.append(i)
	# date_range.append(dates)
	w.writerow(["ID", "Employee", "Name", "Store", "Day 1","Day 2", "Day 3",
		  "Day 4", "Day 5", "Day 6", "Day 7"])
	w.writerow(date_range)
	return w
def add_header_get_data(w, args):
	dates = get_dates(args)
	print(dates)
	w.writerow(["Notes:"])
	w.writerow(["Please do not change the template headings"])
	
	date_range = ["","","","-"]
	for i in dates:
		date_range.append(i)
	# date_range.append(dates)
	w.writerow(["ID", "Employee", "Name", "Store", "Day 1","Day 2", "Day 3",
		  "Day 4", "Day 5", "Day 6", "Day 7"])
	w.writerow(date_range)
	start_date = date_range[4]
	end_date = date_range[10]
	# get data from shift schedule
	data=frappe.db.sql("""select employee, employee_name,store 
			from `tabShift Schedule` 
			where (attendance_date between '{0}' 
			and '{1}') group by employee""".format(start_date,end_date), as_dict=1)
	
	for i in range(len(data)):
		w.writerow(["",data[i].employee,data[i].employee_name,data[i].store ])
		
	return w
def add_data(w, args):
	
	return w

def get_active_customers():
	customers = frappe.db.sql("""select name
		from `tabCustomer` where docstatus < 2 """, as_dict=1)
	return customers

def get_existing_attendance_records(args):
	schedule = frappe.db.sql("""select name, attendance_date, employee, 
		store, shift_start, end_time
		from `tabShift Schedule` where docstatus < 2""", as_dict=1)

	existing_attendance = {}
	for att in schedule:
		existing_attendance[tuple([att.date, att.customer_ref])] = att

	return existing_attendance

def get_naming_series():
	series = frappe.get_meta("Shift Schedule").get_field("naming_series").options.strip().split("\n")
	if not series:
		frappe.throw(_("Please setup numbering series for Attendance via Setup > Numbering Series"))
	return series[0]


@frappe.whitelist()
def upload():
	if not frappe.has_permission("Shift Schedule", "create"):
		raise frappe.PermissionError

	print("in upload\n\n")
	from frappe.utils.csvutils import read_csv_content_from_uploaded_file
	from frappe.modules import scrub

	rows = read_csv_content_from_uploaded_file()
	rows = filter(lambda x: x and any(x), rows)
	if not rows:
		msg = [_("Please select a csv file")]
		return {"messages": msg, "error": msg}


	columns = []
	# columns = [scrub(f) for f in rows[1]]
	columns.append("name")
	# columns[1] = "date"
	ret = []
	error = False

	from frappe.utils.csvutils import check_record, import_doc

	for i, row in enumerate(rows[4:]):
		print("in for loop\n\n")
		print("row[1]",row[1])
		if not row: continue
		row_idx = i + 3
		d = frappe._dict(zip(columns, row))
		d["doctype"] = "Shift Schedule"
		d["employee"] = row[1]
		d["store"] = row[3]
		# d["attendance_date"] = rows[3][4]

		print("row\n")
		print(row)
		new_date_list = []
		new_shift_time_list = []
		print("new logic\n")
		for i in rows[3]:
			new_date_list.append(i)
		new_date_list=new_date_list[4:]


		new_shift_time_list=row[4:]
		print("\n new new_date_list",new_date_list)
		print("\n new new_shift_time_list",new_shift_time_list)
		print(len(new_shift_time_list),"new_shift_time_list\n")
		# print(row[1])
		# length_of_dates=len(new_shift_time_list)
		length_of_dates=8

		for i in range(length_of_dates-1):
			print("\n",i)
			print(new_shift_time_list[i])
			print(new_date_list[i])
			d["attendance_date"] = new_date_list[i]
			d["shift_time"] = new_shift_time_list[i]			

			import datetime
			# new_date = datetime.datetime.strptime(row[11],'%d-%b-%y').strftime('%d-%m-%Y')
			# d["date"] = new_date

			if d.name:
				d["docstatus"] = frappe.db.get_value("Shift Schedule", d.name, "docstatus")

			try:
				check_record(d)
				ret.append(import_doc(d, "Shift Schedule", 1, row_idx, submit=True))
			except Exception, e:
				error = True
				ret.append('Error for row (#%d) %s : %s' % (row_idx,
					len(row)>1 and row[1] or "", cstr(e)))
				frappe.errprint(frappe.get_traceback())

	if error:
		frappe.db.rollback()
	else:
		frappe.db.commit()
	return {"messages": ret, "error": error}