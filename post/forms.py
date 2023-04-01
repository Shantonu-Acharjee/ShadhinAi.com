from django import forms
class TextForm(forms.Form):
    text = forms.CharField(widget= forms.TextInput, required= True)