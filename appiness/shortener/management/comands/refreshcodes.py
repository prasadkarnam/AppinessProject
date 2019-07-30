from django.core.management.base import BaseCommand,CommandError

from shortener.models import appinessURL

class Command(BaseCommand):
    help ='refeshing appiness short codes'

    def handle(self,*args,**kwargs):
        return appinessURL.objects.refresh_shortcodes()