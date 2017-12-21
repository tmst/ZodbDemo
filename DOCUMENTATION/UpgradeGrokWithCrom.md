Cromlech provides an upgrade path for Grok applicatoins. 

Cromlech is a close relative of Grok (and Dolmen).
It was written by Souheil Chellfou a major contributor to Grok.
https://pypi.org/user/trollfot/ Cromlech is in production use in a
German company which is supporting it on an ongoing basis.

There are two version of Cromlech. The master branch is very Grok compatible.
The crom branch is running on Python 3.

I have been hard at work learning and documenting the crom branch and upgrading
the crom branch demo.  github.com/pythonlinks/CromlechDemo

The crom branch is a very impressive piece of work.  Souheil has spent the
last 10 years cleaning up and refactoring
grok. Crom has the same concepts as Grok, but a
much cleaner implementation. Time after time I read the code, and
say, man this is so much better than the Grok version.
Grok is a framework: each piece needs
the other pieces.  In contrast,  Cromlech is a library,
the pieces are quite separate. I would not have thought it possible.

I do not know as much about the Master branch of Cromlech.  
I am just about to dig into it.  It is still in
Python 2, but is quite grok compatible. 

I see three ways of using Cromlech to
upgrade Grok.  The first is wait until the German client pays for the upgrade
to Python 3 (Trollfot: Scheduled for 2018?).  The second is use the master
branch as is. I believe what that does is toss out zope.publisher, and
zope.app.publisher, and replaces them with a Dawnlight publisher.
(Trollfot:Is that correct?)
It would aslo have to replace grok.view. 
Dawnlight is based on webob, and uses the uwsgi software stack.
https://github.com/Cromlech/cromlech.dawnlight
The docs should be in the tests.  

The other option is to migrate your content objects to the crom branch. 
The devil is always in the details but here is what I think is possile.

The biggest difference is in the Crom registry.  (Trollfot: Is it plug
compatile?  Is it a superset of functionality of Zope registry?) The next
biggest difference is that Cromlech uses Venutian Decorators rather than
Grok's martian declarations.  Actually Martian is already in Python 3,
so it should be reasonably easy to port it to Crom. Zeam.form
has already been ported to the Crom Registry.

The third issues is that Crom uses zeam.form rather than zc.form and
z3c.form.  Not that much difference there really, just fewer adaptors.


What about Documentation?
Historically
Souheil prioritized software over documentation, so they were hard to access.
It turns out that Cromlech actually includes lots of detailed
documentation, but
it is all hidden in the doc tests.
I have been busy writing high level docs.


So what is the bottom line?

For new projects the Cromlech Demo is a reasonale place to start.
Soon it will be a great place to start. 
Indeed I am
off giving talks about he ZODB, and recommending Cromlech as a starting point
for ZODB applications.  And I am working to improve Crom,
and to port Zopache to it.

For older projects, there is some great softwre here.  I am
busy figuring out how to integrate it with my existing grok
applications.

Comments are most welcome. But I now think that I kind of like
the typical PyCon code of conduct rules.  










