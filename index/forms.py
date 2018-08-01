# This file contain all the forms we use in our index application
from django import forms

# This is the form used in user rigistation it contain first & last name, email, password and another password
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


# This is the form fields used in user login page
class UserLoginForm(forms.Form):
    username = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'haroun@gmail.com'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': '*******'}))


# Form field used for user profile form
class UserProfileForm(forms.Form):
    contact = forms.CharField(required=True,  widget=forms.TextInput(
        attrs={'placeholder': 'e.g 08012345678'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Haroun'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'e.g Exe John'}))


class AddAdminForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter fullname'}))
    username = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password_ = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))