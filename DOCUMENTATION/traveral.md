Object Publishing
================

So this is where the magic happens.  Magic is difficult. 

The model is that we first find an object, then display the view on it.

We take the URL and divide it into segments, that creates the stack.

https://mysite.com/path/to/model/object/optional-view

Starting at the root, we get the next object.


1 First we see if there
is a method with that name, and a traversale decorator.
If so, we execute that method and traverse to that object.  No arguments
allowed to the method, just self.

2 Then we see if this is a container with a __getitem__ method.  If so, we try to
do context[segnemnt-name].  Where we pop segment-name off of the stack.

3If that fails, then we try a custom traverser.

4 And then we try to look up a view with that name on the context.

5And if there is nothign left in the stack, we try to look up the default view.

[About dawnlight](https://github.com/Cromlech/dawnlight) Object Publishing.

Cromlech.dawnlight [docs](https://github.com/Cromlech/cromlech.dawnlight) Object Publishing.

Zopache does it a bit differently.  While Cromlech does strict separtion,
models first, then views. zopache also looks up templates.

Beter to use a namespace for a tempalte. 

https://mysite.com/path/to/model/object/optional-template/optional-view

https://mysite.com/path/to/model/object/template
https://mysite.com/path/to/model/object/template/view
https://mysite.com/path/to/model/object/view
https://mysite.com/path/to/model/object/  Default Template + DefaultVIew
https://mysite.com/path/to/model/object/  Default Temaplate
https://mysite.com/path/to/model/object/  Default View
https://mysite.com/path/to/model/object/  

ALGORITHM
==========
So you get seven cases,
So if the template has already been found, and there is a view look up the view on
that tmeplate. 

If there template has already been found and there is no view, look up the default view on the template.

Traverse the methods.

Traverse the container objects.

Do a name space traverser.

Look up the view on the context.
     If the context is a template tell it so.
     
Look up the default view on the context.

Look up the  template.

Look up the default template. 

