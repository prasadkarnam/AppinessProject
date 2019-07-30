from django.db import models

from shortener.models import appinessURL
#from shortener import models



# Create your models here.
print ("Hello Prasad")

class ClickEventManager(models.Manager):
    def create_event(self, appinessInstance):
        if isinstance(appinessInstance,appinessURL):
            obj, created = self.get_or_create(appiness_URL=appinessInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):

    appiness_URL = models.OneToOneField(appinessURL,on_delete=None)
    print ("The URL name is ", appiness_URL)
    count = models.IntegerField(default=0)

    objects = ClickEventManager()

    def __str__(self):
        return "The count is {i}".format(i=self.count)
