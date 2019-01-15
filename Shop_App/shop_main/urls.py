from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^success_register/$', views.success_register, name='success_register'),
	url(r'^loging_in/$', views.loging_in, name='loging_in'),
]
