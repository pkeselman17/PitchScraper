from django.shortcuts import render

def sport_list(request):
	return render(request, 'sport/sport_list.html', {})
