
* See http://hiidef.github.com/oauth2app for documentation. 
* See https://github.com/hiidef/oauth2app for source code.
* Based on http://code.google.com/p/django-oauth2
* Support for OAuth 2.0 draft 16, http://tools.ietf.org/html/draft-ietf-oauth-v2-16

Installation
------------

If easy_install is available, you can use: ::

    easy_install https://github.com/hiidef/oauth2app/tarball/master

Introduction
------------

The oauth2app module helps Django site operators provide an OAuth 2.0 interface. The module
is registered as an application.

How to set up the OAuth2 provider
---------------------------------

In settings.py, add 'oauth2app' to INSTALLED_APPS. ::

    INSTALLED_APPS = (
        ...,
        'oauth2app' 
    )

Sync the DB models. ::

    python manage.py syncdb

In urls.py, add the oauth2app URL patterns::

    urlpatterns = patterns('',
        ...
        url(r'^oauth2/', include('oauth2app.urls')),
        ...
    )

How to set up a sample OAuth2 consumer
--------------------------------------

TODO: move this all into django-oauth2consumer.
    
Create client models. ::

    from oauth2app.models import Client

    Client.objects.create(
        name="My Sample OAuth 2.0 Client",
        user=user)

Authenticate requests. ::

    from oauth2app.authenticate import Authenticator, AuthenticationException
    from django.http import HttpResponse
    
    def test(request):
        authenticator = Authenticator()
        try:
            # Validate the request.
            authenticator.validate(request)
        except AuthenticationException:
            # Return an error response.
            return authenticator.error_response(content="You didn't authenticate.")
        username = authenticator.user.username
        return HttpResponse(content="Hi %s, You authenticated!" % username)

If you want to authenticate JSON requests try the JSONAuthenticator. ::

    from oauth2app.authenticate import JSONAuthenticator, AuthenticationException

    def test(request):
        authenticator = JSONAuthenticator()
        try:
            # Validate the request.
            authenticator.validate(request)
        except AuthenticationException:
            # Return a JSON encoded error response.
            return authenticator.error_response()
        username = authenticator.user.userame
        # Return a JSON encoded response.
        return authenticator.response({"username":username})

Examples
--------

An `example Django project <https://github.com/hiidef/oauth2app/tree/develop/examples/mysite>`_ demonstrating client and server functionality is available in the repository.

https://github.com/hiidef/oauth2app/tree/develop/examples/mysite
