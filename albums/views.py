# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from album.models import *

def user(request):
	is_auth = request.user.is_authenticated()
	albums = Album.objects.get(userId=request.user)
	return render_to_response('user.html',{'is_auth':is_auth, 'user':request.user, 'albums':albums})

def create(request, albumTitle):
	is_auth = request.user.is_authenticated()
	if (is_auth):
		album = new Album(title=request.albumTitle, description=none, userId=request.user)
		album.save()
		return render_to_response('create.html', {'is_auth':is_auth, 'user':request.user, 'title':albumTitle})
	elif:
		return render_to_response('login.html',{'is_auth':is_auth})
	

def album(request, album):
	is_auth = request.user.is_authenticated()
	if (is_auth):
		photos = Photo.objects.get(albumId = album)
		return render_to_response('album.html', {'is_auth':is_auth, 'user':request.user, 'photos':photo, 'album':album})
	elif:
		return render_to_response('login.html',{'is_auth':is_auth})

def add(request, photoName, photoDescription, album):
	is_auth = request.user.is_authenticated()
	if (is_auth):
		photo = new Photo(title=photoName, description=photoDescription, userId=request.user, albumId=album)
		photo.save()
		return render_to_response('create.html', {'is_auth':is_auth, 'user':request.user, 'title':photoName, 'description':photoDescription})
	elif:
		return render_to_response('login.html',{'is_auth':is_auth})
