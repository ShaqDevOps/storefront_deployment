from django.views.generic import TemplateView
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views
from rest_framework.routers import DefaultRouter

app_name = 'core'

router = DefaultRouter()
router.register('SignUp', views.SignUpViewSet, basename='SignUp')



# URLConf
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='Home'),
    path('SignIn/', views.SignInView, name='SignIn'),
    # path('signUp/', views.SignUpViewSet, name='signUp'),
    #  path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    # path('register/', views.CustomUserCreateView.as_view({'post': 'create'}), name='user-registration'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]


urlpatterns += router.urls
