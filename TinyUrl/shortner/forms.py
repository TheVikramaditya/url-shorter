from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(error_messages={'required':'username is necessary'},required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields =['username']
        labels={'email':'your Email',}#'first_name':'your first name'}
        # widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        # }
        # error_messages={'email':{'required':'this field is required'}}

class LogInForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fiedls=['username','password']