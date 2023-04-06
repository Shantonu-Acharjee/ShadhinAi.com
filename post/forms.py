from django import forms
from .models import Blog

class TextForm(forms.Form):
    text = forms.CharField(widget= forms.TextInput, required= True)



class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'banner', 'description')