var initialLocation;
var browserSupportFlag = new Boolean();
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);

function initialize() {
    var markers = [];
    var myStyles = [
        {
            featureType: "poi",
            elementType: "labels",
            stylers: [
               { visibility: "off" }
            ]
        }
    ];

    var mapOptions = {
        zoom: 6,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        zoomControl: true,
        styles: myStyles
    };
    var map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

    if (navigator.geolocation) {
        browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function (position) {
            initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            map.setCenter(initialLocation);
        }, function () {
            handleNoGeolocation(browserSupportFlag);
        });
    }
        // Browser doesn't support Geolocation
    else {
        browserSupportFlag = false;
        handleNoGeolocation(browserSupportFlag);
    }


    var input = (document.getElementById('pac-input'));
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var searchBox = new google.maps.places.SearchBox(input);


    google.maps.event.addListener(searchBox, 'places_changed', function () {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
        }
        for (var i = 0, marker; marker = markers[i]; i++) {
            marker.setMap(null);
        }

        // For each place, get the icon, place name, and location.
        markers = [];
        var bounds = new google.maps.LatLngBounds();
        for (var i = 0, place; place = places[i]; i++) {
            var image = {
                url: place.icon,
                size: new google.maps.Size(71, 71),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(25, 25)
            };

            // Create a marker for each place.
            var marker = new google.maps.Marker({
                map: map,
                icon: image,
                title: place.name,
                position: place.geometry.location
            });

            google.maps.event.addListener(marker, 'click', function () {
                var lat = marker.getPosition().lat();
                var long = marker.getPosition().lng();

                $("#id_latitude").val(lat);
                $("#id_longitude").val(long);

                $("#locationSuccess").show();
            });

            markers.push(marker);

            bounds.extend(place.geometry.location);
        }

        map.fitBounds(bounds);
    });
    // [END region_getplaces]

    // Bias the SearchBox results towards places that are within the bounds of the
    // current map's viewport.
    google.maps.event.addListener(map, 'bounds_changed', function () {
        var bounds = map.getBounds();
        searchBox.setBounds(bounds);
    });


}


function handleNoGeolocation(errorFlag) {
    if (errorFlag == true) {
        alert("Geolocation service failed.");
        initialLocation = newyork;
    } else {
        alert("Your browser doesn't support geolocation. We've placed you in New York.");
        initialLocation = newyork;
    }
    map.setCenter(initialLocation);
}
google.maps.event.addDomListener(window, 'load', initialize);