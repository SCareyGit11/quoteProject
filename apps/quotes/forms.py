from django import forms
from django.forms import ModelForm
from .models import Quote

# Create the form class.
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'speaker']
        widgets = {
        	'quote' : forms.TextInput(attrs={'class':'form-input'}),
        	'speaker' : forms.TextInput(attrs={'class':'form-input'})
        }