from django import forms
from .models import Publish, Category
choices = Category.objects.all().values_list()
choices_list = []

for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Publish
        fields = ('title', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter a title!!'}),
            'author': forms.Select(
                attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,
                                     attrs={'class': 'form-control'}),
            'body': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Just put your imagination'}),

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Publish
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter a nice title!!'}),
            'body': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Just put your imagination'}),
                       }
