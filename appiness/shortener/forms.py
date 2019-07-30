from django import forms
from django.core.validators import URLValidator
from .validators import validate_url,validate_dot_com



class submitURLform(forms.Form):
    url=forms.CharField(label='Submit URL',validators=[validate_url,validate_dot_com])

'''
    def clean(self):
        cleaned_data= super(submitURLform,self).clean()
        print (cleaned_data)
      #  url=cleaned_data['url']
      #  print (url)
    def clean_url(self):
        url=self.cleaned_data['url']
        if "http" in url:
            return url
        return "http://" + url
            
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("INVALID URL FOR THIS ")
        return url
  '''
