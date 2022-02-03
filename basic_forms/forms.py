import email
from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField(label='Name',validators=[validators.MaxLengthValidator(5)])
    email = forms.EmailField(label='Email')
    verify_email = forms.EmailField(label='Verify Email')
    phone = forms.IntegerField(label='Phone')
    dob = forms.DateInput()
    text = forms.CharField(label='Bio',widget=forms.Textarea)

    def clean(self):
        all_clear_Data = super().clean()
        email = all_clear_Data['email']
        vemail = all_clear_Data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Email and Verify email does not match')