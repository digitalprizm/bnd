from __future__ import unicode_literals
import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data(filters)
	validate_filters(filters)

	return columns, data

def validate_filters(filters):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))


def get_data(filters):
	query="""Select  name, employee_name, company, user_id, date_of_joining, date_of_birth, gender, 
		shift_type, shift_id, eligible_week_off_days, store, enroll_number, weekly_off_day1, weekly_off_day2
	    from `tabEmployee` """
	
	if filters.get("Store"):
		query += """ where store = '{0}' 
			""".format(filters.get("Store"))
	
	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl

def  get_colums():
	columns = ["Emp Id:Data:100"]+["Full Name:Data:100"]+["Company:Data:100"]+["User Id:Data:140"]\
	+["Date of Joining:Date:120"]+["Date of Birth:Date:120"]+["Gender:Data:100"]+["Shift Type:Data:100"]\
	+["Shift Id:Data:100"]+["Eligible Week Off Days:Data:100"]+["Store:Data:100"]+["Enroll Number:Data:100"]\
	+["Weekly Off Day1:Data:100"]+["Weekly Off Day2:Data:100"]
		
	return columns
	
	

