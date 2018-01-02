Why ZODB + Cromlech
=============

The software tools you use determine the concepts you can leverage.

The ZODB gives us a persistent graph of Objects.  Cromlech
then allows us to traverse that graph, and select the appropriate
view for those objects. We can also adapt objects.  And do security on
Objects or views.  Most importantly it is not a framework, it is a toolkit.
So we only use what we want to use. 

I invite you to read [Cromlech Vs Django](./CromlechVsDjango.md)

I invite you to read [Cromlech Vs Pyramid](./CromlechVsPyramid.md)

Flask and Pyramid offer, a very stripped down web framework.

In contrast the
Cromlech  world provides a much richer vocabulary for building websites, and
Cromlech does something I had not thought possible, it breaks it down into
a toolkit, where the individual components can be used separately from each
other. So you do not have to import the whole framework, just the parts that
you need. 
