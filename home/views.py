from django.shortcuts import render,redirect
from django.contrib.auth.models import Permission, User
from app.models import Sport

def index(request):
	if request.user.is_authenticated():
		return render(request, 'home/index.html', {"sports":Sport.objects.all()})
	return redirect('accounts/login/')
	
def search(request):
	lat = float(request.GET.get('lat'))
	lng = float(request.GET.get('lng'))
	return render(request, 'home/search.html', {'lat':lat, 'lng':lng})	