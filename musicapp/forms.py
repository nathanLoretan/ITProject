from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match ")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_count = User.objects.filter(email=email).count()
        if email_count:
            raise forms.ValidationError('Email already exists')
        return email

