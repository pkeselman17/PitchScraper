
$(document).ready(function(){
    var initialLocation;
    var browserSupportFlag = new Boolean();
    var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
    initialize();
    
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
    
        // [END region_getplaces]
    
        // Bias the SearchBox results towards places that are within the bounds of the
        // current map's viewport.
        google.maps.event.addListener(map, 'bounds_changed', function () {
            var bounds = map.getBounds();
        });
    }
});
