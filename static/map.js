var map;
var markers = [];
var circles = [];
var oldCircle;
var oldMarker;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), 
    {
       disableDefaultUI:true
    }); 
//    navigator.geolocation.getCurrentPosition(function(position) {
//      var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
//      map.setCenter(initialLocation);
//      map.setZoom(3);
//    }, function(positionError) {
    // User denied geolocation prompt - default to Chicago
      map.setCenter(new google.maps.LatLng(39.8097343, -98.5556199));
      map.setZoom(3);
//    });
    map.addListener('click', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
    });
}
function openModal(){
  //alert("cheked the button - worked");
  $(".modal").addClass("is-active");
  $("input[name=name]").focus();
}

function closeModal() {
  $(".modal").removeClass("is-active");
};

function addToMap(interest){
  var dataToSend = {
     "interest": interest,
     "name": document.getElementById('name').value,
     "email":  document.getElementById('email').value,
     "contact":  document.getElementById('contact').value,
     "lat": oldMarker.getPosition().lat(),
     "lng": oldMarker.getPosition().lng(),
     "radius": oldCircle.getRadius() / 1609.34
  }
  closeModal();
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if(this.readyState == 4 && this.status == 200) {
           var neighbors = JSON.parse(xhttp.responseText);
           console.log(neighbors);
           displayNeighbors(neighbors);
      }
  }
  xhttp.open("POST", "/getpyram", true);
  xhttp.send(JSON.stringify(dataToSend));
}

function resizeCircle(raidus) {
   oldCircle.setRadius(document.getElementById('radius').value * 1609.34);   
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

function highlightPerson(id) {
  var newCircle = new google.maps.Circle({
	fillColor: '#f45342',
	strokeColor: '#f45342',
	strokeOpacity: 0.2,
   	center: circles[id].center,
	radius: circles[id].radius,
	map: map
  });
  circles[id].setMap(null);
  circles[id] = newCircle;
}

function unhighlightPerson(id) {

  var newCircle = new google.maps.Circle({
	fillColor: '#f4b642',
	strokeColor: '#f4b642',
	strokeOpacity: 0.2,
   	center: circles[id].center,
	radius: circles[id].radius,
	map: map
  });
  circles[id].setMap(null);
  circles[id] = newCircle;

}

function displayNeighbors(neighbors) {
  var list = document.getElementById("menu-list");

  var i = 0;
  neighbors.forEach(function(person) {
   var personForList = document.createElement("LI");
   personForList.className = "menu-item";
   personForList.id = i.toString();
   var linkForPerson = document.createElement("a");
   linkForPerson.id = i.toString();
   linkForPerson.setAttribute("onmouseover", "highlightPerson(this.id)");
   linkForPerson.setAttribute("onmouseout", "unhighlightPerson(this.id)");
   linkForPerson.appendChild(document.createTextNode(person.name));
   personForList.appendChild(linkForPerson);
   var contactInfoList = document.createElement("UL");
   var contactInfo = document.createElement("LI");
   contactInfo.appendChild(document.createTextNode(person['contact info']));
   contactInfoList.appendChild(contactInfo);
   personForList.appendChild(contactInfoList);
   list.appendChild(personForList);
   var marker = new google.maps.Marker({
     position: {
         "lat": person.latitude,
         "lng": person.longitude
     },
     map:map,
     icon:'../static/Assets/Flame-Orange-Other-Small.png',
     size: google.maps.Size(20, 20)
   });
  markers.push(marker);
  var circle = new google.maps.Circle({
     center: {
        "lat":person.latitude,
        "lng": person.longitude
     },
     map: map,
     strokeColor: '#F4B642',
     strokeOpacity: 0.2,
     strokeWeight: 1,
     radius: person.radius * 1609.34,
     fillColor: '#F4B642',
     fillOpacity: 0.2
   });
  circles.push(circle);
  i = i + 1;
  });
  document.getElementById("menu-div").style.display = "block";
}
