from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseServerError

from adressbuch.models import *
from adressbuch.forms import *

def create(request, template = "adressbuch/contact/create.html"):

	# get the information about the user who wants to create a contact
	user = request.user
	
	""" 
	# TODO: implement permissions
	if not user.has_perm('add_person'):
		return HttpResponseForbidden()
	"""

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

			return HttpResponseRedirect(reverse('show_contact'))
	else:
		contact_form = ContactForm(user=request.user)
		adress_formset = AdressFormSet(prefix='form-control')

	return render(request, template,
			{
				'contact_form': contact_form,
				'adress_formset': adress_formset,	
			})

def show(request, page=1, template="adressbuch/contact/list.html"):
	"""
	:param page: The current page of the contacts-paginator
	"""
	print "Hi"
	# get all contacts into a list
	contact_list = Contact.objects.all()
	# use a paginator to only show a page of 20 elements of the list
	paginator = Paginator(contact_list, 20)
	# try to get the current page
	try:
		contacts = paginator.page(page)
	# show last page if page has no elements or is invalid
	except (EmptyPage, InvalidPage):
		contacts = paginator.page(paginator.num_pages)
	# fill kwargs with information from the paginator like if the page has a previous
	kwargs = {
		'object_list': contacts.object_list,
		'has_next': contacts.has_next(),
		'has_previous': contacts.has_previous(),
		'has_other_pages': contacts.has_other_pages(),
		'start_index': contacts.start_index(),
		'end_index': contacts.end_index(),
		'current_page': page,
	}
	# try to add the previous page number if it exists
	try:
		kwargs['previous_page_number'] = contacts.previous_page_number()
	except(EmptyPage, InvalidPage):
		kwargs['previous_page_number'] = None

	# try to add the next page number if it exists
	try:
		kwargs['next_page_number'] = contacts.next_page_number()
	except(EmptyPage, InvalidPage):
		kwargs['next_page_number'] = None

	return render(request, template, kwargs)

def update(request, pk, template="adressbuch/contact/update.html"):
	# get the information about the user who wants to update a contact
	#user = request.user
	
	""" 
	# TODO: implement permissions
	if not user.has_perm('add_person'):
		return HttpResponseForbidden()
	"""
	# check if contact with private_key = pk exists
	try:
		contact = Contact.objects.get(pk=pk)
	except contact.DoesNotExist:
		raise Http404

	if request.method == "POST":
		contact_form = ContactForm(request.POST, instance=contact)
		adress_formset = AdressFormSet(request.POST, instance=contact) 

		if contact_form.is_valid() and adress_formset.is_valid():
			contact_form.save()
			adress_formset.save()

			return HttpResponseRedirect('show')
		else:
			return HttpResponseServerError
	else:
		contact_form = ContactForm(instance=contact)
		adress_formset = AdressFormSet(instance=contact)

		kwvars = {
			'contact_form': contact_form,
			'adress_formset': adress_formset,
		}

	return render(request, template, kwvars)

def delete(request, pk):	
	pass