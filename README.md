Cromlech Introduction AND DEMO
=====================

Cromlech is a rich web framework, a great way to build applications on top
of the Z Object Database.

Installation instructions are in [INSTALL.md](./INSTALL.md)

There is lots of documentation [here](./src/cromdemo/docs)

You will probaly need to understand the [webob api](https://docs.pylonsproject.org/projects/webob/en/stable/reference.html)

And read the [list of packages](http://trac.dolmen-project.org/wiki/technical-overview)

including 
a longer   [article](./src/cromdemo/docs/article.md).


Zope and Cromlech support object publishing. Find an object, find the appropriate view on the object, execute the view, and return either some json, a web page or a viewlet for that object.

Cromlech supports multiple ways to find an object. Either routing or traversal of one or more relational or object databases can be performed. One can mix and match, for example, first route, then traverse, then route again.

Zopache simplifies finding objects. It only does traversal of one ZODB.

Once the python model object has been identified, Cromlech looks up a view on that object, executes it and returns the result.

Views are looked up using a component registry. Cromlech offers a tree of registries. If registration cannot be found in one registry, it is looked for in the parent registry.

Zopache registers the views on basic web objects for you. These include HTML, CSS and Javascript objects.

Cromlech builds on Zope.security. zope.security has a concept of principals. Principals have permissions. Cromlech allows one to wrap either views or objects in security proxies. They can then only be accessed if the current principal has the correct permissions. Otherwise an exception is thrown, and usually the application redirects to a login page.

Zopache simplifies this. The admin has CRUD permission, the anonymous user has view permission.

If you want a richer security model,
Zope.securitypolicy provides a rich security framework. Principals and groups of principals have roles. Principals, Groups and roles can be granted or denied permissions either globally or on arbitrary
branches of a ZODB tree. My website PythonLinks.info is based on
zope.securitypolicy. I love it.

There are two times when security proxies are accessed. If a view is wrapped ina security proxy, then when the view is called, the security proxy is first executed. If there is permission the view is executed, if not an exception is thrown and the user is usually redirected to a login panel.

During traversal, or routing, objects can also be wrapped in a security proxy. To then access that object, the appropriate permissions have to be in place,
or again an exception is thrown.

A wonderful thing and unique thing about Cromlech is that security proxies on views and objects are optional and can be mixed and matched.


Every prototype application needs CRUD. Zope.interface defines the editable attributes on an object. Zeam.form creates the Crud forms. The older zope.formlib and z3c.form are in a well earned retirement. They required way to many adaptations to be understandable. Code for a Zeam.form will be shown.

Zopache simplifies cromlech for beginners by providing CRUD for containers, HTML, CSS and Javascript objects.

An important part of zopache is managing the objects in a container. One needs to be able to select, delete, rename, copy and move those objects. The zopache.zmi, provides this functionality, through-the-web.

Adapters are an important part of the Zope world. They are not special to the Cromlech, but they do deserve to be covered. Views are adaptors of the displayed objects, but there are other types of adaptors. Zopache.CopyPasteMoveDelete being the best example I know. When using the ZMI on different objects, they need to be treated differently. We are really operating on a graph of objects, and different objects interact differently with that graph. So based on adaptors the Zopache ZMI does the right thing to each object. Let us see some examples.

Some objects have canonical URL's. This was coverered in my ZODB talk, the slide will be shown again. When these objects are renamed, the canonical name needs to be changed. When they are deleted, the canonical name needs to be deleted.

Some objects may be indexed in catalogs. On deletion they need to be removed from the catalog.

Some objects may be referenced from another part of the tree. Deleting that object, may require that a reference to that object be changed to None.

Some objects may have copies in another part of the tree. A so called Simese Twin. For example content objects may be present in the authors home directory, and in a shared published group directory. I beliee Reddit does this, although not in Python. Renaming or moving that object requires that its siamese twin also be moved or renamed.. As the complexity of the object graph increases, Adaptors make it easy to keep things correctly organized.

Since HTTP is a stateless protocol, Sessions are an important part of modern web applications. Cromlech supports both JWT sessions and traditional cookie based sessions. The application gets wrapped in either type of session manager. Before traversing the graph, the session manager is invoked and the person is authenticated or declared to be the unauthenticated principal.

Zope and grok were massive frameworks, you could not throw out any part.
Miraculously, cromlech is more of a toolset. One can build lots of different server configurations with Cromlech. One can choose which pieces to use.

The first thing one does in Cromlech is to configure the server. I will show you the configuration file for Zopache, and explain what every line does.

Here is a description of the [configuration file](https://github.com/PythonLinks/CromlechDemo/blob/master/src/cromdemo/docs/configuration.txt).

Competition.
The market leaders in Python web servers are Django, Pyramid and Flask. So why not use them?

Django is for mapping a website, a tree of web pages into a relational table. It just does not fit. Routes can be quite complex. Usually one first gives the table name, then the object name. I will show an example of how Traversal leads to a much simpler URL map.

Flask is a very stripped down web framework. Pyramid also. In contrast the Zope world provides a much richer vocabulary for building websites, and Cromlech does something I had not thought possible, it breaks it down into a toolkit, where the individual components can be used separately from each other.

On the ease of use side, Django is pretty good. It has tools for bringing up applications quite easily. Flask, I believe does not. Pyramid has SubstanceD, but that only allows one to create content types, it is by no means a TTW Javascript IDE. Zopache makes for a much easier introduction into these tall software stacks.  