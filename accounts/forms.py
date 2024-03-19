from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

ALLOWED_EMAILS = ["gmail.com", "outlook.com", "yahoo.com"]

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            # field.field.widget.attrs['style'] = 'border: 1px solid #a8518a;'

class UserRegistrationForm(FormSettings, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].placeholder = 'First Name'
        self.fields['last_name'].placeholder = 'Last Name'
        self.fields['email'].placeholder = 'Email Address'
        self.fields['password1'].placeholder = 'Password'
        self.fields['password2'].placeholder = 'Confirm Password'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith(tuple(ALLOWED_EMAILS)):
            raise forms.ValidationError('This email is not allowed.')
        return email
