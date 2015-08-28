from django.shortcuts import render,redirect
from django.contrib.auth.models import Permission, User
from app.models import Sport
from game.models import Game 
from .helpers import calc_distance

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
    distances.sort()            
    return render(request, 'home/search.html', {'list':games, 'distances':distances, 'lat':lat, 'lng':lng})	
    
def profile(request, username):
    if request.user.is_authenticated():
        return render(request, 'home/profile.html', {'username':username,'user':request.user})
    return redirect('/accounts/login/')
	

    