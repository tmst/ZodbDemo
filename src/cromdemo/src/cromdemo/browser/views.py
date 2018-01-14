# -*- coding: utf-8 -*-
#This software is subject to the CV and Zope Public Licenses.

from crom import target, order
from dolmen.view import name, context, view_component
from cromlech.browser.exceptions import HTTPFound
from cromlech.security import Unauthorized
from cromlech.browser.directives import title

#FROM INTERFACES
from zope.interface import Interface
from dolmen.container import IBTreeContainer
from cromlech.browser.interfaces import IURL, IPublicationRoot
from zopache.crud import IRootContainer
from ..interfaces import ITab, ITreeLeaf


from . import tal_template,  Page
from ..models import TreeRoot, TreeLeaf
from ..auth import logout
from dolmen.breadcrumbs import BreadcrumbsRenderer


@view_component
@name('logout')
@title("Logout")
@context(Interface)
class Logout(Page):

    def update(self):
        logout()

    def render(self):
        raise HTTPFound(location='/')


class BreadcrumbsPage(Page):
    
    def breadcrumbs(self):
        renderer = BreadcrumbsRenderer()
        renderer.update()
        return renderer.render()

    def url2(self,item):
        self.url(item);
        return 'DONE'

    def url(self,item):
        if IPublicationRoot.providedBy(item):
           return self.request.application_url
        container = item.__parent__
        result = self.url(container)+ '/' + item.__name__
        return result


@view_component
@name('index')
@title("View")
@target(ITab)
@context(IBTreeContainer)
class RootIndex(BreadcrumbsPage):
    template = tal_template('home.pt')

    
@view_component
@name('index')
@title("View")
@target(ITab)
@context(ITreeLeaf)
@order(10)
class LeafIndex(BreadcrumbsPage):
    template = tal_template('leaf.pt')


@view_component
@name('')
@context(Unauthorized)
class NoAcces(Page):

    def render(self):
        return "No access for you !"
