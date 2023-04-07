from django import forms
from .models import Blog
from ckeditor.fields import RichTextField

class TextForm(forms.Form):
    text = forms.CharField(widget= forms.TextInput, required= True)



class AddBlogForm(forms.ModelForm):
    description = RichTextField()
    class Meta:
        model = Blog
        fields = ('title', 'category', 'banner', 'description')