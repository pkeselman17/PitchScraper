/* Google Place search section */
function initialize(){
	var autocomplete = new google.maps.places.Autocomplete((document.getElementById('pac-input')),
		{types:['geocode']});
		
	google.maps.event.addListener(autocomplete, 'place_changed', function(){
		var place = autocomplete.getPlace();
		$("#lat").val(place.geometry.location.lat());
		$("#lng").val(place.geometry.location.lng());
	});
}
google.maps.event.addDomListener(window, 'load', initialize);
/* END SECTION */

/*Search Function section */
$(document).ready(function(){
	$(".button.postfix").on("click", function(){
		var lat= $("#lat").val();
		var lng= $("#lng").val();
		var url= "/search?lat=" + lat + "&lng=" + lng;
		window.location.href= url;
	});
});

/* END SECTION */