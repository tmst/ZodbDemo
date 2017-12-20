Cromlech Introduction AND DEMO
=====================

Cromlech is a toolkit for building applications in Python. This demo
shows how to build a wsgi application, but it also
works without wsgi, either as a Python Script or even behind an asyncio or
Tornado server.  Cromlech supports both routing and traversal.  It supports
view lookup on objects.  It supports sessions, and security. I recommend
Cromlech as the best way to build applications on top of the Z Object
Database.  


There is lots of documentation [here](./src/cromdemo/docs).
You may want to start with 
a longer   [article](./src/cromdemo/docs/article.md) submitted to
PyCON USA 2018.

THe installation instructions are in [DOCUMENTATION/INSTALL.md](./DOCUMENTATION/INSTALL.md)

You will probaly need to understand the [webob api](https://docs.pylonsproject.org/projects/webob/en/stable/reference.html)

And read the [list of packages](http://trac.dolmen-project.org/wiki/technical-overview)

Please note that for historic and commercial reasons we are building this on
the crom branch of most of the cromlech packages.

In general Cromlech has great detailed documentation, but it is all hidden
in the doc tests.  So always look for it there.


