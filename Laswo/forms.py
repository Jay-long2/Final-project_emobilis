from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 20:
            raise forms.ValidationError("Message must be at least 20 characters.")
        return message
