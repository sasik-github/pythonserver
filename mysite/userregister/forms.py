# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class UserForm(forms.Form):
    """docstring for ContactForm"""
    name = forms.CharField(label = u'ФИО', max_length = 100, widget = forms.TextInput(attrs = {'class':'form-control'}))
    borndate = forms.DateField(label = u'Дата рождения', 
        widget = SelectDateWidget(
                years = [x for x in range(date.today().year, date.today().year - 80, -1)],
                attrs = {'class': 'form-control', 'style': 'width: 33%; display: inline-block;'}
            ),
        )
    age = forms.IntegerField(label = u'Возраст', widget = forms.NumberInput(attrs = {'class':'form-control'}))
    job = forms.CharField(label = u'Профессия', max_length = 60, widget = forms.TextInput(attrs = {'class':'form-control'}))
    created_at = forms.DateTimeField(label = u'Дата регистрации', widget = forms.TextInput(attrs = {'class':'form-control',}))


class UserFormExtended(UserForm):
    """docstring for UserFormExtended"""
    def as_bootstrap():
        pass
        