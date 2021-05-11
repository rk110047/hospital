from django.shortcuts import render,redirect
from .serializer import RegisterSerializer,LoginSerializer,PasswordChangeSerializer,SubUserSerializer
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,get_user_model,login
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import SubUser




User = get_user_model()

class LoginWithTokenAuthenticationAPIView(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   []
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        if user is not None:
            # login(user,request)
            #TOKEN STUFF
            token, _ = Token.objects.get_or_create(user = user)
            login(request,user)
            #token_expire_handler will check, if the token is expired it will generate new one
            # is_expired, token = token_expire_handler(token)     # The implementation will be described further

            return Response({ 
                'token': token.key,'username':user.username,'email':user.email,'user_id':user.id
            }, status=status.HTTP_200_OK)
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)





# #TOKEN STUFF
#     token, _ = Token.objects.get_or_create(user = user)
    
#     #token_expire_handler will check, if the token is expired it will generate new one
#     is_expired, token = token_expire_handler(token)     # The implementation will be described further
#     user_serialized = UserSerializer(user)

#     return Response({
#         'user': user_serialized.data, 
#         'expires_in': expires_in(token),
#         'token': token.key
#     }, status=HTTP_200_OK)


class RegisterAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   []
     authentication_classes =   []
     serializer_class       =   RegisterSerializer

     def post(self,request,*args,**kwargs):
        username   =   request.data.get('username')
        email      =   request.data.get('email')
        password   =   request.data.get('password')
        password1   =   request.data.get('confirm_password')
        if password==password1:
        	user       =    User.objects.create_user(username=username,password=password,email=email)
        	user       =	authenticate(username=username,password=password)
        	if user is not None:
        		token, _ = Token.objects.get_or_create(user = user)
        		return Response({ 
                'token': token.key,
            }, status=status.HTTP_200_OK)
        	return Response({'message':'invalid form'})
        return Response({'message':'invalid form'})


class PasswordChangeAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   []
     authentication_classes =   [SessionAuthentication,TokenAuthentication]
     serializer_class       =   PasswordChangeSerializer

     def post(self,request,*args,**kwargs):
        username     =   self.request.user.username
        old_password =   self.request.data.get('old_password')
        new_password =   self.request.data.get('new_password')
        user         =   authenticate(username=username,password=old_password)
        if user is not None:
            user = User.objects.get(username=username)
            print(user)
            user.set_password(new_password)
            user.save()
            user         =   authenticate(username=username,password=new_password)
            return Response({"message":"password changed"})
        return Response({"message":"authentication failed "})


class SubUserListCreateAPIView(generics.ListCreateAPIView):
     queryset               =   SubUser.objects.all()
     permission_classes     =   []
     authentication_classes =   [SessionAuthentication,TokenAuthentication]
     serializer_class       =   SubUserSerializer



     def perform_create(self,serializer):
     	user 		=		self.request.user
     	serializer.save(user=user)

     def get(self,request):
     	user 		=		self.request.user
     	query 		=		SubUser.objects.filter(user=user)
     	serialize 	=		SubUserSerializer(query,many=True)
     	return Response(serialize.data)
