from django.conf.urls import patterns, url

urlpatterns = patterns('adressbuch.views',
	#url(r'^$', 'index', name='adressbuch_index'),
	#url(r'^contact/add$', 'add_contact', name='add_contact'),
	#url(r'^contact/(?P<contact_id>[\d\-]+)/$', 'single_contact', name='single_contact'),
	url(r'^create/$', 'contact.create', name = 'create_contact'),
	url(r'^show/$', 'contact.show', name = 'show_contact'),
	url(r'^show/(?P<page>\d{1,})+/$', 'contact.show', name = 'show_contact'),
	url(r'^show/(?P<search>\w+)/$', 'contact.show', name = 'show_contact'),
	url(r'^show/(?P<search>\w+)/(?P<page>\d{1,})/$', 'contact.show', name = 'show_contact'),
	url(r'^update/(?P<pk>\d{1,})+/$', 'contact.update', name = 'update_contact'),
	url(r'^detail/(?P<pk>\d{1,})+/$', 'contact.detail', name = 'contact_detail'),
	url(r'^delete/(?P<pk>\d{1,})+/$', 'contact.delete', name = 'delete_contact'),
)