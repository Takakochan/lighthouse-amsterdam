from django import forms
from .models import Poem


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'body', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 12, 'placeholder': 'Write your poem here...'}),
        }
        labels = {
            'title': 'Title',
            'body': 'Poem',
            'is_published': 'Publish publicly',
        }
