cur_frm.add_fetch('area', 'multi_unit_manager', 'multi_unit_manager');
frappe.ui.form.on("Store", "validate", function(frm) {
       
   	size=cur_frm.doc.operational_day.length;
   	console.log(size);
   	/*cur_frm.doc.operational_day[0].shift_timing1*/
   	for(i=0;i<size;i++){
   		if(cur_frm.doc.operational_day[i].shift_timing1 == cur_frm.doc.operational_day[i].shift_timing2 ){
   			frappe.msgprint("Shift Time Duplicate, Please select another Shift Time ");
   		}
   		if(cur_frm.doc.operational_day[i].shift_timing2 == cur_frm.doc.operational_day[i].shift_timing3 ){
   			frappe.msgprint("Shift Time Duplicate, Please select another Shift Time ");
   		}
   		if(cur_frm.doc.operational_day[i].shift_timing1 == cur_frm.doc.operational_day[i].shift_timing3 ){
   			frappe.msgprint("Shift Time Duplicate, Please select another Shift Time ");
   		}
   	}
    
});
