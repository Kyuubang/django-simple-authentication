from django import forms

class NameForm(forms.Form):
        # TODO: Create Register form included (Username, First name, Last name, Email, Password)
        username = forms.CharField(label='Username', max_length=100)
        email = forms.CharField(label='Username', max_length=100)
        firstname = forms.CharField(label='First Name', max_length=100)
        lastname = forms.CharField(label='Last Name', max_length=100)
        password = forms.CharField(label='Password', max_length=100)

        # TODO: Create Login form included (Username/Email, Password)
        
