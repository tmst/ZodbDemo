# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements


from dolmen.container import BTreeContainer
from zope.interface import implementer
from .interfaces import ITreeLeaf
from zopache.crud.interfaces import IRootContainer, IContainer, ILeaf
from zopache.core import Leaf

@implementer(IRootContainer)
class TreeRoot(BTreeContainer):
    title = "Application  Root"

@implementer(IContainer)
class TreeBranch(BTreeContainer):
    title = "A Branch on the Tree"



from zopache.core import Leaf    
#The ITreeLeaf gives the object  attributes
@implementer(ITreeLeaf) 
class TreeLeaf(Leaf):

    def __init__(self, **kwargs):
        Persistent.__init__(self)
        Contained.__init__(self)
        for key, value in kwargs.items():
            setattr(self,key,value)
       
