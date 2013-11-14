// carousel
$('.carousel').carousel({
  interval: 5000
})

// tooltips for social links
$('.tooltip-social').tooltip({
  selector: "a[data-toggle=tooltip]"
})

$('body').scrollspy({
  target: '#nav-sidebar',
  offset: 80
});

$(window).on('load', function () {
  $body.scrollspy('refresh')
})
