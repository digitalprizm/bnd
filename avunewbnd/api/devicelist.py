
import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond
import json






def load_devices(process_date):
    """Loads Devices list in `__onload`"""
    #Get devices
    datastore = json.loads('[{"device":"hello","date":"2018-04-04"},{"device":"try","date":"2018-04-01"}]')
    frappe.msgprint(str(datastore));
    frappe.msgprint(str(len(datastore)));
    #frappe.msgprint("HII"+process_date);
    vdict = frappe.db.sql("SELECT device_no,device_name,ip_address FROM `tabDevice` ;", as_dict=1)
    #frappe.msgprint(str(vdict[0]['device_name']))
    Today=frappe.utils.data.nowdate()
    for i in range(0,len(vdict)):
    	if datastore[i]['device']==vdict[i]['device_name'] :
    		
    		vdict[i].update({'scanned_date': datastore[i]['date'] })
    		a=frappe.utils.data.date_diff (datastore[i]['date'], process_date );
    		frappe.msgprint("a!=0 a=  "+str(a)+" i= "+str(i));
    		if a>=2:
    			vdict[i].update({'status': "Ready to process" })
    		else:
    			vdict[i].update({'status': "Not ready to process" })
    	else:
    		frappe.msgprint("Something went wrong.");
    		
    		#vdict[i].update({'scanned_date': datastore[i]['date']})
    #frappe.msgprint(str(vdict[i]['status']))
    return vdict

