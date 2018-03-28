// Copyright (c) 2018, Digitalprizm and contributors
// For license information, please see license.txt

frappe.ui.form.on('Upload Shift Schedule', {
	refresh: function(frm) {

	}
});

// Copyright (c) 2017, DPI-Sagar and contributors
// For license information, please see license.txt

frappe.provide("bnd.bnd");

bnd.bnd.UploadCn = frappe.ui.form.Controller.extend({
	refresh: function() {
		this.frm.disable_save();
		this.show_upload();
		cur_frm.add_custom_button(__('<i class="fa fa-home" title="Back" style="margin-left: 10px;background-color: red;padding: 6px;margin: -10px;border-radius: 5px;color: white;"> Cancel</i>'),
			function () { frappe.set_route("/"); }, 'fa fa-home btn-default', 'btn-danger');
	},
	from_date: function() {
		cur_frm.set_value("to_date",frappe.datetime.add_days(cur_frm.doc.from_date,6));
	},
	get_template:function() {
		window.location.href = repl(frappe.request.url +
			'?cmd=%(cmd)s&from_date=%(from_date)s&to_date=%(to_date)s', {
				cmd: "bnd.bnd.doctype.upload_shift_schedule.upload_shift_schedule.get_template",
				from_date: this.frm.doc.from_date,
				to_date: this.frm.doc.to_date,
			});
	},


	show_upload: function() {
		var me = this;
		var $wrapper = $(cur_frm.fields_dict.upload_html.wrapper).empty();

		// upload
		frappe.upload.make({
			parent: $wrapper,
			args: {
				method: 'bnd.bnd.doctype.upload_shift_schedule.upload_shift_schedule.upload'
			},
			sample_url: "e.g. http://domain.com/somefile.csv",
			callback: function(attachment, r) {
				var $log_wrapper = $(cur_frm.fields_dict.import_log.wrapper).empty();

				if(!r.messages) r.messages = [];
				// replace links if error has occured
				if(r.exc || r.error) {
					r.messages = $.map(r.message.messages, function(v) {
						var msg = v.replace("Inserted", "Valid")
							.replace("Updated", "Valid").split("<");
						if (msg.length > 1) {
							v = msg[0] + (msg[1].split(">").slice(-1)[0]);
						} else {
							v = msg[0];
						}
						return v;
					});

					r.messages = ["<h4 style='color:red'>"+__("Import Failed!")+"</h4>"]
						.concat(r.messages)
				} else {
					r.messages = ["<h4 style='color:green'>"+__("Import Successful!")+"</h4>"].
						concat(r.message.messages)
				}

				$.each(r.messages, function(i, v) {
					var $p = $('<p>').html(v).appendTo($log_wrapper);
					if(v.substr(0,5)=='Error') {
						$p.css('color', 'red');
					} else if(v.substr(0,8)=='Inserted') {
						$p.css('color', 'green');
					} else if(v.substr(0,7)=='Updated') {
						$p.css('color', 'green');
					} else if(v.substr(0,5)=='Valid') {
						$p.css('color', '#777');
					}
				});
			}
		});

		// rename button
		$wrapper.find('form input[type="submit"]')
			.attr('value', 'Upload and Import')
	}
})

cur_frm.cscript = new bnd.bnd.UploadCn({frm: cur_frm});