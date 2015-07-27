from django.shortcuts import render,redirect
from django.contrib.auth.models import Permission, User

def index(request):
	if request.user.is_authenticated():
		return render(request, 'home/index.html', {})
	return redirect('accounts/login/')