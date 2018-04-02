// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt
frappe.ui.form.on("Shift Time", "validate", function(frm, cdt, cdn) {		
    console.log("hello");  
    let start_time = cur_frm.doc.start_time;    
    console.log(start_time);
    let end_time = cur_frm.doc.end_time;    
    console.log(end_time);
    var m = start_time.split(':');
    var n = end_time.split(':');

    var start_hours = m[0];
    var start_minute = m[1];
    var start_second = m[2];
    var end_hours = n[0];
    var end_minute = n[1];
    var end_second = n[2];
    var total_minute = parseInt(start_minute) + parseInt(end_minute);
    console.log(total_minute);

    var total_second = parseInt(start_second) + parseInt(end_second);
    console.log(total_second);

    total = end_hours - start_hours;
    if (end_hours < start_hours){
      console.log("shift goes on next day");
      var add_start=24-start_hours;
      console.log(add_start);
      var add_end=end_hours;
      console.log(add_end);
      total=parseInt(add_start)  + parseInt(add_end);
    }

    if(total_minute >=60){
      console.log("calculate minute");
      total_minute = total_minute - 60
      console.log(total_minute) 
      total = total + 1;
    }

    if(total_second >= 60){
      console.log("colculate second");
      total_second = total_second - 60;
      total_minute = total_minute +1;
    }
    
    total=total+":"+total_minute+":"+total_second;
    console.log(total);
    frm.set_value("no_of_hours", total);
})



