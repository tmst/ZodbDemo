
appRootSource="""

<h2>Welcome to the ZODB Demo.&nbsp;</h2>

<p>ZODB is an Object Oriented database written in Python.&nbsp; Just subclass off of class Persistent, and your application becomes persistent.</p>

<p>This demo showcases what is possible with the ZODB. &nbsp;In your browser,&nbsp; you can build a sophisticated&nbsp; web application just by adding&nbsp; HTML, CSS, Javascript, Python&nbsp; and Folder (Container) objects.&nbsp; They all have gorgeous editors, HTML objects have both a technical Ace Editor and a WYSIWYG ckEditor.&nbsp;</p>

<p>But this is not just a tool for end users.&nbsp; We invite you jump into file system development.&nbsp; See how easy it is to customize the existing TreeLeaf and TreeBranch objects, to build your own advanced applications.&nbsp;&nbsp;These web tools work well for both beginners and advanced users.&nbsp; Indeed there are hundreds of man years of excellent software engineering hiding under this pretty user interface.&nbsp;</p>

<p>I invite you to get started by <a href="./ckedit">editing this page</a>.&nbsp;</p>

 """

indexSource=""" 
 <!DOCTYPE html>
<html lang="en">
  <head>

   <script
        src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha256-k2WSCIexGzOj3Euiig+TlR8gA0EmPjuc79OEeY5L45g="
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <meta charset="utf-8" />
    <title> ${view.acquireTitle()}</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="" />
    <meta name="author" content="" />
       <link rel="stylesheet" href="/css" />

    </head>
    <body>
        <center>
            <h1> ${view.acquireTitle()}</h1>
        </center>
         <style>
              div {
          padding-left: 30px; 
          padding-right:30px;
          
      }
       </style>  
   
        
        <div>${structure: view.acquire('Menu')(view)}</div>
        <div> ${structure: view.breadcrumbs()}</div>

        <div> ${structure:context(view)}</div>
        <div>${structure: view.acquire('footer').source}</div>
        
    </body>
</html>


"""
cssSource="""
      #siteheader a {
         color: white;
         text-decoration: none;
      }

      #main {
          padding: 1em;
      }

      #content {
          margin: 1em;
      }
      
      #footer {
          color: white;
	  background-color: #464c4a;
	  padding: 2em 0;
	  margin-top: 2em
      }

      #footer a {
	  color: white;
	  font-weight: bold;
      }

      #siteheader {
	  width: auto;
	  background-color: #004a96;
          margin-bottom: 0em;
          color: white;
      }

      .header-action {
          margin-top: -2em;
      }

      .form-group.required label:after {
          content: "•";
          color: red;
	  padding-left: 0.3em;
	  font-weight: bold;
      }
"""

footerSource="""

<h3>Credits</h3>

<p><a href="http://https:zopache.com">Zopache</a>&nbsp;is built with the&nbsp;<a href="https://ace.c9.io/">Ace Editor</a>,&nbsp;<a href="https://ckeditor.com/">ckEditor</a>, the&nbsp;<a href="https://github.com/PythonLinks/ZodbDemo#zodb--cromlech--introduction-and-demo">Cromlech Toolkit</a>,&nbsp;<a href="https://www.docker.com/">Docker,</a>&nbsp;&nbsp;the&nbsp;<a href="http://https:python.org">Python</a>&nbsp;language,&nbsp; <a href="http://restrictedpython.readthedocs.io/en/latest/">Restricted Python</a> the object-oriented&nbsp;<a href="http://www.zodb.org/en/latest/">ZODB</a>&nbsp;database,&nbsp;&nbsp;<a href="http://uwsgi-docs.readthedocs.io/en/latest/">uwsgi</a>,&nbsp;<a href="https://readthedocs.org/projects/zopeinterface/">Zope.Interface</a>&nbsp;and many other libraries.&nbsp; Thanks to the innumerable open source volunteers who made this project possible.&nbsp;&copy; Christopher Lozinski 2018.&nbsp; Provided to you by <a href="http://PythonLinks.info">PythonLinks.info</a></p>

"""

menuSource= """
<nav class="navbar navbar-inverse">
<div class="container-fluid">
<div class="navbar-header">
<a class="navbar-brand" href="#">ZODB Demo</a>
</div>
<ul class="nav navbar-nav">
<li><a href="/">Home</a></li>


<li class="dropdown" tal:condition="view">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
Add  <span class="caret"></span></a>

<ul class="dropdown-menu">
<li><a href="./addContent">Add Content</a></li>
<li><a href="./addContentContainer">Add Container</a></li>
</ul>
</li>
<li><a href="./manage">Manage</a></li>




<li><a href="./logout">Logout</a></li>
</ul>
</div>
</nav>
"""

from cromdemo.models import TreeRoot
from zopache.ttw.html import HTML,  AceHTML
from zopache.ttw.css import CSS

def initialize(root):
            appRoot = root['applicationRoot'] = TreeRoot()
            appRoot.source=appRootSource
            appRoot.title= 'ZODB Demo'
            
            index=AceHTML()
            index.title='The page layout'
            index.source=indexSource
            appRoot['index']=index

            footer=HTML()
            footer.title='The footer html'
            footer.source=footerSource
            appRoot['footer']=footer

            css=CSS()
            css.title='Home Page CSS'
            css.source=cssSource
            appRoot['css']=css    

            menu=AceHTML()
            menu.title='HTML For the User Menu'
            menu.source=menuSource
            appRoot['Menu'] = menu

