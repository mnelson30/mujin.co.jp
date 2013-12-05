// carousel
$('.carousel').carousel({
  interval: 5000
});

// tooltips for social links
$('.tooltip-social').tooltip({
  selector: 'a[data-toggle=tooltip]'
});

$('#mail-link').click(function() {
  var body = '';
  $('#contactform [data-human-name]').each(function() {
    var $this = $(this);

    body += '<b>' + $this.data('humanName') + '</b><br/>';
    body += $this.val() + '<br/>';
    body += '<br/>';
  });

  var subject = 'Inquiry from ' + $('#first_name').val() + ' ' + $('#last_name').val();

  $.ajax({
    type: 'POST',
    url: '/app/contactSubmit',
    data: JSON.stringify({
      subject: subject,
      body: body
    }),
    success: function() {
      $('#contactform #form').hide();
      $('#contactform #thanks').show();
    },
    dataType: 'json',
    contentType: 'application/json; charset=UTF-8'
  });
});
