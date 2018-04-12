cur_frm.add_fetch('area', 'multi_unit_manager', 'multi_unit_manager');
frappe.ui.form.on("Store", "validate", function(frm) {
   	size=cur_frm.doc.operational_day.length;
   	for(i=0;i<size;i++){
         if( cur_frm.doc.operational_day[i].shift_timing1 ){
      		if(cur_frm.doc.operational_day[i].shift_timing1 == cur_frm.doc.operational_day[i].shift_timing2 ){
      			frappe.throw("Shift Time Duplicate, Please select another Shift Time ");
      		}
         } 
         if( cur_frm.doc.operational_day[i].shift_timing2) {
      		if(cur_frm.doc.operational_day[i].shift_timing2 == cur_frm.doc.operational_day[i].shift_timing3 ){
      			frappe.throw("Shift Time Duplicate, Please select another Shift Time ");
      		}
         }
         if( cur_frm.doc.operational_day[i].shift_timing3){
      		if(cur_frm.doc.operational_day[i].shift_timing1 == cur_frm.doc.operational_day[i].shift_timing3 ){
      			frappe.throw("Shift Time Duplicate, Please select another Shift Time ");
      		}
         }
         for(j=i+1;j<size;j++){
            if(cur_frm.doc.operational_day[i].operating_days == cur_frm.doc.operational_day[j].operating_days){
               frappe.throw("Duplicate Day - "+cur_frm.doc.operational_day[i].operating_days);
            }
         }
   	}
});


