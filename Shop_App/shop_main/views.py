
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	
	context = {
	'title': 'Electronic Shop',
	}

	return render(request, 'index.html', context);
