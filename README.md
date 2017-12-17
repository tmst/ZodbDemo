Cromlech Introduction AND DEMO
=====================

Installation instructions are in [INSTALL.md](./INSTALL.md)

Cromlech is a modern, clean implementation of the concepts first developed
in Grok. Its author, Souheil Chelfouh,  was one of the original
contributors to Grok, and he has taken the last 10 years to clean up Grok
and disentangle the various pieces.  So Cromlech  shares the same concepts
as Grok, but
has a much clearner implementation.  It runs in both Python 3 and Python 2.
It is in daily production use in a big company in Germany, and in
daily development use by its author Souheil. 

How does Cromlech differ from Grok? Both are based on the ZTK. Both have
object publishers.  Both use zope.security.  Both have a component registry.
Both have security on views.  But Grok is really a massive monolithic
framework, while Cromlech has done the miraculous job of
separating out the different pieces into a toolkit.  With Grok you
have to hae a ZODB.  You add applications.  Applications  have sites.  Sites
have registries, and users.  There is a big complexity overhead required by
Grok.

Cromlech is a toolkit, you get control over how you structure your
applications. Choose those pieces which you want.
At first I did not believe it possible, but the more I dug, the more I realized
it to be true.  Cromlech does not even require a ZODB, It can use one or
more root ZODB's. it can use dispatch, it can use traversal, it can dispatch,
and then traverse.   Cromlech can run as a WSGI server, a stand alone app, or a
async (such as Tornado) server.  Awesome.  Like ZTK Cromlech is a toolset.  But it also has two demos you can start with. 

For me the biggest reason is that Cromlech
is already running in Python 3, while Grok has some
15-24 packages which need to be ported.   

The next biggest advantage of cromlech is the Publisher called
[dawnligt](https://github.com/Cromlech/dawnlight).
It is very clean.  It
subclassses off of webob.  It works with or without a ZODB.
It support both traversal and routing, the two can be
mixed together, and the location tools preserve url reporting.
In comparison the grok pulishing process is a mess. 

The next reason to use Cromlech is that we are now much smarter
than when grok was written.
zope.formlib and z3c.form had way way too many adapters.  Cromlech uses
Zeam.form
which is much better designed.

Cromlech uses the more modern WebOb,
while grok/zope are still using the older zope.publisher.
If you take a look at the Zope.publisher source code, it does everything.
Way too complex to understand, let alone hack.  And zope.publisher
even calls zope.app.publisher.publication.
Cromlech is much simpler, cleaner readable and understandable.

The next big difference is  in the security model.  The
modern way to do security is security on views.
ZTK also does security on object access.
So Grok has to patch that leading to a lot of additional complexity.
Cromlech takes the simpler approach of directly downg security on views.
During traversal, you can optionally add in security on object access.
Cromlech got that one right.


Cromlech uses Zeam.form, while Grok uses
zope.formlib and Z3c.form.  The problem with the later two is that they
have a lot of extra adaptors, leading to unnecessary complexity.  Even
Jim Fulton said something like: “We used way too many adaptors.”  And of
course zeam.form can also be used with Grok or Plone.

Cromlech has a very simple, yet powerful security and authentication  model.
Before beginning traversal wrap the Publication class in an authentication
decorator. Unauthenticated users will be challenged.  Wrap secure views with a
security decorator.  

Cromlech has a new component registry.
While it is plug compatible with the old registry, it allows for chaining of
registries.  Think a tree of registries. In contrast Grok has both local and
global registeries.  The Cromlech approach makes more sense.

Cromlech startup is a bit different than Grok.  Grok just had one way to
start up.  Cromlech has an app.py file which configures your startup.
It gives you a much more flexible  approach than the grok approach. 


Martian Vs Venusian.
Grok does configuration using martian.  Cromlech
uses Venutian.  What is the difference?

Martian  uses declarations.   Here is an example.

```
class AuditAccount(grok.View):
   grok.context(IAccount)
   grok.name ("audit")
   grok.require("banking.auditAccount")
```

Venutian uses decorators  Here is an example from the Pyramid documentation.
Although I believe the cromlech decorators are a bit different.


```
@view_config()
def my_view(request):
    """ My view “""
    return Response()
```

The senior developers prefer decorators.  Simpler to implement and do not 
inherit.  The junior developers prefer martian.  Easier to understand.  
Does inheritance properly.  In many cases you do not have to do anything, 
inheritance does it for you.  It looks just like regular code.  But of 
course open source is written by the senior developers, for the senior 
developers, so Martian has sadly mostly passed out of use.  
For those who do prefer Martian, the good news is that it is already running on
Python 3.  But there are many special grokkers in Grok, and reportedly as of 
middle 2017, not all of them work  with Martian on Python 3. 

It should e reasonably doable to port Grok Model Objects and views to Cromlech. 
Once I figure out the Cromlech libraries, it should not be that 
hard to port a Grok application over.  My hope is that porting a Grok 
application to Cromlech will only require upgrading a few grok packages to 
Python 3.  Time will tell. 

So why not just use Pyramid?  The reason that I like Grok or Cromlech is
that they are rich environments.  They give you a lot of concepts to build
on.  In contrast Pyramid is quite stripped down.  Optimized for computer speed,
rather than ease of development. So Pyrmaid tossed out zope.security in foavor
simplistic Access Control Lists.  Pyramid hides the component registry under
a simpler api, and only uses it for view lookups. Pyramid does not include
zope.interface and CRUD.  Choose your own forms libraries. 
In particular the wonderfully expressive zope.securitypolicy has not
been ported to Pyramid.  Maybe it cannot be because Pyramid does nto use 
zope.security.

The other problem with Pyrmaid  is that itt only works
as a WSGI server, whereas Cromlech is more a collection of separate tools.
Let us take a look at the limitations of running Pyramid with Tornado.  
Reportedly you can only run Pyramid as a single thread.
https://stackoverflow.com/questions/29496870/how-to-use-pyramid-with-tornado
Whereas with Cromlech you can call app.py from a tornado process and run 
as many threads as you want. 

Is Cromlech perfect?  Well no.  The biggest prolem is the lack of 
documentations.  The author has put his focus on the code.  
So I am busy writing documentation. If
you are a grok or zope developer, then you understand the basic concepts. 
There is enough documentation here to get you oriented and started.  
And if you have any questions, the tech support is just brilliant.  
Not only are the text answers
on the irc freenode channel #dolmen excellent, but whenever 
I have run into a problem
the author getes me a new release the next day, often staying up late 
to do so. 

This is not just some open source library someone drafted.  This represents 
a world
view of how software should be done.  Our professional identiies are tied up 
with this work.  Very much a labor of love.  Those of us who are working 
on this 
software really care about it, and want you to have a good experience.  We 
invite you to try it out.  Just be nice in your feedback. 

There are additional docs [here](./src/cromdemo/docs) including 
a longer   [article](./src/cromdemo/docs/article.md).

You will probaly need to understand the [webob api](https://docs.pylonsproject.org/projects/webob/en/stable/reference.html)

And read the [list of packages](http://trac.dolmen-project.org/wiki/technical-overview)
