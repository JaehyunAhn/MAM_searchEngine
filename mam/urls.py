from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os.path
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), '../site_media'
)

urlpatterns = patterns('',
    # url patterns    
    url(r'^$', 'search_mam.views.home'),
    url(r'^genSearch/$','search_action.views.searchView'),
    url(r'^loginSearch/$','search_mam.views.loginView'),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'search_mam.views.login_user'),
	url(r'^logout/', 'search_mam.views.logout_user'),
	url(r'^register/', 'search_mam.views.register_user'),
	url(r'^register_req/', 'search_mam.views.register_req'),
	url(r'^search/$', 'search_action.views.searchView'),
	url(r'^searchImage/$', 'search_action.views.imageSearch'),
	url(r'^searchText/$', 'search_action.views.textSearch'),
	url(r'^searchMovie/$', 'search_action.views.movieSearch'),
	url(r'^searchIntegrated/$', 'search_action.views.intgSearch'),
	url(r'^upload_image/$', 'search_action.views.upload_image', name='upload_image'),
	url(r'^upload_media/$', 'search_action.views.upload_media', name='upload_media'),
	# Show Image
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',
        { 'document_root':site_media,}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.IMAGE_ROOT}),
)
