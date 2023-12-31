from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .forms import CustomUserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from .serializers import *


User = get_user_model()

class SignUpViewSet(ModelViewSet):
    serializer_class = UserCreateSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return User.objects.none()  # Or apply other filtering logic
        return super().get_queryset()  
    

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return[AllowAny()]
        else:
            return [IsAdminUser()]
        
  

    @action(detail=False, methods=['get', 'post'])
    def SignUpForm(self, request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.data)
            if form.is_valid():
                form.save()
                # Redirect or perform other actions after saving
                return redirect('/')
        else:
            form = CustomUserCreationForm()

        # Use Django's render function to render the form template
        return (render(request, 'core/SignUp.html', {'form': form}))
    
#HOW TO USE TEMPLATES WITH REST_FRAMEWORK
        """
        class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'user': self.object}, template_name='user_detail.html') ==> This LINE RIGHT HERE
        
        
        """


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])  # Allow any user to access this view
def SignInView(request):
    if request.method in ['POST']:
        # Extract credentials from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated
            refresh = RefreshToken.for_user(user)

            if user is not None:
                # User is authenticated
                return render(request, 'core/index.html')  # Render a simple HTML template

        else:
            # Invalid credentials
            # You can pass an error message to the template
            error_message = 'Invalid Credentials'
            return render(request, 'core/SignIn.html', {'error_message': error_message})

    # If it's a GET request, render the sign-in template
    return render(request, 'core/SignIn.html')