
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .forms import Register_form
from .forms import UserLog



from .models import User

# Create your views here.
def index(request):

	login = ''

	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']
		#print("jep it works")

	if request.method == 'POST':
		form = UserLog(request.POST)
		if form.is_valid():
			test = True;
			request.set_cookie('nickname',form.cleaned_data['username']),
			request.set_cookie('password',form.cleaned_data['password']),
			#form = UserLog()
			#return HttpResponse("dupa");

	else:
		form = UserLog()

	context = {
	'title': 'Electronic Shop',
	'login': login
	}

	return render(request, 'main_site.html', context);
def register(request):
	login = ''
	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']
		#print("jep it works")
	form = None;
	test = False;
	if request.method == 'POST':
		form = Register_form(request.POST)

		if form.is_valid():
			test = True;

	else:
		form = Register_form()

	context = {
	'form': form,
	'title' : 'Electronic Shop',
	'login': login
	}

	return render(request, 'register_site.html',context);

def loging_in(request):
	login = ''
	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']
		#print("jep it works")
	form = None;
	test = False;


	if request.method == 'POST':
		form = UserLog(request.POST)
		if form.is_valid():
			test = True;
			#form = UserLog()
			#return HttpResponse("dupa");

	else:
		form = UserLog()

	context = {
		'form': form,
		'title': 'Electronic Shop',
		'login': login
	}

	response = render(request, 'login_site.html',context);
	if test:
		response.set_cookie('nickname',form.cleaned_data['username']),
		response.set_cookie('password',form.cleaned_data['password']),

	return response

def success_register(request):

	login = ''

	context = {

		'title' : 'Electronic Shop',
		'login' : login
	}

	return render(request, 'success_register.html',context);
