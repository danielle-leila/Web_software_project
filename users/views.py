# Create your views here.
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse



def index(request):
    #return HttpResponse("Correct")
    #check if there is a user in db
    #user = User.objects.create_user('user','','user')
    user = auth.authenticate(username='useru',password='user')
    if user is not None:
        return HttpResponse("Correct")
    else:
        return HttpResponse('not correct') 
