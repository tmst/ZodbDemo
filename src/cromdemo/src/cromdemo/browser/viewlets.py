# -*- coding: utf-8 -*-
#This software is subject to the CV and Zope Public Licenses.

from crom import order
from crom.utils import sort_components
from dolmen.viewlet import viewlet, Viewlet
from cromlech.browser import IURL, slot
from cromlech.browser.directives import title
from cromlech.security import getSecurityGuards, permissions
from zope.interface import implementedBy

from . import tal_template
from ..interfaces import ITab 
from zopache.core.layout import SiteHeader, AdminHeader, ContextualActions
from zopache.core.layout import Footer, Breadcrumbs
from dolmen.breadcrumbs import BreadcrumbsRenderer
from cromlech.browser import IView
from zopache.crud.interfaces import IWeb
from zopache.crud.interfaces import IApp
from zopache.ttw.interfaces import IHistoricDetails
import operator
from zopache.ttw.interfaces import IHTML, IHTMLClass

from ..content import footerSource
@viewlet
@slot(Footer)
class Footer(Viewlet):

    def render(self):
        return footerSource


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
        crumbs = BreadcrumbsRenderer(self.context,self.request)
        crumbs.update()
        return crumbs.render()

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


@viewlet
@slot(ContextualActions)
class Tabs(Viewlet):
    template = tal_template('tabs.pt')

    def tabs(self):
        context=self.context
        url = IURL(context, self.request)
        view=self.view 
        views=IView.all_components(view.context, view.request)
        result = []

        #THE VIEW LOOKUP INDEX ON ORDINARY OBJECTS
        if (IHTML.providedBy(context) and not
            IHTMLClass.providedBy(context)):
            result.append( {
                'active': False,
                'title': 'View',
                'url': url,
            })
        
        for item  in views:
            id=item[0]
            aClass=item[1]
            #THE Logout View is not part of crud. 
            if id=="logout":
               continue

            #Dont show add custom user's classes
            if IApp.implementedBy(aClass):
                   continue
               
            # Don't show add HTML CSS Javascript Image
            if IWeb.implementedBy(aClass):
                   continue

            #These are only accessed from History Page   
            if IHistoricDetails.implementedBy(aClass):
                   continue
               
            if ((id =='edit') and IHTML.providedBy( view.context)): 
               continue

            result.append( {
                'active': self.view.__class__ is aClass,
                'title': title.get(aClass) or id,
                'url': '%s/%s' % (url, id),
            })
        result.sort(key=operator.itemgetter('title'))
        return result        

    def update(self):
        tabs = ITab.all_components(self.context, self.request)
        predict, _ = getSecurityGuards()
        if predict is not None:
            tabs = (
                (name, tab) for name, tab in tabs
                if predict(tab, swallow_errors=True) is not None)

        self._tabs = sort_components(tabs, key=sort_key)
        self.available = len(self._tabs) > 0
