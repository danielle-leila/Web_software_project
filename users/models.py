from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key = True)
    loginName = models.CharField(max_length = 20, null = True)
    passwd = models.CharField(max_length = 50, null = True)
    facebookName = models.CharField(max_length = 50, null = True)
  
class Album(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    userId = models.ForeignKey(User)
  
class Photo(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    uri = models.URLField(verify_exists = True)
    AlbumId = models.ForeignKey(Album)
