from django.shortcuts import render
from .models import Game
from .forms import CreateForm

def create(request, sport):
	if request.method == 'POST':
		pass
	else:
		if(sport != None):
			form = CreateForm(initial={'sport': sport})
		else:
			form = CreateForm()
	return render(request, 'game/create.html', {'form': form, 'sport': sport})
	
	
