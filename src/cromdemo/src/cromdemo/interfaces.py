from cromlech.browser.interfaces import IPublicationRoot
from zope.interface import implementer, Interface
from dolmen.container import BTreeContainer,IBTreeContainer
from cromlech.browser import IView
from zope.schema import Text, TextLine, Password

class ITab(IView):
    pass

class IRoot(IPublicationRoot, IBTreeContainer):
      pass

class IName (Interface):
    name = TextLine(
        title='Object Id', required=True)
    
class ILogin(Interface):

    username = TextLine(
        title='Username', required=True)

    password = Password(
        title='Password', required=True)


class ILeaf(Interface):

    title = TextLine(
        title='Title', required=True)

    body = Text(
        title='Body', required=True)

