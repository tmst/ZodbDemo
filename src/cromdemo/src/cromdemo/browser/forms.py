# -*- coding: utf-8 -*-
#This software is subject to the CV and Zope Public Licenses.

import uuid
from crom import target, order
from cromlech.browser import IURL
from cromlech.browser.exceptions import HTTPFound
from cromlech.browser.interfaces import IPublicationRoot
from cromlech.browser.directives import title
from cromlech.security import permissions
from dolmen.forms.base import Fields, FAILURE
from dolmen.forms.base import action, name, context, form_component
from dolmen.forms.base import apply_data_event
from dolmen.forms.base.errors import Error
from zopache.ttw.html  import AddCkHTML
from zopache.ttw.container import AddContainer
from zope.interface import implementer, Interface

from zopache.core.forms  import  Form
from ..interfaces import ITab

from ..auth import Auth
from ..interfaces import  IContent, IContentContainer, ILogin
from ..models import  Content, ContentContainer
from dolmen.container import IBTreeContainer, BTreeContainer
from dolmen.template import TALTemplate
from zopache.crud.interfaces import IApp

@form_component
@name('addContent')
@context(IBTreeContainer)
@target(ITab)
@title("Add Content")
@permissions('Manage')
class AddContent(AddCkHTML):
    label='Add a new Content Object'
    implements = IApp
    interface = IContent
    ignoreContent = True
    factory=Content

#THERE ARE BASICALLY TWO VERSIONS OF CONTAINERS
#ONE IS THE STANDARD ONE AT zopache.container
#AND THE OTHER ONE IS THIS ONE, DESIGNED TO BE CUSTOMIZED  YOU
@form_component
@name('addContentContainer')
@context(IBTreeContainer)
@target(ITab)
@title("Add Content Container")
@permissions('Manage')
class AddContentContainer(AddContainer):
    label='Add a new Content Container'
    implements = IApp
    interface = Interface
    ignoreContent = True
    factory=ContentContainer



    
@form_component
@name('login')
@context(Auth)
class Login(Form):

    fields = Fields(ILogin)
    ignoreContent = True

    @property
    def action_url(self):
        return self.request.url

    @action('Log me')
    def login(self):
        data, errors = self.extractData()
        if errors:
            form.errors = errors
            return FAILURE

        success = self.context.authenticate(
            data['username'], data['password'])
        if not success:
            self.errors.append(Error(
                title='Login failed',
                identifier=self.prefix,
            ))
            return FAILURE
        raise HTTPFound(self.request.url)
