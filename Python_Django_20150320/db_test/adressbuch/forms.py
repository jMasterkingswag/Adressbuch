from django import forms
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.contrib.contenttypes.generic import generic_inlineformset_factory as inlineformset_factory

from adressbuch.models import *
"""
class RequiredFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
"""
class ContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ()
    """
    def __init__(self, *pa, **ka):
        #user = ka.pop('user')
        super(ContactForm, self).__init__(*pa, **ka)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    """
class AdressForm(ModelForm):

    class Meta:
        model = Adress
        fields = ('street','city','state','zip_code')
    """
    def __init__(self, instance, *pa, **ka):
        super(AdressForm, self).__init__(*pa, **ka)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    """
AdressFormSet = inlineformset_factory(Adress, extra="1")