# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements

from cromlech.container.contained import Contained
from dolmen.container import BTreeContainer
from persistent import Persistent
from zope.interface import implementer
from .interfaces import ITreeLeaf
from zopache import crud
        
@implementer(crud.IRootContainer)
class TreeRoot(BTreeContainer):
    title = "Application  Root"

@implementer(crud.IContainer)
class TreeBranch(BTreeContainer):
    title = "A Branch on the Tree"

#The ITreeLeaf gives the object  attributes
@implementer(ITreeLeaf) 
class TreeLeaf(Contained, Persistent):

    def __init__(self, **kwargs):
        Persistent.__init__(self)
        Contained.__init__(self)
        for key, value in kwargs.items():
            setattr(self,key,value)
       
