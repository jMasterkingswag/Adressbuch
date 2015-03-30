from django import forms
from db_test_app.models import Contact, Residence, Street, Adress

class StreetForm(forms.ModelForm):
	
	street_name = forms.CharField(max_length=128)
	
	class Meta:
		model = Street
		fields = ('street_name',)
		
class ContactForm(forms.ModelForm):
	
	class Meta:
		model = Contact
		fields = ('first_name', 'second_name','last_name', 'email', 'birth_date',)
		
class ResidenceForm(forms.ModelForm):
	
	residence_name = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder':'Enter the name',
			}
		)
	)
	
	zip_code = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder':'Enter the Zip Code',
			}
		)
	)
	
	name_adding = forms.CharField(
		widget = forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder':'Name Adding',
			}
		)
	)
	
	class Meta:
		model = Residence
		fields = ('residence_name', 'zip_code', 'name_adding',)
		
class AdressForm(forms.ModelForm):

	street_name  = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'input-xlarge'}))

	class Meta:
		model = Adress
		fields = ('street_name',)
		
from db_test_app.models import Asset

class AssetForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
		
	class Meta:
		model = Asset