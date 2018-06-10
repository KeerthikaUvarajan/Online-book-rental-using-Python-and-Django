from django import forms
from .models import BookLeaseUser, Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SigninForm(forms.Form):
	username = forms.CharField(max_length=15,required=True)
	password = forms.CharField(max_length=15,required=True)
	
class MyRegistrationForm(UserCreationForm):
	GENDER_CHOICES=[('M','Male'), ('F','Female')]
	
	email = forms.EmailField()
	firstname = forms.CharField(max_length=30)
	lastname = forms.CharField(max_length=30)
	email = forms.EmailField()
	address = forms.CharField(max_length=50)
	city = forms.CharField(max_length=60)
	state = forms.CharField(max_length=30)
	zipcode = forms.CharField(max_length=15)
	phonenumber = forms.CharField(max_length=30)
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	school = forms.CharField(max_length=30)
	work = forms.CharField(max_length=30)
	description = forms.CharField(max_length=200)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'address', 'city', 'state', 'zipcode', 'phonenumber', 'gender', 'school', 'work', 'description')
		
		def save(self, commit=True):
			user = super(MyRegistrationForm, self).save(commit=False)
			user.email = self.cleaned_data['email']
        
			if commit:
				user.save()

			return user

class BookLeaseUserCreationForm(forms.ModelForm):
	# GENDER_CHOICES=[('Male','Male'), ('Female','Female')]
	
	# username = forms.CharField(max_length=15,required=True)
	# password = forms.CharField(max_length=15,required=True)
	# email = forms.EmailField()
	# firstname = forms.CharField(max_length=30)
	# lastname = forms.CharField(max_length=30)
	# email = forms.EmailField()
	# address = forms.CharField(max_length=50)
	# city = forms.CharField(max_length=60)
	# state = forms.CharField(max_length=30)
	# zipcode = forms.CharField(max_length=15)
	# phonenumber = forms.CharField(max_length=30)
	# gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	# school = forms.CharField(max_length=30)
	# work = forms.CharField(max_length=30)
	# description = forms.CharField(max_length=200)

	# fields = ('username', 'email', 'password', 'firstname', 'lastname', 'address', 'city', 'state', 'zipcode', 'phonenumber', 'gender', 'school', 'work', 'description')	
	
	class Meta:
		model = BookLeaseUser
		fields = '__all__'
		
		
class BookForm(forms.ModelForm):
	
	class Meta:
		model = Book
		fields = ('book_name', 'book_author', 'edition', 'isbn', 'price')

class BookFormFull(forms.ModelForm):
	
	class Meta:
		model = Book
		fields = '__all__'