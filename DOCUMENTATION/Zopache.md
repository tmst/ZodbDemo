What I am building
===================

I am in the process of building Zopache on top of Cromlech.  Here
is some documentation of what I am building. 

Cromlech provides very powerful and flexible concepts, but it takes a while to learn and deeply understand these concepts.  That is a significant barrier to entry in a Scrum world where your boss wants to see something today.  To ease this transition Zopache provides a number of tools.

Basic Web Objects
Basic Web Objects make it easy to put up a simple web site.  Basic web objects include Folder, HTML, CSS, Javascript, Image, and File objects.  Folders allow you to create a tree of objects. Each object has its own URL.  HTML, CSS, and Javascript objects all hold the relevant content type and all support the gorgeous browser-based ACE editor and syntax checker.   HTML objects also support the WYSIWYG ckEditor.  Image objects store images.   
 
Folder
A Folder in Zopache is much like a folder on your operating system.  But instead of holding static files, it holds dynamic objects.  You can add objects to it.  You can also select items using the check boxes on the left of each row, and cut, copy or delete them.  Once you copy them, a paste option appears, to paste the copies into the current folder. Navigate to the folder where you want to put those copied objects,and hit the paste button.  


HTML
HTML objects are the core of any website. Zopache makes them easy to edit from anywhere in the world, using your regular web browser. No need to become a Unix System Administrator!  The CkEditor is a WYSIWYG HTML Editor.  The ACE editor is more technical.


CSS
CSS objects are edited with the ACE editor, which checks their syntax.  

Javascript
Javascript objects are edited with the syntax checking Javascript editor.  We have both Javascript Objects and Javascript folders.  A javascript folder allows one to have every javascript function in a separate file, but merges all of them into a single (soon minified) file when served to the client.

File objects allow one to upload a file to the website.
Image objects allow one to upload images.  When called they autogenerate the correct HTML tag.
