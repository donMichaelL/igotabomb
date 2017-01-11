from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.utils.functional import cached_property

class Bomb(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField()
    duration_starting = models.DateTimeField()
    duration_ending = models.DateTimeField()
    brange = models.IntegerField()
    image = models.ImageField(upload_to="bombs/", null=True, blank=True)
    user_change_location = models.BooleanField(default=False)
    change_location = models.BooleanField(default=False)
    stealth = models.BooleanField(default=False)
    simultaneous = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    @cached_property
    def duration(self):
        return self.duration_ending - self.duration_starting
