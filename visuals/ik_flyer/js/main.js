// assume debug if running on localhost or an ip address
var hostname = (location.host || 'localhost').split(':')[0];
var isIPAddress = function(addr) {
  if (addr.split('.').length !== 4) {
    return false;
  }
  else {
    for (var i = 0; i < 4; i++) {
      var part = addr.split('.')[i];
      if (parseInt(part) + '' === 'NaN' || parseInt(part) >= 256) {
        return false;
      }
    }
  }
  return true;
};
if (hostname == 'localhost' || isIPAddress(hostname)) {
  var DEBUG = true;
}
else {
  var DEBUG = false;
}

$(document).ready(function() {
  if (DEBUG) {
    // live reloads to make development easy
    var script = document.createElement('script');
    script.src = 'http://' + (location.host || 'localhost').split(':')[0] + ':35729/livereload.js?snipver=1';
    document.body.appendChild(script);
  }
});
