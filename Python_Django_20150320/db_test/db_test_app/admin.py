# encoding: utf-8
from django.contrib import admin
from db_test_app.models import Contact, Residence, Adress, Street, Asset, Asset_Category, Asset_State
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'birth_date']
	list_filter = ['first_name', 'last_name']
	search_fields = ['first_name', 'last_name']
admin.site.register(Contact, ContactAdmin)

class AdressAdmin(admin.ModelAdmin):
	pass
admin.site.register(Adress, AdressAdmin)

class StreetAdmin(admin.ModelAdmin):
	pass
admin.site.register(Street, StreetAdmin)

class Asset_Cat_Admin(admin.ModelAdmin):
	pass 
admin.site.register(Asset_Category, Asset_Cat_Admin)

class Asset_Admin(admin.ModelAdmin):
	pass
admin.site.register(Asset, Asset_Admin)

class Asset_State_Admin(admin.ModelAdmin):
	pass
admin.site.register(Asset_State, Asset_State_Admin)