from django import forms

class delivery(forms.Form):
    name = forms.CharField()
    fam = forms.CharField()
    mail = forms.CharField()
    adres = forms.CharField()
