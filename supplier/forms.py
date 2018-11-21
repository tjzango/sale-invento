from django import forms

from supplier.models import (
    Supplier,
)


# This is the form fiels used for addding new supplier
class AddSupplierForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g muslim habibu ', 'class': 'form-control'}))
    contact = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g +2349038337462', 'class': 'form-control'}))
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))

    # Use supplier db table
    class Meta:
        model = Supplier
        fields = ('name', 'contact', 'address')
