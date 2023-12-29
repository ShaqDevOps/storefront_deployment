from django.views.generic import TemplateView
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

# URLConf
urlpatterns = [
    path('', TemplateView.as_view(template_name = 'core/index.html')),
     path('signIn/', views.signInView, name='signIn'),
    path('signUp/', views.SignUpViewSet.as_view({'get': ''}), name='signUp'),
    #  path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    # path('register/', views.CustomUserCreateView.as_view({'post': 'create'}), name='user-registration'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

