from django.shortcuts import render,redirect
from .models import Game
from .forms import CreateForm
import datetime

def create(request, sport):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			t = datetime.datetime.strptime(data['time'],'%I:%M %p').time()
			dt = datetime.datetime.combine(data['date'], t)
			game = Game(sport=data['sport'], latitude=data['latitude'], longitude=data['longitude'], description=data['description'], date= dt, created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
			game.save()
			return redirect('/')
	else:
		if(sport != None):
			form = CreateForm(initial={'sport': sport})
		else:
			form = CreateForm()
	return render(request, 'game/create.html', {'form': form, 'sport': sport})
	
	
