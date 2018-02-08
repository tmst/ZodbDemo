<a id="introduction"></a>
ZODB + Cromlech  Introduction and Demo
=====================

ZODB is an Object Oriented database written in Python. Just subclass off of class Persistent, and your appliocation becomes persistent.

This demo showcases what is possible with the ZODB. In your browser, you can build a sophisticated website, by creating and graphically editing  HTML, CSS, Javascript and Folder objects (Containers). If you want to go further, it is easy to customize the existing TreeLeaf and TreeBranch Python classes.

USEFUL LINKS
-------------

There is lots of documentation [here](./DOCUMENTATION).

THe installation instructions are in [DOCUMENTATION/INSTALL.md](./DOCUMENTATION/INSTALL.md)


The [Major Interfaces](https://github.com/Cromlech/cromlech.browser/blob/crom/src/cromlech/browser/interfaces.py) are all defined here. While that may seem like a simple to understadn page, it took one person a long time to clear up the myriad concepts generated by the Zope + Grok committees and come up with this easy-to-understnd collection of interfaces.

You can read about [the security model](./src/cromlech/security/tests/test_secure_component.txt).

You may want to better understand [webob](https://docs.pylonsproject.org/projects/webob/en/stable/reference.html).

And read the [list of packages](http://trac.dolmen-project.org/wiki/technical-overview)


NOTES
---------

In general Cromlech has great detailed documentation, but it is all hidden in the doc tests. So always look for it there.

The objective of this software is to simplify and speed up software development.  There are many rich and wonderful libraries here. Like a Russian Bubudzka doll there is always another layer hidden below.

All of it is needed. It is the distilled wisdon of many people working on this for more than [20 years](https://en.wikipedia.org/wiki/Zope#History).

My ojective is to make it easy for you to get started, and yet possible to grow your applicatoin from there.
