from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['login', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "As senhas não correspondem. Por favor, tente novamente."
            )

    def save(self, commit=True):
        user_profile = super(UserForm, self).save(commit=False)
        user = User.objects.create_user(username=user_profile.login, email=user_profile.email, password=self.cleaned_data['password'])
        user_profile.user = user

        if commit:
            user_profile.save()
        return user_profile
