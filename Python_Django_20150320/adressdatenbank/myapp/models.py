from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique = True)
	
	# Slug = Whitespaces will be replaced by '-' --> Safer urls
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
		
	class Meta:
		# sonst wuerde im Admin tool 'categorys' stehen
		verbose_name_plural = 'categories'
	
	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title

from django.contrib.auth.models import User
		
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	website = models.URLField(blank=True)
	#picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __str__(self):
		return self.user.username
		

		