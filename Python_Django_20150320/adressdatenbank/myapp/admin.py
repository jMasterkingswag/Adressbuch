from django.contrib import admin
from myapp.models import Category, Page, UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	#print 'lala'
admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
	
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)