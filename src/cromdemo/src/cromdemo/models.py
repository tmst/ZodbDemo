# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements

import persistent

from dolmen.container import BTreeContainer
from zope.interface import implementer
from .interfaces import ILeaf, IRoot


@implementer(ILeaf)
class Leaf(persistent.Persistent):

    def __init__(self, title, body):
        self.title = title
        self.body = body


@implementer(IRoot)
class Root(BTreeContainer):
    title = "Application  Root"

    



