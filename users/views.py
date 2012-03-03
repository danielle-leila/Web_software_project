# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render_to_response


def index(request):

    return render_to_response('index.html') 

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
