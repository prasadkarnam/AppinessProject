import random
import string
from django.conf import settings

SHORTCODE_MIN=getattr(settings,"SHORTCODE_MIN",6)
def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
#    new_code=''
#   for _ in range(size):
#      new_code+=random.choice(chars)
#  return new_code
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code=code_generator(size=size)
    print (instance)
    print (instance.__class__)
    print (instance.__class__.__name__)
    Mclass=instance.__class__   # inherting the Model class
    sc_exists=Mclass.objects.filter(shortcode=new_code).exists()  #True or False
    if sc_exists:
        return create_shortcode(size=size)
    return new_code