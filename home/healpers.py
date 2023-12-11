from django.utils.text import slugify



import string
import random



def geenreate_randomstring(N):
    res=''.join(random.choices(string.ascii_uppercase+string.digits,k=N))
    return res

def generateslug(text):
    new_slug=slugify(text)
    from home.models import BlogModel
    if BlogModel.objects.filter(slug=new_slug).exists():
       return generateslug(text+geenreate_randomstring(5))
    return new_slug

from django.conf import settings
from django.core.mail import send_mail

def send_mail_to_user(token,email):
    subject=f"Your accounts need to be varified"
    message=f"Hii pase the link to verify account http://127.0.0.1:8000/verify/{token}".format
    email_form=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_form,recipient_list)
    return True