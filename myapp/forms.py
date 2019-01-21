# myapp/forms.py
from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea) # FormField에는 TextField가 없다!