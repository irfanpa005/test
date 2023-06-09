from .models import crud
from django import forms


class CrudForm(forms.Form):
    sl_no = forms.IntegerField()
    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text'}))
    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


