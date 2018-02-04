# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements


from dolmen.container import BTreeContainer
from zope.interface import implementer
from .interfaces import ITreeLeaf
from zopache.crud.interfaces import IRootContainer, IContainer, ILeaf
from zopache.core import Leaf
from zopache.ttw.html import HTML, HTMLContainer


@implementer(IContainer)
class TreeBranch(HTMLContainer):
    def __init__(self):
        BTreeContainer.__init__(self)
        
    title = "A Branch on the Tree"
    source=u''
    
@implementer(IRootContainer)
class TreeRoot(TreeBranch):
    title = "Application  Root"

    def __init__(self):
       BTreeContainer.__init__(self)        
       #Needed For Cut Copy Paste
       self.pasteFolder=TreeBranch()
       self.__name__='root'

from zopache.core import Leaf    
#The ITreeLeaf gives the object  attributes
@implementer(ITreeLeaf) 
class TreeLeaf(Leaf):
      pass
       
