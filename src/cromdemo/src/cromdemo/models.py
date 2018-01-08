# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements


from dolmen.container import BTreeContainer, Contained
from zope.interface import implementer
from .interfaces import ILeaf, IRoot


@implementer(ILeaf)
class Leaf(Contained):

    def __init__(self, title, body):
        Contained.__init__(self)
        self.title = title
        self.body = body


@implementer(IRoot)
class Root(BTreeContainer):
    title = "Application  Root"

    



