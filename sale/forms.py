from django import forms

from sale.models import Order, Expense

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 1000)]


class QuantityForm(forms.Form):
    unit = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)


class OrderSaveForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('customer',)


class DebtForm(forms.Form):
    balance = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'placeholder': 'eg 1000', 'value': 0}))


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'amount')
