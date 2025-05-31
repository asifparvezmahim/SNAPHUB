from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
class Registerform(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'autocomplete': 'current-password',
            'autofocus': True
        })
        self.fields['new_password1'].widget.attrs.update({
            'autocomplete': 'new-password'
        })
        self.fields['new_password2'].widget.attrs.update({
            'autocomplete': 'new-password'
        })