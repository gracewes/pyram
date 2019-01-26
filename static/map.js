var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), 
    {
       disableDefaultUI:true
    }); 
    navigator.geolocation.getCurrentPosition(function(position) {
      var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
      map.setCenter(initialLocation);
      map.setZoom(3);
    }, function(positionError) {
    // User denied geolocation prompt - default to Chicago
      map.setCenter(new google.maps.LatLng(39.8097343, -98.5556199));
      map.setZoom(3);
    });
    map.addListener('click', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
    });
}

function placeMarkerAndPanTo(latLng, map) {
  var marker = new google.maps.Marker({
     position: latLng,
     map:map
   });
   map.panTo(latLng);
}
