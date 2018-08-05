from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'e.g Muslim'}))
    contact = forms.CharField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'eg 07064353426'}))

    class Meta:
        model = Customer
        fields = ('name', 'contact')
