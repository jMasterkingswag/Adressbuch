import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db_test.settings')

import django
django.setup()

from adressbuch.models import *

from django.contrib.contenttypes.models import ContentType

first_names = ['Patrick', 'Jan', 'Peter', 'Hans', 'Inge', 'Anna', 'Lena', 'Heidi', 'Franz', 'Erhard', 'Dieter']
last_names = ['Meier', 'Mueller', 'Schaeferling', 'Deutinger', 'Scholz', 'Schulz', 'Berndt', 'Kahn', 'Hoffmann']

residence_objects = []

def populate(steps):
	
	# Clear everything before
	Contact.objects.all().delete()
	
	for i in range(0, steps):
		createAddress(createContact())
	
from random import randint

residences = ['Woerth', 'Bissingen', 'Erding', 'Muenchen', 'Wolfsburg', 'Hamburg']
zip_codes = ['85457', '87321', '89220', '86690', '77221', '66332']
states = ["Bayern", "Baden-Wuertemberg", "Hamburg", "Hessen", "Berlin", "Sachsen"]
streets = ['Unteranger', 'Parkstrasse', 'Leipziger Strasse', 'Freisinger Strasse', 'Hauptstrasse']

def createAddress(contact):
	
	for adr in range(0, randint(0, 10)):
		a = Adress()
		a.content_type_id = ContentType.objects.get_for_model(contact).id
		a.object_id = contact.pk
		a.city = residences[randint(0, len(residences) - 1)]
		a.zip_code = zip_codes[randint(0, len(zip_codes) - 1)]
		a.state = states[randint(0, len(states) - 1)]
		a.streets = streets[randint(0, len(streets) - 1)]
		a.save()
	print len(residence_objects)

def createContact():
	c = Contact()
	c.first_name = first_names[randint(0, len(first_names) - 1)]
	c.last_name = last_names[randint(0, len(last_names) - 1)]
	c.birth_date = "-".join([
		str((1900 + randint(50, 99))),
		str(randint(1, 12)),
		str(randint(1, 28)),
		])
	c.save()
	return c

populate(1000)