# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bnd"
app_title = "BnD"
app_publisher = "Digitalprizm"
app_description = "manages attendance "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "contact@digitalprizm.net"
app_license = "MIT"

fixtures = ['Custom Field', 'Property Setter',"Print Format",'Report']
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/bnd/bnd.css"
# app_include_js = "/assets/bnd/js/bnd.js"
app_include_js = "/assets/js/bnd.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/bnd/css/bnd.css"
# web_include_js = "/assets/bnd/js/bnd.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}
doctype_js = {
    "Employee":["custom_script/employee.js"],
    "Attendance" : ["custom_script/attendance.js"],
    "Salary Slip" : ["custom_script/salary_slip.js"]
}
# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doc_events = {
	"Salary Slip": {
		"validate": "bnd.custom_methods.salary_slip",
			},
	# "Leave Application": {
	# 	"validate": "bnd.custom_methods.create_attendance",
	# 		},
	"Employee": {
		"validate": "bnd.custom_methods.employee_reg_validate",
			}
}
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bnd.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bnd.install.before_install"
# after_install = "bnd.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bnd.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bnd.tasks.all"
# 	],
# 	"daily": [
# 		"bnd.tasks.daily"
# 	],
# 	"hourly": [
# 		"bnd.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bnd.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bnd.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bnd.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bnd.event.get_events"
# }

