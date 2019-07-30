from django.db import models
from .utils import code_generator,create_shortcode
from django.conf import settings
from .validators import validate_url,validate_dot_com
# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse

SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX",15)

# Create your models here.

class appinessURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main=super(appinessURLManager,self).all(*args,**kwargs)
        qs=qs_main.filter(active=True)
        return qs
    def refresh_shortcodes(self):
        qs=appinessURL.objects.filter(id__gte=1)
        new_codes=0
        for q in qs:
            #if q.shortcode='abc': - to put the sortcode as unique
            q.shortcode=create_shortcode(q)
            print (q.shortcode)
            q.save()
            new_codes+=1
        return "new codes made{i}".format(i=new_codes)

    def get_or_create(self, defaults=None, **kwargs):
        search_url = kwargs.get('url')
        if search_url is not None:
            if not 'http' in kwargs['url']:
                kwargs['url'] = 'http://' + kwargs['url']
        return super().get_or_create(defaults, **kwargs)

class appinessURL(models.Model):
    url=models.CharField(max_length=1000,validators=[validate_url,validate_dot_com])
    shortcode=models.CharField(max_length=SHORTCODE_MAX, unique=True,blank=True,)
    updated=models.DateTimeField(auto_now=True,)
    active=models.BooleanField(default=True)
    #timestamp = models.DateTimeField(auto_now_add=True,)
    objects=appinessURLManager()

    def save(self,*args,**kwargs):
        print ("Hello! Appiness")
        if self.shortcode is None or self.shortcode == " ":
            #self.shortcode=code_generator()
            self.shortcode =create_shortcode(self)
        if not "http" in self.url:
            self.url="http://" + self.url
        super(appinessURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)


    def get_short_url(self):
        url_path = reverse("sccode",kwargs = {'shortcode':self.shortcode}, host ='www',scheme='http')
        return url_path
'''
#  return "http://google.com/{shortcode}".format(shortcode=self.shortcode)
'''