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
    distances=[]
    
    #Check each game's distance from searched (lat,lng) and append those under 20 miles
    for g in allGames:
        distance = calc_distance(lat,lng,g.latitude,g.longitude)
        if distance <=20:
            distances.append(distance)
            games.append(g)
            
    return render(request, 'home/search.html', {'list':games, 'distances':distances})	
	
#Calculates distance between (lat,lng) points	
def calc_distance(lat1, long1, lat2, long2):
 
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
    
    #Convert to miles and round to 2 decimal points
    
    distance = float("{0:.2f}".format(3959 * arc))
    return distance
    