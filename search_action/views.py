from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

# Modify this page for Search MAIN page
def searchView(request):
	return render_to_response('search.html',{ 'user':request.user })

# Modify this page for IMAGE Search
def imageSearch(request):
	return render_to_response('image_search.html', { 'user':request.user} )

# Modify this page for TEXT based Search
def textSearch(request):
	return render_to_response('text_search.html', { 'user':request.user} )

# Modify this page for Movie DNA Search
def movieSearch(request):
	return render_to_response('movie_search.html', { 'user':request.user} )

# Modify this page for Integrated Search
def intgSearch(request):
	return render_to_response('intg_search.html', { 'user':request.user} )
