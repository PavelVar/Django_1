from .models import Message
from django.forms import ModelForm, TextInput, Textarea


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['name', 'email', 'text']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control'}),
        }
