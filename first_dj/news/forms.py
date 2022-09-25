from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticleForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date',]

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Article title'}),
            'anons': TextInput(attrs={'class': 'form-control', 'placeholder': 'Article anons'}),
            'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Article Text'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Article date'}),
        }


