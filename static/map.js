var map;
var oldCircle;
var oldMarker;
var firstClick = true;
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
    if(firstClick){
      requestContactInfo();
      firstClick = false;
    }
    });
}
function requestContactInfo(){
  //alert("cheked the button - worked");
  document.getElementById('getContact').style.display= 'block' ;
}

function placeMarkerAndPanTo(latLng, map) {
   var marker = new google.maps.Marker({
     position: latLng,
     map:map,
     icon:'../static/Assets/Flame-Bright-Orange-Small.png',
     size: google.maps.Size(20, 20)
   });
  var circle = new google.maps.Circle({
     center: latLng,
     map: map,
     strokeColor: '#F4B642',
     strokeOpacity: 0.2,
     strokeWeight: 1,
     radius: document.getElementById('radius').value * 1609.34,
     fillColor: '#F4B642',
     fillOpacity: 0.35

   });
    circle.addListener('click', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
    });
   if (oldMarker != undefined) {
      oldMarker.setMap(null);
   }
   oldMarker = marker;
  
   if (oldCircle != undefined) {
      oldCircle.setMap(null);
   }
   oldCircle = circle;
   map.panTo(latLng);
}

function displayNeighbors(neighbors) {
  neighbors.foreach(function(person) {
   var marker = new google.maps.Marker({
     position: person.latLng,
     map:map,
     icon:'../static/Assets/Flame-Orange-Other-Small.png',
     size: google.maps.Size(20, 20)
   });
  var circle = new google.maps.Circle({
     center: person.latLng,
     map: map,
     strokeColor: '#F4B642',
     strokeOpacity: 0.2,
     strokeWeight: 1,
     radius: person.radius * 1609.34,
     fillColor: '#F4B642',
     fillOpacity: 0.35
   });
  });
}
