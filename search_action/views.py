from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

# Image Upload
@csrf_exempt
def upload_pic(request):
	if request.method == 'POST':
		if 'file' in request.FILES:
			UPLOAD_DIR = '/Users/sogo/Desktop/internship/codes/mam/images'
			file = request.FILES['file']
			filename = file._name
			fp = open('%s/%s' % (UPLOAD_DIR, filename), 'wb')
			for chunk in file.chunks():
				fp.write(chunk)
			fp.close()
			query = 'File Uploaded'
			return render_to_response('search.html', {'user':request.user, 'query':query})
		else:
			query = 'Not valid File please check search_action/views.py Line:20'
			return render_to_response('search.html', {'user':request.user, 'query':query})
	query = 'Fail to Upload, please check search_action/views.py Line: 26'
	return render_to_response('search.html', {'user':request.user, 'query':query})

# Modify this page for Search MAIN page
@csrf_exempt
def searchView(request):
	query = 'This is search QUERY'
	if request.POST:
		query = request.POST.get('inputField')
	return render_to_response('search.html',{ 'user':request.user, 'query':query })

# Modify this page for IMAGE Search
def imageSearch(request):
	return render_to_response('image_search.html', { 'user':request.user })

# Modify this page for TEXT based Search
def textSearch(request):
	return render_to_response('text_search.html', { 'user':request.user} )

# Modify this page for Movie DNA Search
def movieSearch(request):
	return render_to_response('movie_search.html', { 'user':request.user} )

# Modify this page for Integrated Search
def intgSearch(request):
	return render_to_response('intg_search.html', { 'user':request.user} )
