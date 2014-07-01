from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
def login_user(request):
	state = "Please login below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			state = "Logged in!"
		else:
			state = "Your username or password were incorrect."
			username = ''
	return render_to_response('search.html',{'state':state, 'username':username})

@csrf_exempt
def register_user(self):
	return render_to_response('register.html')

def logout_user(request):
	logout(request)
	username = ''
	return render_to_response('search.html',{'username':username})

@csrf_exempt
def register_req(request):
	state = "There's something wrong. Please reload this page"
	username = password1 = password2 = ''
	if request.POST:
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		# Check username is blank
		if not username:
			state = "Please type your username in the field"
			return render_to_response('register.html',{'state':state})
		# Check password is same
		if password1 == password2:
			pass
		else:
			state = "Passwords are not same"
			return render_to_response('search.html',{'state':state})
		# Check ID is not exist & Register User
		try:
			find = User.objects.get(username=username)
		except User.DoesNotExist:
			user = User.objects.create_user(username,'',password1)
			user.save()
			state = "Registraion complete. Please log on."
	return render_to_response('search.html',{'state':state})
