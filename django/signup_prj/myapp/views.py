from django.shortcuts import render
# from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from rest_framework import status
from django.db import models
from .service import user_validation
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer,CustomUserSerializer,EmailVerifySerializer
from .models import CustomUser
from django.contrib.auth import authenticate, login
from .email import *
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class=CustomUserSerializer

#     print(serializer_class)
#     def post(self,request,*args,**kwargs):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class SignupAPI(APIView):
    def post(self,request,*args,**kwargs):

        print("------------------")

        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

                serializer.save()

                return Response({"status":200,"message":"Data saved succesfully"})

        else:

                return Response({"status":400,"message":"Data Invalid"})
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({"status":200,"message":"Data saved succesfully"})
    

class LoginAPI(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        print('phn--',email)
        print('pass--',password)
        flag=user_validation(email,password)
        print("''''''''''''''''''",flag)
        if flag==True:
            return Response({"status":200,"error":False,"message":"logged in successfully"})
        else:
            return Response({"status":400,"error":False,"message":"Invalid credentials"})


class Emailotp(APIView):
    def post(self,request):
        # try:
            data= request.data

            print("the data of retspai is -------------->",data)
            serializer= CustomUserSerializer(data=data)
            # print("the data of serialzizer is -------------->",serializer)
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message':'Succesfully otp send',
                    'data': serializer.data
                })
            
            return Response({
                    'status': 400,
                    'message':'Invalid Email',
                    'data': serializer.errors
                })
        
        # except Exception as e:
        #     # print(e)
        #     return Response({
        #             'status': 400,
        #             'message':'Invalid expect'
                    
        #         })

class VerifyOTP(APIView): 
    def post(self,request): 
            data=request.data 
            print("------------",data)
            serializer=EmailVerifySerializer(data=data) 

            # print("---------------->",serializer.data)
            if serializer.is_valid(): 
                email=serializer.data['email'] 
                otp=serializer.data['otp'] 

                print("email --------------------->",email)
                print("--------------------->",otp)
                user=CustomUser.objects.filter(email=email) 
                print("------------------>",user) 
                if not user.exists(): 
                    return Response({
                        'status': 400, 'message': 
                        'something went wrong', 
                        'data' : 'invalid email'
                        }) 
                print("------------------- user ",user[0].otp) 
                if not user[0].otp == otp: 
                    return Response({
                        'status': 400,
                        'message': 'something went wrong',
                          'data': 'Wrong Otp'
                          }) 
                user=user.first() 
                user.verify=True 
                user.save() 
                return Response({
                    'status': 200,
                    'message': 'Account Verified',
                    'data': {}}) 
            return Response({'status': 400, 
                             'message': 'something went wrong', 
                             'data': serializer.errors}) 