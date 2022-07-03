from tkinter import Widget
from django.forms import ModelForm
from django import forms

from .models import Stock


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ("name", "shares")

        Widget = {
            'name': forms.TextInput(attrs={"calss": "form-control", "placeholder": "Symbol of the stock"}),
            'shares': forms.NumberInput(attrs={"calss": "form-control", "placeholder": "Number of shares"}),
        }
