CromlechCromDemo
================

Here we have one of two Crom Demos.  The other one is
[here](https://github.com/Cromlech/Crom_ZODB_SQL_demo) and
includes a cromlech introduction.

This demo  does not use the ZODB, but it does more than the ZODB demo.
It creates a root node, with two leaves.
You have two forms.  One to edit the leaves.  One to login.

Before you get started, let me note that there is a lot of complexity here.
All of it is needed.  It is the distilled wisdon of many people working on this
for more than [20 years](https://en.wikipedia.org/wiki/Zope#History).
Even I, the author of this document, had to go back and read it multiple times,
each time going one layer deeper in understanding what is going on.  So be
patient with yourself.  

So what does all of this software do?

There is a lot going on in not many lines of code here.  At first it can be
a bit hard to follow, so let me describe in English what it does.

When you first download this there is a file called bootstrap.py.
You run
python bootstrap.py to create bin/buildout.

When you run bin/buildout, it downlaods all the required software, and creates
all the files and directories needed to run the application.
In particular it creates config.json, which includes all the Python Path
information.

So what does actually Cromlech do?

So first you have to understand that Cromlech is a toolkit.  There are many
ways to configure it.  This is but one configuration.

In loader.py there is something called PythonConfiguration.
It imports config.json to create
the Python Path that the application uses to search for
Python definitions. 

So first take a look at server.py.
Server.py  defines all the things required to configure the servers.
That sets up the wsgi server, and calls the
[demo_application](./src/cromdemo/src/cromdemo/demo.py).

And finally there is app.py.    That is where the application functionality
is defined.

Cromlech uses a concept called object publishing.   When your browser goes
to a url, the wsgi server calls a Python application.  And it passest a
bunch of variables to that Python application in a request object.  The
object publisher first looks up the object,
then it looks up the view on that object.
It executes the view and returns the result.


That is the simple story.  Security requirements make things even more
complex than that. You can either secure your views or not.  If you do not
secure your views, then the above description holds.  Everything is easy.
If you do secure your views or objects.  Cromlech wraps them in a security
proxy.  When you try to access or call them, the security machinery is invoked.
The first thing the security machinery does is to check if you are logged in.
If not, if you are the anonymous user, then you do not have permission, it
throws an exception, and you have a chance to login. If you are logged in,
then it it checks what permission is required, and whether you have that
permission or not.

This is a very simple security model.  If you want a much more sophisticated
model, I recommend zope.securitypolicy.

How does it know if you are logged in or not or who you are?
The request stores its values in a dictionary called
environ. That may include cookies.  And the cookies may include the
identity of the logged in user.  So before calling the application it has
to create a user session, and convert that cookie into a user name.  And
if there is a user name, it has to convert that name into a Zope principal
object, used by zope.security, or into the unauthenticaed user.

And then at the end, when object publishing executes the view, to generate
the response object,  the security machinery will be
invoked.  Of course security is only invoked if you have used a decorator
to declare something to be a protected view.
If the called view is protected, the security will check if it is a logged
in principal,  what permissions are needed for
that view, and  if the principal has those permissions.  If all is
well, the view is rendered,  otherwise a security exception is thrown,
and the user is
redirected to a login page.

How is all this implemented?
Before you get to the Application several things happen in decorators.

Before calling the application, the sessiond decorator is called.  It checks
to see if there is a session, if so it sets
environ[“username”]= uername

If there is a username, it then creates a principal.

There is a lot going on here.  Even for an experienced zope developer, it
takes a while to get it all.  But once you understand the abstractions, many
things are made simple, and your productiivty will rapidly increase. 

Okay, now let us take a loot at the structure of the software.

Here are the files.
The following files are included.

bootstrap.py
loader.py
server.py
          auth.py
          models.py
          security.py
          app.py
          browser
             forms.py
             layout.py
             views.py
             templates
                home.pt
                layout.pt
                leaf.pt
                tabs.pt

There are 4 templates. The layout gives the overall appearance.  There is a
home page tempjlate, a leaf template  with a link to a protected view.
And a tabs template.

There is a layout.py file.  It includes a layout object.  And within the
layout there can be two viewlets.  One to show a protected view.
And one to show actions. 


Installation instructions are below.

For python2.7+
--------------

```bash
$> virtualenv . && source bin/activate
$> python bootstrap.py
$> ./bin/buildout
$> pip install uwsgi
$> uwsgi --http :8080 --wsgi-file server.py
```

For python3.3+
--------------

```bash
$> pyvenv . && source bin/activate
$> python bootstrap.py
$> ./bin/buildout
$> pip install uwsgi
$> uwsgi --http :8080 --wsgi-file app.py
```
To debug the uwsgi easily, just use : --honour-stdin, in the command line when launching it.
it will allow you to use PDB without problems.
You can also reduce the number of workers to 1.
Use the option -p 1

 uwsgi --http :8081  -p 1 --honour-stdin --wsgi-file server.py

Note that port 8081 works for me, you may want a different port number. 