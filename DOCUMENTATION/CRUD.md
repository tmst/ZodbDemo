Cromlech.forms.crud
===============

Every application needs to do CRUD on objects.  Create, Read, Update Delete.
This package provide that.  There are four classes represented here.
Display, Add, Edit, Delete, and 4 actions
AddAction, UpdateAction, DeleteAction, CancelAction

We have to define the class we are going to operating on.  But first we
have to define its interface.


from dolmen.forms.crud import Display, Add, Edit, Delete
from dolmen.forms.crud import AddAction, UpdateAction
from dolmen.forms.crud imnport DeleteAction, CancelAction

from cromlech.content import Factory
from cromdemo.models import Root, Leaf


@form_component
@crom.sources(IRequest, Leaf)
class AddLeafForm(Form):
   label = u"Add a Leaf"
   description = u"to the parent node."
   fields = Fields(Field(u'Name'))
   actions = Actions(AddAction("Add a Leaf",Factory(Leaf)))