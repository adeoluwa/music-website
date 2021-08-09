var map = '';
var center;

function initialize() {
  var mapOptions = {
    zoom: 16,
    center: new google.maps.LatLng(37.769725, -122.462154),
    scrollwheel: false,
  };

  map = new google.maps.Map(document.getElementById('google-map'), mapOptions);

  google.maps.event.addDomListener(map, 'idle', function () {
    calculateCenter();
  });

  google.maps.event.addDomListener(window, 'resize', function () {
    map.setCenter(center);
  });
}

function calculateCenter() {
  center = map.getCenter();
}

function loadGoogleMap() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.src =
    'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' +
    'callback=initialize';
  document.body.appendChild(script);
}

function setNavbar() {
  if ($(document).scrollTop() > 160) {
    $('.tm-sidebar').addClass('sticky');
  } else {
    $('.tm-sidebar').removeClass('sticky');
  }
}

$(document).ready(function () {
  // Single page nav
  $('.tm-main-nav').singlePageNav({
    currentClass: 'active',
    offset: 20,
  });

  // Detect window scroll and change navbar
  setNavbar();

  $(window).scroll(function () {
    setNavbar();
  });

  // Magnific pop up
  $('.tm-gallery').magnificPopup({
    delegate: 'a', // child items selector, by clicking on it popup will open
    type: 'image',
    gallery: { enabled: true },
    // other options
  });

  // Google Map
  loadGoogleMap();
});
