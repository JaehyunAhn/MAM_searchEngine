from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

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
	(r'^images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.IMAGE_ROOT}),
)
