# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements

from zope.location import Location, locate
from .interfaces import ILogin, ILeaf, IRoot
from dolmen.container import BTreeContainer
from zope.interface import implementer
import persistent
    
@implementer(ILeaf)
class Leaf(persistent.Persistent):
    def __init__(self, title, body):
        self.title = title
        self.body = body

@implementer(IRoot)
class Root(BTreeContainer):
        title = u"Application  Root"

    



