from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

# Modify this page to search
def search_view(request):
	return render_to_response('search.html')
