import json
import requests
import frappe
from frappe import _

@frappe.whitelist()
def get_apidata():
	frappe.msgprint("API is calling... wait for sometime");
	headers=  {'content-type' : 'application/json'}
    url = 'http://192.168.16.194/subwayapi/api/attendance'
    params = {'_IP': "12.3.4.5" , '_Dev': 123, '_key': 34}
    r=requests.post(url, params=params, headers=headers)
    data = json.loads(r.text)
	return data
