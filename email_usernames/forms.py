# encoding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

try:
    # If you have django-registration installed, this is a form you can
    # use for users that signup.
    from registration.forms import RegistrationFormUniqueEmail
    class EmailRegistrationForm(RegistrationFormUniqueEmail):
        def __init__(self, *args, **kwargs):
            super(EmailRegistrationForm, self).__init__(*args, **kwargs)
            del self.fields['username']

        def save(self, *args, **kwargs):
            # Note: if the username column has not been altered to allow 75 chars, this will not
            #       work for some long email addresses.
            self.cleaned_data['username'] = self.cleaned_data['email']
            return super(EmailRegistrationForm, self).save(*args, **kwargs)
except ImportError:
    pass

class EmailLoginForm(AuthenticationForm):
    email = forms.EmailField(label=_("Email"), max_length=75, widget=forms.TextInput(attrs=dict(maxlength=75)))

    def __init__(self, *args, **kwargs):
        result = super(EmailLoginForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        self.fields.keyOrder = ['email', 'password']
        return result

    def clean(self):
        self.cleaned_data['username'] = self.cleaned_data.get('email')
        return super(EmailLoginForm, self).clean()