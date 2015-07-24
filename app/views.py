from django.shortcuts import render
from .models import Sport

def sport_list(request):
	sports = Sport.objects.order_by('name')
	return render(request, 'sport/sport_list.html', {'sports': sports})
