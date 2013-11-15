// carousel
$('.carousel').carousel({
  interval: 5000
})

// tooltips for social links
$('.tooltip-social').tooltip({
  selector: "a[data-toggle=tooltip]"
});


$('#form_submit').click(function() {
  var body = '';
  $('#contactform [data-human-name]').each(function() {
    var $this = $(this);

    body += '[' + $this.data('humanName') + ']\n';
    body += $this.val() + '\n';
    body += '\n';
  });
  var subject = 'New inquiry from ' + $('#first_name').val() + ' '  + $('#last_name').val() 
  
  var address = 'mailto:' + encodeURI('info@mujin.co.jp?subject=' + subject + '&body=' + body);
  window.location = window.location.href = address;
});
