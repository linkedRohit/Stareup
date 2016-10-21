from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
  title = models.CharField('title', max_length=200)
  desc = models.TextField('desc', max_length=1000, blank=True)
  #email = models.EmailField('Email', blank=True)
  #headshot = models.ImageField(upload_to='img', blank=True)
  
  def __str__(self):
    return '%s' % (self.name)
