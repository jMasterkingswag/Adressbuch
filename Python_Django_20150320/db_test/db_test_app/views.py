from django.shortcuts import render, redirect
from db_test_app.models import Contact, Residence, Street, Adress, Asset_Category, Asset
from django.http import HttpResponse
# Create your views here.
from db_test_app.forms import ContactForm, AdressForm, ResidenceForm, StreetForm, AssetForm
def createContact(request):
	if request.method == "POST":
		
		contactForm = ContactForm(data = request.POST)
		residenceForm = ResidenceForm(data = request.POST)
		streetForm = StreetForm(data = request.POST)
		adressForm = AdressForm(data = request.POST)
		streetForm = StreetForm(data = request.POST)
		
		if contactForm.is_valid and residenceForm.is_valid and streetForm.is_valid and adressForm.is_valid:
			c = contactForm.save()
			c.save()
			print c + " saved"
		
			r = residenceForm.save()
			r.save()
			
			s = streetForm.save()
			s.save()
			
			a = adressForm.save()
			a.save()
			
		else:
			print contactForm.errors + residenceForm.errors + streetForm.errors + adressForm.errors
			
	else:
		contextDict = {
			'contactForm' : ContactForm(),
			'residenceForm' : ResidenceForm(),
			'streetForm' : StreetForm(),
			'adressForm' : AdressForm(),
			'streetForm' : StreetForm(),
		}
		
		
	return render(request, 'db_test_app/create_contact.html', contextDict)

from django.forms.models import inlineformset_factory	
	
def createAdress(request, contact_id):
	
	AdressFormSet = inlineformset_factory(Street, Adress, fk_name='contact', fields=('street', 'street_number'))
	
	street = (Contact.objects.filter(first_name = contact_id))[0]
	formset = AdressFormSet(instance = contact)
	
	return render(request, "db_test_app/addAdress.html", { 'formset': formset })
	
def createResidence(request):
	if request.method == "POST":
		residenceForm = ResidenceForm(data = request.POST)
		if residenceForm.is_valid:
			residence = residenceForm.save()
			print "saving Residence: " + str(residence)
			residence.save()
			return HttpResponse("Thank you for adding residence!")
		else:
			print residenceForm.errors
	else:
		residenceForm = ResidenceForm()
	return render(request, 'db_test_app/addResidence.html', { 'residenceForm': residenceForm })

def createAsset(request):
	if request.method == "POST":
		assetForm = AssetForm(data = request.POST)
		if assetForm.is_valid:
			asset = assetForm.save()
			asset.save()
			return HttpResponse("everything worked fine")
		else:
			print assetForm.errors
	else:
		assetForm = AssetForm()
	return render(request, 'db_test_app/createAsset.html', {'assetForm': assetForm})
		
from django.db.models import Count

def showCategories(request):
	categories = Asset_Category.objects.all().annotate(Count('asset'))
	return render(request, 'db_test_app/showCategories.html', {'categories':categories})
		
def showAssets(request, category, search=None):
	if search == None:
		categories = Asset_Category.objects.filter(category_name = category)
		assets = Asset.objects.all().filter(asset_category = categories[0])		
	return render(request, 'db_test_app/showAssets.html', {'assets': assets})	
		
def asset_detail(request, asset):
	asset = Asset.objects.get(pk = asset)
	return render(request, 'db_test_app/asset_detail.html', {'asset': asset})		
		