from django import forms


class IndexForm(forms.Form):
    offset = forms.CharField(max_length=200, widget=forms.TextInput())
