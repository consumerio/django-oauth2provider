from django.conf.urls.defaults import patterns, url
from oauth2app.token import handler as token_handler
from oauth2app.views import missing_redirect_uri, authorize

urlpatterns += patterns('',
    url(r'^missing_redirect_uri/?$', missing_redirect_uri, name='missing_redirect_uri'),
    url(r'^authorize/?$', authorize, name='authorize'),
    url(r'^token/?$', token_handler, name='token_handler'),
)
