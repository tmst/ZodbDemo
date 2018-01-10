# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements

from cromlech.container.contained import Contained
from dolmen.container import BTreeContainer
from persistent import Persistent
from zope.interface import implementer
from .interfaces import ILeaf, IRoot

@implementer(ILeaf)
class Leaf(Contained, Persistent):

    def __init__(self, title, body):
        Persistent.__init__(self)
        self.title = title
        self.body = body


@implementer(IRoot)
class Root(BTreeContainer):
    title = "Application  Root"
