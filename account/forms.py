from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput) #чтобы скрыть пароль
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation', 'email', 'first_name', 'last_name')

    def clean_username(self): #этот метод всегда должен возвращать значение, которое проверяется
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists(): #exist выдает true/false
            raise forms.ValidationError('User with given username already exists')
        return username

    def clean(self): #метод clean должен быть один, здесь осуществляются все проверки, которые нужны
        data = self.cleaned_data  #data это словарь со значениеями, а ключи - поля
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Пароли не совпадают')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data) #распаковка словаря
        return user
