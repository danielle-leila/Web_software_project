from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django_openid_auth import views
import albums
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
      url(u'^index/$', 'albums.views.index'),
      (r'^login/$', 'albums.views.login'),
     (r'^albums/$', 'albums.views.album_list'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^private/$', 'albums.views.require_authentication'),

    #(r'^openid/', include('django_openid_auth.urls')),
   # url(r'^openid/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
  #  url(r'^openid/complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
   # url(r'^openid/logo.gif$', 'django_openid_auth.views.logo', name='openid-logo'),

)
