from django import forms
from django.forms import ModelForm, Form
from django.contrib.contenttypes.generic import generic_inlineformset_factory as inlineformset_factory

from adressbuch.models import *

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ()
    
    def __init__(self, *pa, **ka):
        user = ka.pop('user')
        super(ContactForm, self).__init__(*pa, **ka)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
   
class ContactUpdateForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ()
    
    def __init__(self, *pa, **ka):
        super(ContactUpdateForm, self).__init__(*pa, **ka)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

AdressFormSet = inlineformset_factory(Adress, extra=1)