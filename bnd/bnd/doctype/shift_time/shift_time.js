// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt
frappe.ui.form.on("Shift Time", "validate", function(frm, cdt, cdn) {		 
    let start_time = cur_frm.doc.start_time;    
    let end_time = cur_frm.doc.end_time;
    var m = start_time.split(':');
    var n = end_time.split(':');

    var start_hours = m[0];
    var start_minute = m[1];
    var start_second = m[2];
    var end_hours = n[0];
    var end_minute = n[1];
    var end_second = n[2];
    var total_minute = parseInt(start_minute) + parseInt(end_minute);

    var total_second = parseInt(start_second) + parseInt(end_second);

    total = end_hours - start_hours;
    if (end_hours < start_hours){
      var add_start=24-start_hours;
      var add_end=end_hours;
      total=parseInt(add_start)  + parseInt(add_end);
    }

    if(total_minute >=60){
      total_minute = total_minute - 60;
      /*total = total + 1;*/
    }
    /* new calculation*/
    if(start_minute>=1){
      end_minute = end_minute - start_minute;
      if (end_minute <0){
        total = total -1;
      }
    }
    /* calculation end here*/
    if(total_second >= 60){
      total_second = total_second - 60;
      total_minute = total_minute +1;
    }
    
    total=total+"Hr, "+total_minute+" Min";
    frm.set_value("no_of_hours", total);
})



