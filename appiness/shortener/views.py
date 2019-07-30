from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .forms import submitURLform
from .models import appinessURL



# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method == 'POST':
        print (request.POST)
        return  render(request,"shortener/home.html",{})

class homeview(View):
    def get(self,request,*args,**kwargs):
        the_form=submitURLform()
        context = {
            "title": "Hello  Appiness",
            "form": the_form
        }
        return render(request,"shortener/home.html", context)
    def post(self,request,*args,**kwargs):

        form=submitURLform(request.POST)
        context = {
            "title": "Submit URL",
            "form": form
        }
        template="shortener/home.html"

        if form.is_valid():

            new_url=form.cleaned_data.get("url")
            obj,created=appinessURL.objects.get_or_create(url=new_url)
            context={
                "object":obj,
                "created":created,
            }
            if created:
                template= "shortener/success.html"
            else:
                template= "shortener/already-exists.html"


        return render(request,template,context)

'''def appiness_view(request, shortcode=None,*args,**kwargs): #function based view #POST
    print (args)
    print (kwargs)
    print (shortcode)
  #  obj=appinessURL.objects.get(shortcode=shortcode)

    obj=get_object_or_404(appinessURL,shortcode=shortcode)
  #  obj_url=obj.url
  #  try:
  #    obj = appinessURL.objects.get(shortcode=shortcode)
  # except:
  #      obj = appinessURL.objects.all().first()


   # obj_url=None
   # qs=appinessURL.objects.filter(shortcode__iexact=shortcode.upper())
   # if qs.exists() and qs.count() == 1:
   #     obj=qs.first()
   #     obj_url=obj.url

   # return HttpResponse("Hey! Appiness your short code is {sc}".format(sc=obj.url))
    return HttpResponseRedirect(obj.url)
'''
class URLredirectview(View): #class based view   #GET
    def get(self,request,shortcode=None,*args,**kwargs):
     #   return  HttpResponse("Hey! Appiness your one more short code is {sc}".format(sc=shortcode))
        qs=appinessURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() !=1 and not qs.exists():
            raise Http404
        obj=qs.first()

        return HttpResponseRedirect(obj.url)

    def post(self,request,*args,**kwargs):
        return HttpResponse