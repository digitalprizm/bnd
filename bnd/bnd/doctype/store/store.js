cur_frm.add_fetch('area', 'multi_unit_manager', 'multi_unit_manager');
frappe.ui.form.on("Store", "validate", function(frm) {
    let start_time = cur_frm.doc.store_open_time;    
    let end_time = cur_frm.doc.store_close_time;
    var start = start_time.split(':');
    var end = end_time.split(':');

    var start_hours = start[0];
    var end_hours = end[0];

    var start_minute = start[1];
    var end_minute = end[1];

    var start_second = start[2];
    var end_second = end[2];

    var total_minute = parseInt(start_minute) + parseInt(end_minute);

    var total_second = parseInt(start_second) + parseInt(end_second);

    total = 0;
    if (start_hours > end_hours){
      var start_hours= 24-start_hours;
      total=parseInt(start_hours)  + parseInt(end_hours);
    }
    else{
      total = end_hours - start_hours;
    }
    if(start_minute>=1){
      if(end_minute > start_minute){
        total_minute = end_minute - start_minute;
      }
      else{
        total_minute = 60  - start_minute ;
      }
      end_minute = (60 - start_minute) + parseInt(end_minute);
      if(end_minute < 60){
        total = total - 1;
      }
      if ( end_minute < 0){
        total_minute = 60 - end_minute;
      }
    }
    if(total_minute >=60){
      total_minute = total_minute - 60;
        }
    if(total_second >= 60){
      total_second = total_second - 60;
      total_minute = total_minute +1;
    }
    
    total=total+":"+total_minute;
    frm.set_value("total_no_of_hours", total);


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


