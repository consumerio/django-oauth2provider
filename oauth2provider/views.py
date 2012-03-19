from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from oauth2provider.authenticate import Authenticator, JSONAuthenticator, AuthenticationException
from oauth2provider.authorize import Authorizer, MissingRedirectURI, AuthorizationException
from django import forms
from django.http import HttpResponse

class AuthorizeForm(forms.Form):
    pass

@login_required
def missing_redirect_uri(request):
    return render_to_response(
        'oauth2/missing_redirect_uri.html', 
        {}, 
        RequestContext(request))

@login_required
def authorize(request):
    authorizer = Authorizer()
    try:
        authorizer.validate(request)
    except MissingRedirectURI, e:
        return HttpResponseRedirect("/oauth2/missing_redirect_uri")
    except AuthorizationException, e:
        # The request is malformed or invalid. Automatically 
        # redirects to the provided redirect URL.
        return authorizer.error_redirect()
    if request.method == 'GET':
        template = {}
        # Use any form, make sure it has CSRF protections.
        template["form"] = AuthorizeForm()
        # Appends the original OAuth2 parameters.
        template["form_action"] = '/oauth2/authorize?%s' % authorizer.query_string
        return render_to_response(
            'oauth2/authorize.html', 
            template, 
            RequestContext(request))
    elif request.method == 'POST':
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            if request.POST.get("connect") == "Yes":
                # User agrees. Redirect to redirect_uri with success params.
                return authorizer.grant_redirect()
            else:
                # User refuses. Redirect to redirect_uri with error params.
                return authorizer.error_redirect()
    return HttpResponseRedirect("/")
    
def authenticate(request):
    authenticator = Authenticator()
    try:
        # Validate the request.
        authenticator.validate(request)
    except AuthenticationException:
        # Return an error response.
        return authenticator.error_response(content="You didn't authenticate.")
    username = authenticator.user.username
    return HttpResponse(content="Hi %s, You authenticated!" % username)

def authenticate_json(request):
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
