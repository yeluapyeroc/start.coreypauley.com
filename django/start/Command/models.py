from django.db import models

class Basic(models.Model):
    command = models.CharField(max_length=100)
    default = models.CharField(max_length=500)
    header1 = models.CharField(max_length=500, blank=True)
    header2 = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.command

    class Admin:
        pass

    class Meta:
        verbose_name = "basic command"
        verbose_name_plural = "basic commands"

class Advanced(models.Model):
    name = models.CharField(max_length=200)
    command = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        verbose_name = "advanced command"
        verbose_name_plural = "advanced commands"
