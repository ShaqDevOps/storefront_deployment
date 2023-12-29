from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from .serializers import *

User = get_user_model()

class SignUpViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @action(detail=False, methods=['get', 'post'])
    def render_form(self, request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.data)
            if form.is_valid():
                form.save()
                # Redirect or perform other actions after saving
                return Response({'status': 'User created'})
        else:
            form = CustomUserCreationForm()

        # Use Django's render function to render the form template
        return (render(request, 'core/signUp.html', {'form': form}))





# User = get_user_model()

# class SignUpViewSet(GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = CustomUserCreationSerializer
#     def GetRenderedForm(self, request):
#         form = CustomUserCreationForm
#         if self.request.method == 'GET':
#           return render(request, {form :'form'}, 'core/signUp.html')



#     # def PostForm(self):

    #     if self.request.method == 'POST':
    #          print(<object from the form>)


def signInView(request):
    return Response(request, 'core/signIn.html')

# def signUpView(request):
#     return Response(request, 'core/signUp.html')
