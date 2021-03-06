# search_action/view.py

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
# PIL: Python Image Library
from PIL import Image
from os.path import join

# Media Upload
@csrf_exempt
def upload_media(request):
    query = ''
    if request.method == 'POST':
        if 'file' in request.FILES:
            MEDIA_DIR = '/Users/sogo/Documents/Projects/14.7_AnT_internship/MAM_searchEngine/media/'
            file = request.FILES['file']
            filename = file._name
            fp = open('%s/%s' % (MEDIA_DIR, filename), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            #query = 'File Uploaded'
            return render_to_response('intg_search.html', {'user':request.user, 'query':query})
        else:
            #query = 'Not valid File please check search_action/views.py Line:20'
            return render_to_response('intg_search.html', {'user':request.user, 'query':query})
    #query = 'Fail to Upload, please check search_action/views.py Line: 26'
    return render_to_response('intg_search.html', {'user':request.user, 'query':query})

# Image Uploaid
@csrf_exempt
def upload_image(request):
    img = None
    query = ''
    if request.method == "POST":
        if 'file' in request.FILES:
            IMAGE_DIR = '/Users/sogo/Documents/Projects/14.7_AnT_internship/MAM_searchEngine/images/'
            file = request.FILES['file']
            filename = file._name
            fp = open('%s/%s' % (IMAGE_DIR, filename), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close() # Upload is over

            #query = 'Image Uploaded' # TODO: execute when uploaded, show thumbnail
            IMAGE_DIR = '/images/'
            img = join(IMAGE_DIR, filename)
            return render_to_response('intg_search.html', {'user':request.user, 'query':query, 'img':img})
        return render_to_response('intg_search.html', {'user':request.user})
    #query = 'Fail to Upload, please check search_action/views.py upload_image function'
    return render_to_response('intg_search.html', {'user':request.user, 'query':query})


# Modify this page for Search MAIN page
@csrf_exempt
def searchView(request):
    query = ''
    if request.POST:
        query = request.POST.get('inputField')
    return render_to_response('intg_search.html',{ 'user':request.user, 'query':query })

# Modify this page for IMAGE Search
@csrf_exempt
def imageSearch(request):
    query = 'This is search QUERY'
    if request.POST:
        query = request.POST.get('inputField')
    return render_to_response('image_search.html',{ 'user':request.user, 'query':query })

# Modify this page for TEXT based Search
@csrf_exempt
def textSearch(request):
    query = 'This is search QUERY'
    if request.POST:
        query = request.POST.get('inputField')
    return render_to_response('text_search.html',{ 'user':request.user, 'query':query })

# Modify this page for Movie DNA Search
@csrf_exempt
def movieSearch(request):
    query = 'This is search QUERY'
    if request.POST:
        query = request.POST.get('inputField')
    return render_to_response('movie_search.html',{ 'user':request.user, 'query':query })

# Modify this page for Integrated Search
@csrf_exempt
def intgSearch(request):
    query = ''
    if request.POST:
        query = request.POST.get('inputField')
    return render_to_response('intg_search.html',{ 'user':request.user, 'query':query })

def Demo(request):
    return render_to_response('intgResult.html')
