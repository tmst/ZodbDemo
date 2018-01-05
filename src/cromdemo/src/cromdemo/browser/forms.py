# -*- coding: utf-8 -*-

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
from dolmen.forms.crud import Add


from  slugify import slugify

from . import  Form
from ..interfaces import ITab, IName

from ..auth import Auth
from ..interfaces import  ILeaf, ILogin
from ..models import  Leaf
from dolmen.container import IBTreeContainer, BTreeContainer

@form_component
@name('addLeaf')
@context(IBTreeContainer)
@target(ITab)
@order(50)
@title("Add a leaf")
@permissions('Manage')
class AddLeaf(Form):

    fields = Fields(ILeaf)
    ignoreContent = True

    @action('Add')
    def add(self):
        data, errors = self.extractData()
        if errors:
            form.errors = errors
            return FAILURE
        name=slugify(data['title'])
        content = Leaf(data['title'], data['body'])
        self.context[name] = content
        raise HTTPFound(IURL(self.context, self.request))


#AND NOW ADD A CONTAINER
@form_component
@name('addContainer')
@context(IBTreeContainer)
@target(ITab)
@order(60)
@title("Add a Container")
@permissions('Manage')
class AddContainer(Form):
    fields = Fields(IName)
    ignoreContent = True
    
    @action('Add')
    def add(self):
        data, errors = self.extractData()
        if errors:
            form.errors = errors
            return FAILURE
        name=slugify(data['name'])
        content = BTreeContainer()
        self.context[name] = content
        raise HTTPFound(IURL(self.context, self.request))

    
@form_component
@name('edit')
@context(ILeaf)
@target(ITab)
@order(20)
@title("Edit the content")
@permissions('Manage')
class Edit(Form):

    fields = Fields(ILeaf)
    ignoreContent = False

    @action('Apply')
    def apply(self):
        data, errors = self.extractData()
        if errors:
            form.errors = errors
            return FAILURE

        content = self.getContent()
        apply_data_event(self.fields, content, data)
        raise HTTPFound(IURL(content, self.request))


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
