.. warning::

    This fork of oauth2app is still a work in progress.  Do not use this.


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

In settings.py, add 'oauth2provider' to INSTALLED_APPS. ::

    INSTALLED_APPS = (
        ...,
        'oauth2provider' 
    )

Sync the DB models. ::

    python manage.py syncdb

In urls.py, add the oauth2provider URL patterns::

    urlpatterns = patterns('',
        ...
        url(r'^oauth2/', include('oauth2provider.urls')),
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

Examples
--------

An `example Django project <https://github.com/hiidef/oauth2app/tree/develop/examples/mysite>`_ demonstrating client and server functionality is available in the repository.

https://github.com/hiidef/oauth2app/tree/develop/examples/mysite
