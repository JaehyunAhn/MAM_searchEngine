from django.conf.urls import patterns, include, url

from django.contrib import admin
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
	url(r'^upload_pic/$', 'search_action.views.upload_pic', name="upload_pic"),
)
