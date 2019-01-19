from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^success_register/$', views.success_register, name='success_register'),
	url(r'^loging_in/$', views.loging_in, name='loging_in'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^login_success/$', views.login_success, name='login_success'),
	url(r'^product/(?P<id>\d+)/$', views.product, name="product")
]
