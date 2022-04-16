from django import forms
from django.contrib.auth import get_user_model


class MyUserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.errors['password'] = 'Пароли не совпадают!'
            self.errors['password_confirm'] = 'Пароли не совпадают!'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['image', 'username', 'email', 'phone', 'is_company', 'password', 'password_confirm']
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['image', 'username', 'email', 'phone']
        
        
class PasswordUpdateForm(forms.ModelForm):
    password = forms.CharField(strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(strip=False, widget=forms.PasswordInput)
    password_old = forms.CharField(strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_password_old(self):
        password_old = self.cleaned_data.get('password_old')
        if not self.instance.check_password(password_old):
            raise forms.ValidationError('Не правильно указан старый пароль!')
        return password_old

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['password_confirm'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'password_old']

