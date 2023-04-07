from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import *


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    soglasie = forms.BooleanField(label='Согласие на обработку персональных данных', widget=forms.BooleanField)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Поля паролей не совпадают!')
        return cd['password2']

    def soglasie(self):
        cd = self.cleaned_data
        if cd['soglasie'] != True:
            raise forms.ValidationError('Поле согласие на обработку персональных данных, обязательно!')
            return cd
        return cd['soglasie']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        kiril = [RegexValidator('^[а-яА-Я -]*$', message='Разрешенные символы (кирилица, пробел и тире).')]
        angl = [RegexValidator('^[a-zA-Z0-9-]*$', message='Разрешенные символы (латиница, цифры и тире).')]
        self.fields['username'].validators = angl
        self.fields['username'].label = 'Логин'
        self.fields['username'].help_text = 'Обязательное поле. Только латиница, цифры и тире.'
        self.fields['first_name'].validators = kiril
        self.fields['last_name'].validators = kiril

class RequestCreate(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=forms.Textarea)

    class Meta:
        model = Request
        fields = ('type', 'text', 'img')

