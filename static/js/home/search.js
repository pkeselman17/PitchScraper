
function initialize(points, lat, lng, distances) {
    var initialLocation;
    var browserSupportFlag = new Boolean();
    var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var labelIndex = 0;
    
    
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
        
        //add locations to map as markers
        for(var i=0;i<points.length;i++){
            var marker = new google.maps.Marker({
                position:new google.maps.LatLng(points[i].lat,points[i].lng),
                label: labels[labelIndex++ % labels.length],
                map: map
            })
            markers.push(marker);
        }
        
        addToList(markers, distances);
        
       
        
        initialLocation= new google.maps.LatLng(lat,lng)
        map.setCenter(initialLocation);
        
       
        google.maps.event.addListener(map, 'bounds_changed', function () {
            var bounds = map.getBounds();
        });
        
}

function addToList(markers,distances){
    var places = $(".places");
    var i = 0;
    while(i<markers.length){
        var div = document.createElement("div");
        div.className= ("row loc");
        div.innerHTML = "<img id='map-pin' src='https://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi-dotless_hdpi.png'/>" + "<p id='markerText'>"+ markers[i].label + "</p>" + "<p id='distInfo'>" + distances[i] + " Miles away</p>";
        places.append(div);
        i++;
    }
}

