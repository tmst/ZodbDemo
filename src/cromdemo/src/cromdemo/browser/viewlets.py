# -*- coding: utf-8 -*-

from crom import order
from crom.utils import sort_components
from dolmen.viewlet import viewlet, Viewlet
from cromlech.browser import IURL, slot
from cromlech.browser.directives import title
from cromlech.security import getSecurityGuards, permissions

from . import tal_template
from ..interfaces import ITab, ILeaf
from .layout import SiteHeader, AdminHeader, ContextualActions
from .layout import Footer, Breadcrumbs
from dolmen.breadcrumbs import defaultBreadcrumbs

@viewlet
@slot(Footer)
class Footer(Viewlet):

    def render(self):
        return """
<div class='container'>
  <em>Read 
    <a href='https://github.com/pythonlinks/Demo#introduction'>the Documentation</a>.
  </em>
</div>"""


@viewlet
@slot(SiteHeader)
class Cromlech(Viewlet):

    def render(self):
        baseurl = self.request.script_name
        if not baseurl.startswith('/'):
            baseurl = '/' + baseurl
        return  "<h1><a href='%s'>ZODB Demo</a></h1>" % baseurl


@viewlet
@slot(Breadcrumbs)
class Breadcrumbs(Viewlet):
    def render(self):
        return defaultBreadcrumbs(self.context,self.request) 



@viewlet
@slot(SiteHeader)
@permissions('View')
class Logout(Viewlet):

    def render(self):
        return """
<div class='header-action pull-right'><a href='%s/logout'>Logout</a></div>
""" % self.request.script_name


@viewlet
@slot(AdminHeader)
class WelcomeMaster(Viewlet):
    """Greets a logged in superuser on the index.
    """
    def render(self):
        username = self.request.environment['REMOTE_USER']
        return "<p>Welcome, master %s !</p>" % username


def sort_key(component):
    explicit = order.get_policy(component[1], order.dotted_name, 0)
    return (explicit, component[1].__module__, component[1].__class__.__name__)

from cromdemo.models import Leaf
@viewlet
@slot(ContextualActions)
class Tabs(Viewlet):
    template = tal_template('tabs.pt')

    def tabs(self):
        url = IURL(self.context, self.request)
        for id, view in self._tabs:    
            #Basically if the views are for Ileaves
            #And the context is ILeaf,
            #or vice versa display them. 
            #Really this should be
            #if getattr(view,'cromlech.context').providedBy(self.context)
            if not (( getattr(view,'cromlech.context')==ILeaf) ==
                    (ILeaf.providedBy(self.context))):
                continue
            yield {
                'active': self.view.__class__ is view,
                'title': title.get(view) or id,
                'url': '%s/%s' % (url, id),
            }

    def update(self):
        tabs = ITab.all_components(self.context, self.request)
        predict, _ = getSecurityGuards()
        if predict is not None:
            tabs = (
                (name, tab) for name, tab in tabs
                if predict(tab, swallow_errors=True) is not None)

        self._tabs = sort_components(tabs, key=sort_key)
        self.available = len(self._tabs) > 0
