from django.db import models

from cloudinary.models import CloudinaryField

from chalk_root.users.models import User

app_name = "main"

class UserType(models.Model):
	"""
		UserType: Used to store the type of user Ex: Student, Principal, Professor etc.
	"""
	name = models.CharField("Type of User", max_length=50)

	def __str__(self):
		return self.name


class UserInfo(models.Model):
	"""
	Description: Preferences and information about the user
	"""
	user = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)
	user_type = models.ForeignKey("UserType", blank=True, null=True, on_delete=models.CASCADE)
	school_admin = models.ForeignKey('School', blank=True, null=True, related_name='school_admin', on_delete=models.CASCADE)
	employment_details = models.TextField(blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	photo = models.TextField(blank=True, null=True)
	child_school = models.ForeignKey('School', blank=True, null=True, related_name='child_school', on_delete=models.CASCADE)
	facility_preferred = models.ManyToManyField('School')
	

	class Meta:
		pass

class School(models.Model):
	"""
	School: Strores all details about the school
	"""
	sid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30, blank=True, null=True)
	category =  models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)
	address_line1 = models.CharField(max_length=30, blank=True, null=True)
	address_line2 = models.CharField(max_length=30, blank=True, null=True)
	area = models.CharField(max_length=30, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=30, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	facilities = models.CharField(max_length=100 ,blank=True, null=True)
	contact_number = models.CharField(max_length=20,blank=True, null=True)
	website = models.CharField(max_length=30, blank=True, null=True)
	photos = CloudinaryField('image',blank=True, null=True)
	admission_info = models.TextField(blank=True, null=True)
	overall_rating = models.FloatField(blank=True, null=True)
	board = models.ForeignKey('Board', blank=True, null=True, on_delete=models.CASCADE)
	added_by = models.ForeignKey("users.User", blank=True, null=True, related_name='school_creator', on_delete=models.CASCADE)
	def __str__(self):
		return self.name


class Board(models.Model):
	"""
	Facilities: Stores individual facility provided info
	"""
	name = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.name


class Reviews(models.Model):
	"""
	Reviews: Stores reviews for each school
	"""
	school = models.ForeignKey('School', blank=True, null=True, on_delete=models.CASCADE)
	parent = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)
	review_content = models.TextField(blank=True, null=True)
	rating = models.CharField(max_length=10)

	def __str__(self):
		return parent.name

class Category(models.Model):
	"""
	Category: Stores the type of school, primary, secondary,etc.
	"""
	name = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.name
	