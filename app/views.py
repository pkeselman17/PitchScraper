from django.shortcuts import render
from .models import Sport
from django.contrib.auth.decorators import login_required

@login_required
def sport_list(request):
	sports = Sport.objects.order_by('name')
	return render(request, 'sport/sport_list.html', {'sports': sports})
