from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_pass = forms.CharField(label='Your pass', max_length=100)