from django import forms

from recipebox.models import Recipe


class Author_Input(forms.Form):
    name = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    user = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class Recipe_Input(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "author", "desc", "time", "instructions"]
