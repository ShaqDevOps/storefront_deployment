from django.shortcuts import render
from djoser.views import *
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin
from core.serializers import UserCreateSerializer, UserSerializer
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import CustomUserCreationSerializer

# from django.views.generic import TemplateView

# class CustomUserCreateView(GenericViewSet,CreateModelMixin):
#     serializer_class = UserCreateSerializer



# class UserProfileView(TemplateView):
#     # serializer_class = UserSerializer
#     template_name = 'core/profile.html'

#     def get_object(self):
#         return self.request.user  # Retrieve the currently authenticated user

# class SignUpView(ModelViewSet):
#     def 
#         if request.method == 'POST':
#             form = CustomUserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # After saving, you can redirect the user or perform other actions
#                 print(form)
#                 return redirect('/')
#         else:
#             form = CustomUserCreationForm()

#         return render(request, 'core/signUp.html', {'form': form})




User = get_user_model()

class SignUpViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserCreationSerializer
    def get(self):
        if self.request.method == 'GET':
            
            print(serializer.data)


def signInView(request):
    return Response(request, 'core/signIn.html')

# def signUpView(request):
#     return Response(request, 'core/signUp.html')
