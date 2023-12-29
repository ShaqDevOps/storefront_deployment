from django.shortcuts import render
from djoser.views import *
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from core.serializers import UserCreateSerializer, UserSerializer
# from django.views.generic import TemplateView

# class CustomUserCreateView(GenericViewSet,CreateModelMixin):
#     serializer_class = UserCreateSerializer



# class UserProfileView(TemplateView):
#     # serializer_class = UserSerializer
#     template_name = 'core/profile.html'

#     def get_object(self):
#         return self.request.user  # Retrieve the currently authenticated user

def signInView(request):
    return render(request, 'core/signIn.html')

def signUpView(request):
    return render(request, 'core/signUp.html')
