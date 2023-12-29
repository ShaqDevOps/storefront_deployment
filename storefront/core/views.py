from django.shortcuts import render
from djoser.views import *
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from core.serializers import UserCreateSerializer, UserSerializer
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# from django.views.generic import TemplateView

# class CustomUserCreateView(GenericViewSet,CreateModelMixin):
#     serializer_class = UserCreateSerializer



# class UserProfileView(TemplateView):
#     # serializer_class = UserSerializer
#     template_name = 'core/profile.html'

#     def get_object(self):
#         return self.request.user  # Retrieve the currently authenticated user

def signUpView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # After saving, you can redirect the user or perform other actions
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/signUp.html', {'form': form})


def signInView(request):
    return Response(request, 'core/signIn.html')

# def signUpView(request):
#     return Response(request, 'core/signUp.html')
