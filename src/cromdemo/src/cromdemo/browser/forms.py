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
from zopache.crud.components import AddForm


from zopache.core.forms  import  Form
from ..interfaces import ITab

from ..auth import Auth
from ..interfaces import  ITreeLeaf, ITreeBranch, ILogin
from ..models import  TreeLeaf, TreeBranch
from dolmen.container import IBTreeContainer, BTreeContainer
from dolmen.template import TALTemplate

@form_component
@name('addLeaf')
@context(IBTreeContainer)
@target(ITab)
@title("Add a leaf")
@permissions('Manage')
class AddLeaf(AddForm):
    interface = ITreeLeaf
    ignoreContent = True
    factory=TreeLeaf

@form_component
@name('addBranch')
@context(IBTreeContainer)
@target(ITab)
@title("Add a Branch")
@permissions('Manage')
class AddBranch(AddForm):
    interface = ITreeBranch
    ignoreContent = True
    factory=TreeBranch   


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
