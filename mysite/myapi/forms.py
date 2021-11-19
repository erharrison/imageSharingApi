from django import forms
from .models import ImagePost


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('image', 'caption')
