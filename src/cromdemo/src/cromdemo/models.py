# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import IPublicationRoot
from zope.interface import implementer, Interface
from zope.location import Location, locate
from zope.schema import Text, TextLine, Password


class ILogin(Interface):
    username = TextLine(title=u'Username', required=True)
    password = Password(title=u'Password', required=True)


class ILeaf(Interface):
    title = TextLine(title=u'title', required=True)
    body = Text(title=u'body', required=True)

from dolmen.container import BTreeContainer    

@implementer(IPublicationRoot)
class Root(BTreeContainer):
        title = u"Application  Root"

    
@implementer(ILeaf)
class Leaf(BTreeContainer):

    def __init__(self, title, body):
        BTreeContainer.__init__(self)
        self.title = title
        self.body = body



