from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Haroun'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Exe John'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'haroun@gmail.com'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Strong Password'}))
    password_ = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Strong Password'}))


class UserLoginForm(forms.Form):
    username = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'haroun@gmail.com'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': '*******'}))


class UserProfileForm(forms.Form):
    contact = forms.CharField(required=True,  widget=forms.TextInput(
        attrs={'placeholder': 'e.g 08012345678'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Haroun'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Exe John'}))


class BankInfo(forms.Form):
    bank_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Farmers Bank'}))
    account_no = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'e.g 1234567890'}))
    account_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Farmers Account'}))
    sort_code = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Sort Code'}))


class AddAdminForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter fullname'}))
    username = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password_ = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))