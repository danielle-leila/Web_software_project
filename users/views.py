# Create your views here.
from django.django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.utils.html import escape
from django.shortcuts import render_to_response
from users.models import Album


def do_login(request, user):
    pass


def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))

	if request.method == 'POST' and request.POST.get('action') == 'register':
		regform = UserCreationForm(request.POST)
		if not regform.is_valid():
			return render_to_response('index.html', {'regform': regform}, context_instance=RequestContext(request))

		username = regform.cleaned_data['username']
		password = regform.cleaned_data['password1']
		regform.save()

		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('album_list'))

	return login(request, template_name='index.html')
   # return render_to_response('index.html')

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

    #    s.append('You are signed in as <strong>%s</strong> (%s)' % (
     #           escape(request.user.username),
     #           escape(request.user.get_full_name())))
      #  s.append(' | <a href="/logout">Sign out</a>')

       # s.append('<a href="/openid/login">Sign in with OpenID</a>')

    #s.append('</p>')

    #s.append('<p><a href="/private">This requires authentication</a></p>')
    return render_to_response('login.html',{'is_auth':is_auth})


def next_works(request):
    return HttpResponse('?next= bit works. <a href="/">Home</a>')


@login_required
def require_authentication(request):
    return HttpResponse('This page requires authentication')

@login_required
def logout(request, **kwargs):
	return logout_then_login(request)

