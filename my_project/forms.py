from django import forms

class Form(forms.Form):
    address = forms.URLField(label = 'Enter a URL')
