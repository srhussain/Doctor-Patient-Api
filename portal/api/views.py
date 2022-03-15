from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            # email=data.get('email')
            # password=data.get('password')
            if serializer.is_valid():
                username=serializer.data['username']
                password=serializer.data['password']
                user = authenticate(request,username=username, password=password)
                if user is None:
                    return Response({
                        'status':404,
                        'message':'Invalid Password',
                        'data':{}
                    })

                # if user.is_email_verified is False:
                #     return Response({
                #         'status':404,
                #         'message':'Your account is not Verified ',
                #         'data':{}
                #     })


                refresh=RefreshToken.for_user(user)
                users=User.objects.filter(username=username).first()
                return Response({
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                    'email':users.email,
                    'username':users.username,
                    'city':users.city,
                    'first_name':users.first_name,
                    'line1':users.line1,
                    'state':users.state,
                    'city':users.city,
                    'pincode':users.pincode,
                    'is_patient':users.is_patient,
                    'is_doctor':users.is_doctor


                })


            return Response({
                'status':404,
                'message':'something went wrong',
                'data':serializer.errors
            })


        except Exception as e:
                print(e)
                return Response({
                    'status':404,
                    'error':'something went wrong'
                })




class RegisterView(APIView):

    def post(self,request):
        try:
            password =request.data['password']
            confirm_password=request.data['confirm_password']
            if password!=confirm_password:
                return Response({
                    'status':404,
                    'message':'Both Password are Wrong'

                })
            serializer=UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status':403,
                    'errors':serializer.errors

                })
            serializer.save()
            return Response({
                'status':200,
                'message':'Successfully Registered'
            })

        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'error':'something went wrong'
            })
