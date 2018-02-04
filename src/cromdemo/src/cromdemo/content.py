
appRootSource="""

<h2>Welcome to the ZODB Demo.&nbsp;</h2>

<p>ZODB is an Object Oriented database written in Python.&nbsp; Just subclass off of class Persistent, and your application becomes persistent.</p>

<p>This demo showcases what is possible with the ZODB. &nbsp;In your browser,&nbsp; you can build a sophisticated&nbsp; web application just by adding&nbsp; HTML, CSS, Javascript, Python&nbsp; and Folder (Container) objects.&nbsp; They all have gorgeous editors, HTML objects have both a technical Ace Editor and a WYSIWYG ckEditor.&nbsp;</p>

<p>But this is not just a tool for end users.&nbsp; We invite you jump into file system development.&nbsp; See how easy it is to customize the existing TreeLeaf and TreeBranch objects, to build your own advanced applications.&nbsp;&nbsp;These web tools work well for both beginners and advanced users.&nbsp; Indeed there are hundreds of man years of excellent software engineering hiding under this pretty user interface.&nbsp;</p>

<p>I invite you to get started by <a href="./ckedit">editing this page</a>.&nbsp;</p>

<p>&nbsp;</p>

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
    <title>ZODB Demo</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="" />
    <meta name="author" content="" />
 
    </head>
    <body>
        ${structure:context(view)}
          ${structure: view.acquire('footer').source}
    </body>
</html>

"""


footerSource="""
<div style="padding-left: 30px;padding-right: 30px;"> 
<h3>Credits</h3>

<p><a href="http://https:zopache.com">Zopache</a>&nbsp;is built with the&nbsp;<a href="https://ace.c9.io/">Ace Editor</a>,&nbsp;<a href="https://ckeditor.com/">ckEditor</a>, the&nbsp;<a href="https://github.com/PythonLinks/ZodbDemo#zodb--cromlech--introduction-and-demo">Cromlech Toolkit</a>,&nbsp;<a href="https://www.docker.com/">Docker,</a>&nbsp;&nbsp;the&nbsp;<a href="http://https:python.org">Python</a>&nbsp;language,&nbsp; <a href="http://restrictedpython.readthedocs.io/en/latest/">Restricted Python</a> the object-oriented&nbsp;<a href="http://www.zodb.org/en/latest/">ZODB</a>&nbsp;database,&nbsp;&nbsp;<a href="http://uwsgi-docs.readthedocs.io/en/latest/">uwsgi</a>,&nbsp;<a href="https://readthedocs.org/projects/zopeinterface/">Zope.Interface</a>&nbsp;and many other libraries.&nbsp; Thanks to the innumerable open source volunteers who made this project possible.&nbsp;&copy; Christopher Lozinski 2018.&nbsp; Provided to you by <a href="http://PythonLinks.info">PythonLinks.info</a></p>
</div>
"""
from cromdemo.models import TreeRoot, TreeLeaf, TreeBranch
from zopache.ttw.html import HTML,  AceHTML

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
            
            appRoot['green'] = TreeLeaf(title='Green leaf', body='A summer leaf')
            appRoot['yellow'] = TreeLeaf(title='Yellow leaf', body='An automn leaf')
