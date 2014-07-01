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
	url(r'^search/', 'search_action.views.search_view'),
)
