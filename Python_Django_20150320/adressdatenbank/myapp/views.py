from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from myapp.models import Category, Page
from datetime import datetime
# Create your views here.
def index(request):
	'''
	#Create Test Cookie to check if browser supports it
	request.session.set_test_cookie()
	'''
	# Get the objects from Category
	category_list = Category.objects.order_by('-likes')[:5]
	pages_list = Page.objects.order_by('-views')[:5]
	context_dict = {
		'boldmessage' : 'I am the bold message',
		'categories' : category_list,
		'pages': pages_list,}
		
	# Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, we default to zero and cast that.
	#visits = int(request.COOKIES.get('visits', '1'))
	
	visits = request.session.get('visits')
	
	if not visits:
		visits = 1
	
	reset_last_visit_time = False
	
	last_visit = request.session.get('last_visit')
	if last_visit:
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
		
		if (datetime.now() - last_visit_time).days > 0:
			visits += 1
			reset_last_visit_time = True
	else:
		# Cookie last_visit doesn't exist, so flag that it should be set.
		reset_last_visit_time = True
		
	if reset_last_visit_time:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = visits
	
	context_dict['visits'] = visits
	
	response = render(request, 'myapp/index.html', context_dict)
	
	return response
	
def about(request):
	visits = request.session.get('about_visits')
	
	if visits:
		print "visits: " + str(visits)
		visits += 1
	else:
		print "visits = 1"
		visits = 1
	
	request.session['about_visits'] = visits
	
	context_dict = {'a': 'This is a variable', 'about_visits': visits}
	return render( request, 'myapp/about.html', context_dict)
	
def category(request, category_name_slug):
	context_dict = {}
	
	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name
		
		pages = Page.objects.filter(category=category)
		
		context_dict['pages'] = pages
		context_dict['category'] = category
		context_dict['name_slug'] = category.slug
	
	except Category.DoesNotExist:
		pass
	
	return render(request, 'myapp/category.html', context_dict)
	
from myapp.forms import CategoryForm

def add_category(request):
	# Wenn Inhalt schon eingeben
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			# call index View
			return index(request)
		else:
			print form.errors
	# Sonst zeige Seite mit Eingabemoeglichkeiten
	else:
		form = CategoryForm()
	return render(request, 'myapp/add_category.html', {'form': form})

from myapp.forms import PageForm

@login_required	
def add_page(request, category_name_slug):
	print "add_page"
	try:
		cat = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		cat = None
	
	if request.method == "POST":
		print "Hallo"
		form = PageForm(request.POST)
		if form.is_valid():
			print "Form is valid"
			if cat:
				page = form.save(commit=False)
				page.category = cat
				page.views = 0
				page.save()
				print "saved page"
				return category(request, category_name_slug)
		else:
			print form.errors
	else:
		form = PageForm()
		
	context_dict = {'form':form, 'category':cat}
	return render(request, 'myapp/add_page.html', context_dict)

from myapp.forms import UserForm, UserProfileForm
	
def register(request):
	'''
	#Check if Cookie created in index worked
	
	if request.session.test_cookie_worked():
		print ">>>> TEST COOKIE WORKED!"
		request.session.delete_test_cookie()
	'''
	registered = False
	
	if request.method == 'POST':
	
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid and profile_form.is_valid:
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			
			'''if request.Files != None and 'picture' in request.Files:
				profile.picture = request
				'''
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request, 
		'myapp/register.html', 
		{'user_form': user_form, 'profile_form':profile_form, 'registered':registered})

from django.contrib.auth import authenticate, login
		
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/myapp/')
			else:
				return HttpResponse('Your Account is disabled')
				
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("invalid login details supplied")
	else:
		return render(request, 'myapp/login.html', {})

from django.contrib.auth import logout		
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/myapp/')