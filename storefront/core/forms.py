from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Include the fields you want from your User model
        fields = ('username', 'email', 'first_name', 'last_name')



class UserDetailForm(forms.Form):
    username = forms.CharField(max_length=150, disabled=True)  # Username is typically not editable
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    # Include any additional fields or validation as required


# class UserSignIn(forms.Form):
#     username = forms.CharField(max_length=150, disabled=True)
#     password = forms.CharField(max_length=)