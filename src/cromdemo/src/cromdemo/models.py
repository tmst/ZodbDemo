# -*- coding: utf-8 -*-

# Subject to ZPL and CV License agreements


from dolmen.container import BTreeContainer
from zope.interface import implementer
from .interfaces import IContent, IContentContainer
from .interfaces import IRootContentContainer
from zopache.crud.interfaces import  IContainer, ILeaf
from zopache.core import Leaf
from zopache.ttw.container import HTMLContainer
from zopache.ttw.html import TrustedHTML

#THIS IS BASICALLYT HE SAME THING AS A
#TTW CONTAINER, BUT THIS ONE IS FOR YOU TO
#CUSTOMIZE
@implementer(IContentContainer)
class ContentContainer(HTMLContainer):
    def __init__(self):
        BTreeContainer.__init__(self)
        
    title = "An HTML Container"
    source=u''
    
@implementer(IRootContentContainer)
class TreeRoot(ContentContainer):
    title = "Application  Root"

    def __init__(self):
       BTreeContainer.__init__(self)        
       #Needed For Cut Copy Paste
       self.pasteFolder=HTMLContainer()
       self.__name__='root'

from zopache.core import Leaf    
#The IContent gives the object  attributes
@implementer(IContent) 
class Content(TrustedHTML,Leaf):
      pass


