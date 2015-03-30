from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

from adressbuch.forms import *
from adressbuch.models import *

def single_contact(request, contact_id):
	contact = Contact.objects.get(pk = contact_id)

	adresses = Adress.objects.filter(contact = contact)
	print adresses
	if contact != None:
		return render(request, 'adressbuch/single_contact.html', {'contact':contact, 'adresses': adresses})
	else:
		return HttpResponseRedirect(reverse('adressbuch_index'))

