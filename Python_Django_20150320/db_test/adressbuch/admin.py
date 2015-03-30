from django.contrib import admin
from adressbuch.models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	pass

admin.site.register(Contact, ContactAdmin)

class AdressAdmin(admin.ModelAdmin):
	pass

admin.site.register(Adress, AdressAdmin)