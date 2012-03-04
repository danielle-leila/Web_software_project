from django.db import models
from django.core.urlresolvers import reverse


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
    stamp_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
		return reverse('album_view', args=[self.id])

class Photo(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    uri = models.URLField(verify_exists = True)
    AlbumId = models.ForeignKey(Album)

#
class Template(models.Model):
	name = models.CharField(max_length=32)
	image_slots = models.IntegerField()
	text_slots = models.IntegerField()
#
class Page(models.Model):
	album = models.ForeignKey('Album', db_index=True)
	template = models.ForeignKey(Template)
	rank = models.IntegerField()
