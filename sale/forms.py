from django import forms
from sale.models import Order


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 1000)]


class QuantityForm(forms.Form):
    unit = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)


class OrderSaveForm(forms.ModelForm):
    amount_paid = forms.CharField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'eg 1000'}))

    class Meta:
        model = Order
        fields = ('customer', 'amount_paid')
