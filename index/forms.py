# This file contain all the forms we use in our index application
from django import forms
from index.models import Employee, Account

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


class EmployeeForm(forms.ModelForm):
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Address', 'class': 'form-control'}
    ))
    joined_on = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'placeholder': 'MM-DD-YYYY', 'class': 'form-control'}
    ))

    class Meta:
        model = Employee
        fields = (
            'name',
            'address',
            'status',
            'dob',
            'salary',
            'joined_on',
            'level',
        )


class UserAddForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'First Name e.g Musleem', 'class': 'form-control input' }))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Username e.g Musleem', 'class': 'form-control input'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Lastname e.g Exe John', 'class': 'form-control input' }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Strong Password', 'class': 'form-control input' }))
    password_ = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Retype Password', 'class': 'form-control input' }))

    class Meta:
        model = Account
        fields = (
            'user',
            'employee'
        )
