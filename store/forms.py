from django import forms

from store.models import Item, RequestOrder


class AddItemForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'class': 'form-control'}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Price', 'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ('name', 'price')


class RequestOrderForm(forms.ModelForm):
    bill_no = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Bill No', 'class': 'form-control'}))
    requested_quantity = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Requested Quantity', 'class': 'form-control'}))
    requested_price = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Price', 'class': 'form-control'}))

    class Meta:
        model = RequestOrder
        fields = ('bill_no', 'requested_price', 'requested_quantity', 'supplier', 'item', 'action')


class StockOrderForm(forms.ModelForm):
    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Requested Quantity', 'class': 'form-control'}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Price', 'class': 'form-control'}))

    class Meta:
        model = RequestOrder
        fields = ('price', 'quantity')
