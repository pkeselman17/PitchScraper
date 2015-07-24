from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.sport_list, name='sport_list')
]