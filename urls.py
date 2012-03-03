from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django_openid_auth import views
import users
from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PhotoAlbum.views.home', name='home'),
    # url(r'^PhotoAlbum/', include('PhotoAlbum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
      url(u'^$', 'users.views.index'),
      (r'^login/$', 'users.views.login'),
    # (r'^openid/', include('django_openid_auth.urls')),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^private/$', 'views.require_authentication'),

    url(r'^openid/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^openid/complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^openid/logo.gif$', 'django_openid_auth.views.logo', name='openid-logo'),

)
