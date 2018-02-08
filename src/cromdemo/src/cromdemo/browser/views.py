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
from zopache.crud.interfaces import IRootContainer
from cromdemo.interfaces import ITab,IContent


from zopache.core.page  import  Page
from ..models import TreeRoot
from ..auth import logout
from dolmen.breadcrumbs import BreadcrumbsRenderer
from . import tal_template

@view_component
@name('logout')
@title("Logout")
@context(Interface)
class Logout(Page):

    def update(self):
        logout()

    def render(self):
        raise HTTPFound(location='/')


#THIS WAS THE ORIGINAL VIEW ON BTREES CONTAINERS
#IT IS NO LONGER USED, BUT IT COULD BE USED.
# TO DO SO, 
# JUST REMOVE THE COMMENT LINES BELOW. 
    
#@view_component
#@name('index')
#@title("Manage")
#@target(ITab)
#@context(IBTreeContainer)
class ContainerIndex(Page):
    template = tal_template('home.pt')

    
#@view_component
#@name('index')
#@title("View")
#@target(ITab)
#@context(IContent)
#@order(10)
class ContentIndex(Page):
    template = tal_template('content.pt')


@view_component
@name('')
@context(Unauthorized)
class NoAcces(Page):

    def render(self):
        return "No access for you !"
