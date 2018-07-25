from django import forms
from supplier.models import (
    Supplier,
)
from store.models import (
    RequestOrder
)


class AddSupplierForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Haruna Tijjani', 'class': 'form-control'}))
    contact = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g +2349038337462', 'class': 'form-control'}))
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': '', 'class': 'form-control'}))

    class Meta:
        model = Supplier
        fields = ('name', 'contact', 'address')

