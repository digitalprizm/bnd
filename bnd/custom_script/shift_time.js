frappe.ui.form.on("Shift Time", "validate", function(frm, cdt, cdn) {		
    console.log("hello");  
    let start_time = cur_frm.doc.start_time;    
    console.log(start_time);
    let end_time = cur_frm.doc.end_time;    
    console.log(end_time);
    let total = addTimes(start_time, end_time);
    console.log(total);
    frm.set_value("no_of_hours", total);
})
function timeToMins(time) {
  var b = time.split(':');
  return b[0]*60 + +b[1];
}
function timeFromMins(mins) {
  function z(n){return (n<10? '0':'') + n;}
  var h = (mins/60 |0) % 24;
  var m = mins % 60;
  return z(h) + ':' + z(m);
}
function addTimes(t0, t1) {
  return timeFromMins(timeToMins(t0) + timeToMins(t1));
}