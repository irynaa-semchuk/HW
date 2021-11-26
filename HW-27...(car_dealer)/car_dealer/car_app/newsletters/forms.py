from django import forms

from car_app.newsletters.models import NewsLetter


class NewsLetterModelForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']