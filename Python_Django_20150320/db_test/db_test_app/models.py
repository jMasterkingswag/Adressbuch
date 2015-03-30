# encoding: utf-8
from django.db import models
# Create your models here.

	
class Residence(models.Model):
	
	zip_code = models.CharField(max_length = 5)
	residence_name = models.CharField(max_length = 128)
	name_adding = models.CharField(max_length = 128, blank = True)
	
	def __str__(self):
		return ' '.join([
			self.zip_code,
			self.residence_name,
			self.name_adding,
		])
	'''
	def save(self, *args, **kwargs):
		super(Residence, self).save(*args, **kwargs)
	'''
	
class Street(models.Model):
	street_name = models.CharField(max_length = 128)
	residence = models.ForeignKey(Residence, null = True)
	
	def __str__(self):
		return self.street_name

class Contact(models.Model):
	
	first_name = models.CharField(max_length = 128)
	second_name = models.CharField(max_length = 128, blank = True)
	last_name = models.CharField(max_length = 128)
	email = models.EmailField(blank = True)
	birth_date = models.DateField()
	
	# Foreign Key to Residence m Contacts --> 1 Residence
	
	def __str__(self):
		return ' '.join([
			self.first_name,
			self.second_name,
			self.last_name,
		])

		
class Adress(models.Model):
	contact = models.ForeignKey(Contact, null = True)
	street = models.ForeignKey(Street, null=True)
	street_number = models.IntegerField()
	
	class Meta:
		verbose_name_plural = "Adresses"
	
	def __str__(self):
		return " ".join([
			#self.street.residence.zip_code,
			#self.street.residence.residence_name, 
			#self.street.street_name,
			str(self.street_number),
		])

from mptt.models import MPTTModel, TreeForeignKey

class Asset_Category(MPTTModel):
	# f.e. license, laptop
	category_name = models.CharField(max_length=128)
	description = models.CharField(max_length=256, blank=True)

	#Foreign Keys
	parent = TreeForeignKey(u'self', null=True, blank=True, related_name="children")

	class Meta:
		verbose_name_plural = "Asset Categories"
		verbose_name = "Asset Category"

	class MPTTMeta:
		order_insertion_by = ["category_name"]

	def __str__(self):
		return self.category_name

class Asset_State(models.Model):
	# the name of the state, f.e. 'lent', 'broken', 'lost'
	state_name = models.CharField(max_length=128)
	# description of the state
	description = models.CharField(max_length=256, blank=True)

	def __str__(self):
		return self.state_name

class Asset(models.Model):
	# Table Fields
	# The vendor of the asset
	vendor = models.CharField(max_length=128, blank=True)
# TODO: make this field a Foreign Key field
	# The department that is responsible for the asset 
	department = models.CharField(max_length=128)
	
	# Next scheduled maintenance
	next_sched_maint = models.DateField(blank=True, null=True)
	# Description
	description = models.CharField(max_length=256, blank=True)
	# The date when the asset was bought
	date_acquired = models.DateField(blank=True, null=True)
	# the date when the asset was sold
	date_sold = models.DateField(blank=True, null=True)
	# the model number of the asset
	model_number = models.CharField(max_length=128, blank=True)
	# the serial number of the asset
	serial_number = models.CharField(max_length=128, blank=True)
	# the barcode of the asset
	barcode_number = models.CharField(max_length=128, blank=True)
	# the purchase price
	purchase_price = models.CharField(max_length=128, blank=True)
	# the current value
	current_value = models.CharField(max_length=128, blank=True)
	# money spent on maintenance
	total_maintenance = models.CharField(max_length=128, blank=True)
	# the annual lost in value of an asset  
	total_depreciation = models.CharField(max_length=128, blank=True)

	# Foreign Keys
	asset_category = models.ForeignKey(Asset_Category)
	# The current state of the asset, f.e. 1 = lent, 2 = reserved
	status = models.ForeignKey(Asset_State)

	def __str__(self):
		return self.vendor + " " + self.description
