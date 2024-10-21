from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder' : 'Your Username',
            'class' : 'p-7 rounded-xl w-full'
        }))
        
        email= forms.CharField(widget = forms.EmailInput(attrs= {
            'placeholder' : 'Your Email',
            'class' : 'p-7 rounded-xl w-full'
        }))
         
        password1 = forms.CharField(widget = forms.PasswordInput(attrs= {
            'placeholder' : 'Your Password',
            'class' : 'p-7 rounded-xl w-full'
        }))
          
        password2 = forms.CharField(widget = forms.PasswordInput(attrs= {
            'placeholder' : 'Repeat Password',
            'class' : 'p-7 rounded-xl w-full'
        }))

class Login(AuthenticationForm):
    # model = User
    # fields = ('username', 'password')
    class Meta:
    
        username = forms.CharField(widget=forms.TextInput(attrs={
                "placeholder" : "Your Username",
                "class" : "p-7 rounded-xl w-full",
            }))
        
        password = forms.CharField(widget = forms.PasswordInput(attrs= {
                'placeholder' : 'Repeat Password',
                'class' : 'p-7 rounded-xl w-full'
            }))
