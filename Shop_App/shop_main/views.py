
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .forms import Register_form
from .forms import UserLog
from .forms import Basket_form

from django.contrib.auth.hashers import make_password, check_password

from .models import User
from .models import Product_Type
from .models import Product

# Create your views here.
def index(request):

	login = ''

	Products = Product.objects.all();


	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']
		#print("jep it works")


	context = {
	'title': 'Electronic Shop',
	'Products': Products,
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
			if not User.objects.get(nick=form.cleaned_data['usernameInput']):
				user = User.objects.create(nick = form.cleaned_data['usernameInput'],
				name=form.cleaned_data['nameInput'],last_name=form.cleaned_data['lastnameInput'],
				password=make_password(form.cleaned_data['password']))
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
	error = ''
	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']
		#print("jep it works")
	form = None;
	test = False;



	if request.method == 'POST':
		form = UserLog(request.POST)
		if form.is_valid():
			#test = True;
			nickname = form.cleaned_data['username'];
			if User.objects.filter(nick = nickname):
				user = User.objects.get(nick = nickname)
				if check_password(form.cleaned_data['password'], user.password):
					test = True
			else:
				error = 'Unknow combinnation'
			#form = UserLog()
			#return HttpResponse("dupa");

	else:
		form = UserLog()

	context = {
		'form': form,
		'error': error,
		'title': 'Electronic Shop',
		'login': login
	}
	response = render(request, 'login_site.html',context);
	if test:
		response.set_cookie('nickname',form.cleaned_data['username']),
		response.set_cookie('password',form.cleaned_data['password']),



	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']
		#print("jep it works")

	response['login'] = login;

	if test:
		login = form.cleaned_data['username']
		password = form.cleaned_data['password']
		return login_success(request,login,password);

	return response

def success_register(request):

	login = ''
	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']

	form = None;
	test = False;
	if request.method == 'POST':
		form = Register_form(request.POST)
		if form.is_valid():
			if not User.objects.filter(nick=form.cleaned_data['usernameInput']):
				user = User.objects.create(nick = form.cleaned_data['usernameInput'],
				name=form.cleaned_data['nameInput'],last_name=form.cleaned_data['lastnameInput'],
				password=make_password(form.cleaned_data['password']))
				test = True;

	else:
		form = Register_form()


	context = {

		'title' : 'Electronic Shop',
		'login' : login
	}

	return render(request, 'success_register.html',context);

def logout(request):
	login = ''

			#form = UserLog()
			#return HttpResponse("dupa");

	context = {
	'title': 'Electronic Shop',
	'login': login,
	}
	response = render(request, 'logout_site.html', context)

	response.delete_cookie('nickname')
	response.delete_cookie('password')


	return response;
def login_success(request,login,password):
	#login = ''
	test = False

	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']

	if request.method == 'POST':
		form = UserLog(request.POST)
		if form.is_valid():
			test = True

	context = {
	'title': 'Electionic Shop',
	'login':''
	}

	if test == False:
		return loging_in(request)

	if login and password:
		response.set_cookie('nickname',login),
		response.set_cookie('password',password),


	response['login'] = login;

	return response
def product(request,id):

	login = None

	product = Product.objects.get(id=id);

	if 'basket' in request.COOKIES:
		basket = request.COOCKIES['basket'];

	response = render(request, 'product.html');

	if request.method == 'POST':
		form =  Basket_form(request.POST)
		#basket += [product.id,form.cleaned_data['mount_of']]
		response.set_cookie('basket',basket)
	else:
		form = Basket_form();


	if 'nickname' in request.COOKIES and 'password' in request.COOKIES:
		login = request.COOKIES['nickname']


	#response['form'] = form;
	response['login'] = login;
	response['product'] = product
	response['title'] = 'Electronic Shop'

	context = {
		'product': product,
		'login': login,
		'form': form,
		'title': 'Electronic Shop'
	}
	

	return response;
