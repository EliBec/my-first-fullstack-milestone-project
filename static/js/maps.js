/* Google Map Code taken from Google Map JavaScript API */
// Initialize and add the map
function initMap() {
    // The location of KiddiesSpot
     var Loc = { lat: 34.4955633, lng: -77.473468 };
    // The map, centered at KiddiesSpot
     var map = new google.maps.Map(document.getElementById("googlemap"), {
      zoom: 6,
      center: Loc,
     });


     // The marker, positioned at KiddiesSpot's coordinates
      var marker = new google.maps.Marker({ position: Loc, map: map,
      title:'133 James Avenue Surf City, NC 24485',
      label: {
              fontSize: '16px',
              fontWeight: 'Bold',
              text:"Beck's Outdoors",
              color: '#1A8849'},
        url :'https://www.google.com/maps/place/133+James+Ave,+Holly+Ridge,+NC+28445/@34.4419231,-77.5659881,17z/data=!3m1!4b1!4m5!3m4!1s0x89a9987f3d7ed3bf:0xff3c61e3573c100d!8m2!3d34.4419231!4d-77.5637994'
      });

    // Open Google Maps on a new tab upon clicking the marker
       google.maps.event.addListener(marker, 'click', function(event) {
        window.open(this.url, '_blank');
       });
    }