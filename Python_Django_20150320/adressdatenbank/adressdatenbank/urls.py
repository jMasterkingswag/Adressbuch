from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adressdatenbank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^myapp/', include('myapp.urls')),
	(r'^accounts/', include('registration.backends.simple.urls')), # @django-registration-redux
)

from django.conf import settings
from django.conf.urls.static import static

if not settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)