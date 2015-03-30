from django.db import models

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation
# Create your models here.
class Contact(models.Model):
	
	first_name = models.CharField(max_length = 50, blank = False)
	second_name = models.CharField(max_length = 50, blank = True)
	last_name = models.CharField(max_length = 50, blank = False)
	birth_date = models.DateField(blank = True)
	title = models.CharField(max_length = 40, blank=True)
	organisation = models.CharField(max_length = 100, blank = True)

	address = GenericRelation('Adress')

	def __unicode__(self):
		if self.second_name != "":
			return "%s %s %s" % (self.first_name, self.second_name, self.last_name)
		return "%s %s" % (self.first_name, self.last_name)

class Adress(models.Model):

	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'app_label': 'adressbuch'})

	object_id = models.IntegerField(db_index=True)
	content_object = generic.GenericForeignKey()

	contact = models.ForeignKey(Contact, related_name='adressen')
	street = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	zip_code = models.CharField(max_length = 10)

	def __unicode__(self):
		return "a"

	class Meta:
		verbose_name_plural = "Adresses"