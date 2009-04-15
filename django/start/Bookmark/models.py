from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    command = models.CharField(max_length=100)
    url = models.URLField(max_length=300)

    def __unicode__(self):
        return self.url

    class Admin:
        pass
