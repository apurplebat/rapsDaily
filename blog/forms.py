# blog/forms.py

from django import forms
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class PhotoContestForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField()

    photo = forms.ImageField()
    #gender = forms.ChoiceField(
    #    label='Gender',
    #    required=False,
    #    choices=[
    #        (None, '-------'),
    #        ('m', 'Male'),
    #        ('f', 'Female'),
    #        ('n', 'Non-binary'),
    #    ]
    #)
    #receive_newsletter = forms.BooleanField(
    #    required=False,
    #    label='Do you wish to receive our newsletter?'
    #)