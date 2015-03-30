from django.conf.urls import patterns, include, url
from django.contrib import admin
from db_test_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'db_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^createContact', views.createContact, name="createContact"),
	url(r'^addAdress/(?P<contact_id>[\w\-]+)/$', views.createAdress),
	url(r'^createResidence', views.createResidence, name="addResidence"),
	# Assets
	url(r'^createAsset', views.createAsset, name="createAsset"),
	url(r'^showCategories', views.showCategories, name="showCategories"),
	url(r'^Categories/(?P<category>[\w\-]+)/$', views.showAssets, name="showAssets"),
	url(r'^assetDetail/(?P<asset>[\d\-]+)/$', views.asset_detail, name="assetDetail"),
)
