# -*- coding: utf-8 -*-

from .models import Root
from .auth import secured
from cromlech.dawnlight import DawnlightPublisher
from cromlech.browser.interfaces import IView
from cromlech.dawnlight import ViewLookup, view_locator
from cromlech.security import unauthenticated_principal
from cromlech.security import ContextualProtagonist, Principal
from cromlech.wsgistate.controlled import WsgistateSession
from cromlech.webob.request import Request
from cromlech.i18n import EnvironLocale
from crom import ComponentLookupError
from cromlech.browser.predication import resolve_predications
from cromlech.security import Unauthorized, Forbidden


logins = {
    'demo': 'demo',
    'admin': 'admin',
}


def query_view(request, context, name=""):
    view = IView.component(context, request, name=name)
    try:
        resolve_predications(view, context, request)
    except (Unauthorized, Forbidden) as e:
        raise
    except Exception as e:
        raise ComponentLookupError(str(e))
    return view(context, request)


view_lookup = ViewLookup(view_locator(query_view))


def demo_application(environ, start_response):

    @secured(logins, "CromlechDemo")
    def publisher(environ, start_response):
        with EnvironLocale(environ):
            request = Request(environ)
            root = Root()
            username = environ.get('REMOTE_USER')
            if username is not None:
                principal = Principal(username)
            else:
                principal = unauthenticated_principal
            with ContextualProtagonist(principal):
                publisher = DawnlightPublisher(view_lookup=view_lookup)
                response = publisher.publish(request, root, handle_errors=True)
                return response(environ, start_response)

    with WsgistateSession(environ, 'session'):
        response = publisher(environ, start_response)

    return response
