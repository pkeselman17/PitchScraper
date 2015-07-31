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
		var sport = $("select").val();
		if(lat == "" && lng == "" && sport == null){
			$("#pac-input").css("box-shadow", "0 0 10px 1px red");
			$("select").css("box-shadow", "0 0 10px 1px red");
		}
		else if(sport == null){
			$("#pac-input").css("box-shadow", "none");
			
			$("select").css("box-shadow", "0 0 10px 1px red");
		}
		else if(lat == "" && lng == ""){
			$("select").css("box-shadow", "none");
			
			$("#pac-input").css("box-shadow", "0 0 10px 1px red");
		}
		else{
			var url= "/search?sport=" + sport + "&lat=" + lat + "&lng=" + lng;
			window.location.href= url;
		}
	});
});

/* END SECTION */