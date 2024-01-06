from django import forms


class BusinessForm(forms.Form):
    name = forms.CharField(max_length=100)
    website = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)
