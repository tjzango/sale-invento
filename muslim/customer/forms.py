from django import forms
from customer.models import Customer


class AddCustomerForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Haruna Tijjani', 'class': 'form-control'}))
    contact = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g +2349038337462', 'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ('name', 'contact')
