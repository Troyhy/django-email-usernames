from registration.backends.default import DefaultBackend
from email_usernames.forms import EmailRegistrationForm

class EmailBackend(DefaultBackend):
    def register(self, request, **kwargs):
        # override the username with the email address and let 
        # the DefaultBackend finish the registration process
        kwargs['username'] = kwargs['email']
        return super(EmailBackend, self).register(request, **kwargs)

    def get_form_class(self, request):
        return EmailRegistrationForm