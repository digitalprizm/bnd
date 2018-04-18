// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt
frappe.ui.form.on("Shift Time", "validate", function(frm, cdt, cdn) {		 
    let start_time = cur_frm.doc.start_time;    
    let end_time = cur_frm.doc.end_time;
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
      console.log("basic total ",total);
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
    minute_length = total_minute.toString().length;
    total_length = total.toString().length;;
    if(minute_length==1){
      total_minute = "0"+total_minute;
    }
    if(total_length==1){

      total = "0" + total;
    }
    total=total+":"+total_minute;
    frm.set_value("no_of_hours", total);
})
