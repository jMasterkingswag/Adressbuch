
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

from adressbuch.forms import *
from adressbuch.models import *
# Create your views here.

def add_contact(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST, user=request.user)
		adress_formset = AdressFormSet(request.POST, prefix="form-control")

		if(contact_form.is_valid() and adress_formset.is_valid()):
			# Create new contact
			contact = contact_form.save()
			# iterate over each entered adress and save it
			for form in adress_formset:
				adress = form.save(commit = False)
				# set the foreign key of the adress to the new contact
				adress.contact = contact
				adress.save()

			return HttpResponseRedirect(reverse('adressbuch_index'))
	else:
		contact_form = ContactForm(user=request.user)
		adress_formset = AdressFormSet(prefix='form-control')

	return render(request, 'adressbuch/add_contact.html',
			{
				'contact_form': contact_form,
				'adress_formset': adress_formset,	
			})

def index(request):
	req_dict = {'contacts': Contact.objects.all(),}
	return render(request, 'adressbuch/index.html', req_dict)

def single_contact(request, contact_id):
	contact = Contact.objects.get(pk = contact_id)

	adresses = Adress.objects.filter(contact = contact)
	print adresses
	if contact != None:
		return render(request, 'adressbuch/single_contact.html', {'contact':contact, 'adresses': adresses})
	else:
		return HttpResponseRedirect(reverse('adressbuch_index'))
