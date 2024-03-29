# Create your views here.
from albums.models import *
from django.django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from albums.models import Photo
from models import Album






def user(request):
	is_auth = request.user.is_authenticated()
	albums = Album.objects.get(userId=request.user)
	return render_to_response('user.html',{'is_auth':is_auth, 'user':request.user, 'albums':albums})

def create(request, albumTitle):
	is_auth = request.user.is_authenticated()
	if (is_auth):
		album = Album(title=request.albumTitle, description=none, userId=request.user)
		album.save()
		return render_to_response('create.html', {'is_auth':is_auth, 'user':request.user, 'title':albumTitle})
	else:
		return render_to_response('login.html',{'is_auth':is_auth})
	

def album(request, album):
	is_auth = request.user.is_authenticated()
	if (is_auth):
		photos = Photo.objects.get(albumId = album)
		return render_to_response('album.html', {'is_auth':is_auth, 'user':request.user, 'photos':photo, 'album':album})
	else:
		return render_to_response('login.html',{'is_auth':is_auth})

def add(request, photoName, photoDescription, album):
	is_auth = request.user.is_authenticated()
	if (is_auth):
		photo = Photo(title=photoName, description=photoDescription, userId=request.user, albumId=album)
		photo.save()
		return render_to_response('create.html', {'is_auth':is_auth, 'user':request.user, 'title':photoName, 'description':photoDescription})
	else:
		return render_to_response('login.html',{'is_auth':is_auth})



def do_login(request, user):
    pass


def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))

		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('album_list'))

	return login(request, template_name='index.html')

def album_list(request):
    return render_to_response('albums.html')


def login2(request):
    #return HttpResponse("Correct")
    #check if there is a user in db
    #user = User.objects.create_user('user','','user')
    #user = auth.authenticate(username='useru',password='user')
    #if user is not None:
    #else:
    #   return HttpResponse('not correct')

    return render_to_response('login.html')


def login(request):
    s = ['<p>']
    is_auth = request.user.is_authenticated()
    return render_to_response('login.html',{'is_auth':is_auth})


def next_works(request):
    return HttpResponse('?next= bit works. <a href="/">Home</a>')


@login_required
def require_authentication(request):
    return HttpResponse('This page requires authentication')

@login_required
def logout(request, **kwargs):
	return logout_then_login(request)

