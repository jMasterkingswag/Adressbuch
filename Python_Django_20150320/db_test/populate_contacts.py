import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db_test.settings')

import django
django.setup()

from db_test_app.models import Contact, Residence

first_names = ['Patrick', 'Jan', 'Peter', 'Hans', 'Inge', 'Anna', 'Lena', 'Heidi', 'Franz', 'Erhard', 'Dieter']
last_names = ['Meier', 'Mueller', 'Schaeferling', 'Deutinger', 'Scholz', 'Schulz', 'Berndt', 'Kahn', 'Hoffmann']

residence_objects = []

def populate(steps):
	
	# Clear everything before
	Contact.objects.all().delete()
	Residence.objects.all().delete()
	
	createResidences()
	
	for i in range(0, steps):
		createContact()
	
from random import randint

residences = ['Woerth', 'Bissingen', 'Erding', 'Muenchen', 'Wolfsburg', 'Hamburg']
zip_codes = ['85457', '87321', '89220', '86690', '77221', '66332']

def createResidences():
	
	for res in range(0, len(residences) - 1):
		r = Residence()
		r.residence_name = residences[res]
		r.zip_code = zip_codes[res]
		residence_objects.append(r)
		r.save()
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
	c.email = c.first_name + "." + c.last_name + "@googlemail.com"
	c.residence = residence_objects[randint(0,len(residence_objects)-1)]
	c.save()

populate(1000)