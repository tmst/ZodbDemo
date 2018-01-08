# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements

from zope.location import Location, locate
from .interfaces import ILogin, ILeaf, IRoot
from zope.interface import implementer
from persistent import Persistent
from dolmen.container import BTreeContainer
    
@implementer(ILeaf)
class Leaf(Persistent):
    def __init__(self, title, body):
        Persistent.__init__(self)
        self.title = title
        self.body = body


@implementer(IRoot)
class Root(BTreeContainer):
        title = "Application  Root"

    



