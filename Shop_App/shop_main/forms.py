from django import forms

class Register_form(forms.Form):
    usernameInput = forms.CharField(label='user name', max_length = 100)
    nameInput = forms.CharField(label='name', max_length = 100)
    lastnameInput = forms.CharField(label='last name', max_length = 200)
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

    widgets = {
            'password': forms.PasswordInput(),
        }

class UserLog(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput)

    widgets = {
        'password': forms.PasswordInput(),
    }

class Basket_form(forms.Form):
    mount_of = forms.IntegerField(label='how many?', initial='1');
