from django import forms
from django.core import validators


class BanTimeForm(forms.Form):
    ban_time = forms.IntegerField(required=False, label='', min_value=1,
                                  widget=forms.NumberInput(attrs={'placeholder': 'кол-во дней', 'type': 'number'}))


