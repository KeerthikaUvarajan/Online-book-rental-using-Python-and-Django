from django.db import models
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class BookLeaseUser(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	username = models.CharField(max_length=15,primary_key=True)
	password1 = models.CharField(max_length=15)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email = models.EmailField()
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=30)
	zipcode = models.CharField(max_length=15)
	phonenumber = models.CharField(max_length=30)
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
	school = models.CharField(max_length=30)
	work = models.CharField(max_length=30)
	agreetermsandconditions = models.BooleanField(default=False, blank=False)
	description = models.CharField(max_length=200)
	
	def __str__(self):
		return u'%s %s' % (self.firstname,self.lastname)

	
class Book(models.Model):
	AVAILABLE = 'AV'
	ON_HOLD = 'OH'
	RENTED = 'RE'
	BOOK_STATUS = (
		('AV', 'Available'),
		('OH', 'On Hold'),
		('RE', 'Rented'),
	)
	book_owner = models.ForeignKey(BookLeaseUser)
	#book_owner = models.CharField(max_length=30)
	book_name = models.CharField(max_length=30)
	book_author = models.CharField(max_length=30)
	edition = models.IntegerField()
	isbn = models.IntegerField()
	book_status = models.CharField(max_length=2,choices=BOOK_STATUS,default=AVAILABLE,blank=True)
	image = models.ImageField(upload_to = 'booklease/images/',null=True,blank=True)
	price = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal('0.00'))

	def __str__(self):
		return u'%s' % (self.book_name)
	
	
class BorrowedBook(models.Model):
	AVAILABLE = 'AV'
	ON_HOLD = 'OH'
	RENTED = 'RE'
	RETURNED = 'RT'
	BOOK_STATUS = (
		('RE', 'Rented'),
		('RT', 'Returned'),
	)
	borrowed_book_owner = models.ForeignKey(BookLeaseUser,related_name='borrowed_book_owner')
	borrowed_book_name = models.ForeignKey(Book,related_name='borrowed_book_name')
	book_borrowed_by = models.ForeignKey(BookLeaseUser,related_name='borrowed_book_by')
	start_date = models.DateTimeField(auto_now=True)
	end_date = models.DateTimeField(auto_now=False)
	book_status = models.CharField(max_length=2,choices=BOOK_STATUS,default=RENTED)
	
	#def __str__(self):
		#return u'Book Name: %s - Owned By: %s - Borrowed By: %s' % (self.borrowed_book_name, self.borrowed_book_owner, self.book_borrowed_by)
	
	
class Reviews(models.Model):
	review_by = models.ForeignKey(BookLeaseUser,related_name='review_by')
	review_for = models.ForeignKey(BookLeaseUser,related_name='review_for')
	review = models.CharField(max_length=200)
	rating = models.IntegerField()

	#def __str__(self):
		#return u'Review By: %s - Review For: %s - Rating: %d' % (self.review_by, self.review_for, self.rating)