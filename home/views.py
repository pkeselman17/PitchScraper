from django.shortcuts import render,redirect
from django.contrib.auth.models import Permission, User
from app.models import Sport
from game.models import Game
import math

def index(request):
    if request.user.is_authenticated():
        return render(request, 'home/index.html', {"sports":Sport.objects.all()})
    return redirect('accounts/login/')
	
def search(request):
    sport_id = int(request.GET.get('sport'))
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    allGames = Game.objects.all().filter(sport=sport_id)
    games=[]
    
    for g in allGames:
        if distance_on_unit_sphere(lat,lng,g.latitude,g.longitude) <=20:
            games.append(g)
            
    return render(request, 'home/search.html', {'lat':lat, 'lng':lng, 'list':games})	
	
	
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
    
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    
    # Compute spherical distance from spherical coordinates.
    
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return 3959 * arc