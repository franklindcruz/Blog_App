from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )
    last_name = forms.CharField(
        required=True,
    
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].label = ''
            self.fields[fieldname].help_text = ''
            placeholder = {
                'username': 'Username',
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'email': 'Email',
                'password1': 'Password',
                'password2': 'Confirm Password',

            }
            self.fields[fieldname].widget.attrs.update(
                {'placeholder': placeholder.get(fieldname, fieldname.replace('_', ' ').title())})
            self.fields[fieldname].error_messages.update({
                'required': f'{placeholder.get(fieldname, fieldname.replace("_", " ").title())} is required',
                'invalid': f'Enter a valid {placeholder.get(fieldname, fieldname.replace("_", " ").title())}'
            })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Password does not match")
        return cleaned_data


class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
