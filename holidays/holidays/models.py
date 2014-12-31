from django.db import models
from django.contrib.auth.models import User


class Holiday(models.Model):
    user = models.ForeignKey(User, related_name="holidays")
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.NullBooleanField(default=None)
    approved_by = models.ForeignKey(User, null=True, blank=True)
    
    def __unicode__(self):
        return "Holiday for %s: %s - %s" % (self.user, self.start_date, self.end_date)