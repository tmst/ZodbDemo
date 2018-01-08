# -*- coding: utf-8 -*-

from crom import target, order
from dolmen.view import name, context, view_component
from cromlech.browser.exceptions import HTTPFound
from cromlech.security import Unauthorized
from zope.interface import Interface
from cromlech.browser.interfaces import IPublicationRoot

from . import tal_template,  Page
from ..interfaces import ITab, ILeaf
from ..models import Root, Leaf
from ..auth import logout
from dolmen.container import IBTreeContainer
from dolmen.breadcrumbs import defaultBreadcrumbs

@view_component
@name('logout')
@context(Interface)
class Logout(Page):

    def update(self):
        logout()

    def render(self):
        raise HTTPFound(location='/')

from dolmen.location import resolve_url

class BreadcrumbsPage(Page):
    
    def breadcrumbs(self):
        return defaultBreadcrumbs(self.context,self.request)
    def url2(self,item):
        self.url(item);
        return 'DONE'
    
    def url(self,item):
        if IPublicationRoot.providedBy(item):
           return self.request.application_url
        container = item.__parent__

        result = self.url(container)+ '/' + item.__name__
        print (result)
        return result
    
@view_component
@name('index')
@context(IBTreeContainer)
class RootIndex(BreadcrumbsPage):
    template = tal_template('home.pt')

    
@view_component
@name('index')
@target(ITab)
@context(ILeaf)
@order(10)
class LeafIndex(BreadcrumbsPage):
    template = tal_template('leaf.pt')


@view_component
@name('')
@context(Unauthorized)
class NoAcces(Page):

    def render(self):
        return "No access for you !"
