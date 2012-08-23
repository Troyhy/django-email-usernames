"""
    In your base urls.py include these urls _before_ the django-registration urls.

    Example:

    (r'^accounts/', include('email_usernames.backends.email.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
"""

from django.conf.urls.defaults import *
from registration.views import register
from ...forms import EmailLoginForm

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'authentication_form': EmailLoginForm}, name='login'), 
    url(r'^register/$', register, { 'backend': 'email_usernames.backends.email.EmailBackend' }, name='registration_register'),
)