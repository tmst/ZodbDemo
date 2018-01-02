ZODB + Cromlech  Introduction and Demo
=====================

This demo showcases a small subset of what is possible with Cromlech and the
ZODB.  

ZODB is an Object Oriented database written in Python.  Just subclass off of
class Persistent, and your appliocation becomes persistent. 

There are multiple ways to build applications on top of the ZODB.  I recommend
Cromlech.

Cromlech is a conceptual framework for building Python applications.  But
software needs more than concepts, it needs definitions, so Cromlech is 
a set of interfaces which define  those concepts, and
a specific implementation of those interfaces.

So what are the concepts driving Cromlech? They are carefully
specified  by the
[interface definitions](https://github.com/Cromlech/cromlech.browser/blob/crom/src/cromlech/browser/interfaces.py).  Cromlech WSGI Interfaces define what
services the wsgi server  must provide. 
You probably already have an intuitive understanding
of what are request and resposne.

Next up Cromlech defines publishers and Publication Root.  An object
pulisher starts at the publication root, traverses to an object, 
displays a view on it, and returns the Response.
And of course Cromlech defines the interfaces for  Forms, Templates URLs
and sessions. 

This demo shows how to build a wsgi application using the ZODB,
but Cromlech  also can work without wsgi and without the ZODB,
either as a Python Script or even behind an asyncio or
Tornado server.  Cromlech supports both routing and traversal.  It supports
view lookup on objects.  It supports sessions, and security.

You may now want to go and read all  [about the demo](./DOCUMENTAION/GentleIntroduction.md)


USEFUL LINKS
-------------

There is lots of documentation [here](./DOCUMENTATION).
You may want to start with 
a longer   [article](./DOCUMENTATION/Article.md) submitted to
PyCON USA 2018.


THe installation instructions are in [DOCUMENTATION/INSTALL.md](./DOCUMENTATION/INSTALL.md)


The [Major Interfaces](https://github.com/Cromlech/cromlech.browser/blob/crom/src/cromlech/browser/interfaces.py) are all defined here.  While that may
seem like a simple to understadn page, it took one perosn
a long time to clear up the myrad of concepts generated by the
Zope + Grok committees
and come up with this easy-to-understnd collection of interfaces. 


You may want to better understand [webob](https://docs.pylonsproject.org/projects/webob/en/stable/reference.html).

And read the [list of packages](http://trac.dolmen-project.org/wiki/technical-overview)


NOTES
---------

Please note that for historic and commercial reasons we are building this on
the crom branch of most of the cromlech packages.

In general Cromlech has great detailed documentation, but it is all hidden
in the doc tests.  So always look for it there.

The objective of this software is to simplify and speed up software
development.  There are many rich and wonderful libraries here. Like a
Russian Bubudzka doll there is always another layer hidden below.
All of it is needed.  It is the distilled wisdon of many people working
on this for more than [20 years](https://en.wikipedia.org/wiki/Zope#History).
My ojective is to make it easy for you to get started, and yet possible
to grow your applicatoin from there.