
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import profile
from .healpers import *


class LoginView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data=request.data

            if data.get('username') is None:
                response['message']='Key username not found'
                raise Exception('Key username not found')
            if data.get('password') is None:
                response['message']='Key password not found'
                raise Exception('Key password not found')
        
            cheak_user=User.objects.filter(username=data.get('username')).first()
            if cheak_user is None:
                response['message']='Invalid User name'
                raise Exception('Invalid User name')
            if not profile.objects.filter(user=cheak_user).first().is_varified:
                response['message']='Your profilr is not verified'
                raise Exception('Profile not varified')
            user_obj=authenticate(username=data.get('username'),password=data.get('password'))
            if user_obj :
               login(request,user_obj) 
               response['status']=200
               response['message']='Welcome'
            else:
                response['message']='Invalid password'
                raise Exception('Invalid password') 

        except Exception as e:
            print(e)
                
        return Response(response)


loginView =LoginView.as_view()


class RegisterView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data=request.data

            if data.get('username') is None:
                response['message']='Key username not found'
                raise Exception('Key username not found')
            if data.get('password') is None:
                response['message']='Key password not found'
                raise Exception('Key password not found')
        
            cheak_user=User.objects.filter(username=data.get('username')).first()
            if cheak_user:
                response['message']='Username already taken'
                raise Exception('Username already taken')
            user_obj=User.objects.create(email=data.get('username'),username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token=geenreate_randomstring(20)
            profile.objects.create(user=user_obj,token=token)
            #send_mail_to_user(token,data.get('username'))
            response['message']='User created '
            response['status']=200


        except Exception as e:
            print(e)
                
        return Response(response)


registerView=RegisterView.as_view()


