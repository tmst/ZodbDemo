# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements

from zope.location import Location, locate
from .interfaces import ILogin, ILeaf, IRoot
from dolmen.container import BTreeContainer
from zope.interface import implementer
from persistent import Persistent
    
@implementer(ILeaf)
#class Leaf(BTreeContainer):
class Leaf(Persistent):
    #IT COULD ALSO HAVE SUBCLASSED OFF OF CLASS PERSISTENT
    title="A leaf"
    body="A Beautiful leaf"
    """
    def __init__(self, title, body):
        BTreeContainer.__init__(self)
        self.title = title
        self.body = body
    """

@implementer(IRoot)
class Root(BTreeContainer):
        title = "Application  Root"

    



