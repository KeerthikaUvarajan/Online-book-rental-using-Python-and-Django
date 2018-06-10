from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import BookLeaseUser, Book
from django.contrib.auth.forms import UserCreationForm
from booklease.forms import SigninForm, MyRegistrationForm, BookLeaseUserCreationForm
from booklease.forms import BookForm, BookFormFull
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	return render_to_response('booklease/index.html')

def signin(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('dashboard')
		else:
			return HttpResponseRedirect('invalid')
			#render(request, 'booklease/signin.html', {'form':user})
	else:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})

def register_success(request):
    return render(request, 'booklease/register_success.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		booklease_user_form = BookLeaseUserCreationForm(request.POST)

		if form.is_valid() and booklease_user_form.is_valid():
			form.save()
			booklease_user_form.save()
			return HttpResponseRedirect('register_success')
	
	else:
		form = MyRegistrationForm()
	
	args = {}
	args['form'] = form
	return render(request, 'booklease/register.html', args)

def dashboard(request):
    return render(request, 'booklease/dashboard.html')

def invalid_login(request):
    return render(request, 'booklease/invalid_login.html')

def profile(request):
    return render(request, 'booklease/profile.html')
	
def booksowned(request):
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
	
	args = {}
	recs = Book.objects.filter(book_owner=request.user.username)
	args['booklist'] = recs
	print(recs)
	return render(request, 'booklease/booksowned.html', args)
	
def rentedbooks(request):
    return render(request, 'booklease/rentedbooks.html')
	
def addbook(request):
	username = None
	if request.user.is_authenticated() == False:
		form = SigninForm()
		return render(request, 'booklease/signin.html', {'form':form})
		
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form_dict = form.cleaned_data
			form_dict['book_owner'] = request.user.username
			book_full_form = BookFormFull(form_dict)
			if(book_full_form.is_valid() == False):
				form.errors = book_full_form
			else:
				book_full_form.save(commit=True)
				return HttpResponseRedirect('addbook')
	
	else:
		form = BookForm()

	args = {}
	args['form'] = form
	return render(request, 'booklease/addbook.html', args)
	
def searchbook(request):
    return render(request, 'booklease/searchbook.html')
	
def editprofile(request):
    return render(request, 'booklease/editprofile.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('signin')

