# -*- coding: utf-8 -*-

#This software is subject to the CV and Zope Public Licenses.

from cromlech.browser.interfaces import IPublicationRoot
from zope.interface import implementer, Interface
from dolmen.container import BTreeContainer,IBTreeContainer
from cromlech.browser import IView
from zope.schema import Text, TextLine, Password
from zopache.crud.interfaces import ILeaf, IContainer

class ITab(IView):
    pass


class ILogin(Interface):

    username = TextLine(
        title='Username', required=True)

    password = Password(
        title='Password', required=True)


    
class ITreeLeaf(ILeaf):

    title = TextLine(
        title='Title', required=True)

    body = Text(
        title='Body', required=True)

#The difference is that Tree Branches subclass
#off of containers, so you can add stuff to them. 
class ITreeBranch(IContainer):

    title = TextLine(
        title='Title', required=True)

    body = Text(
        title='Body', required=True)    


