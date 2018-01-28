
appRootSource="""<h2>Welcome to the ZODB Demo.&nbsp;</h2><p>&nbsp;</p><p>
    ZODB is an Object Oriented database written in Python.&nbsp; 
    Just subclass off of class Persistent, and your appliocation becomes persistent.</p><p>This 
    demo showcases what is possible with the ZODB. &nbsp;In your browser,&nbsp; you can build a 
    sophisticated</p><p>website, by creating and graphically editing&nbsp; HTML, CSS, 
    Javascript and Folder objects (Containers).&nbsp; If you want to go further, it is easy to 
    customize the existing TreeLeaf and TreeBranch Python classes. &nbsp; These web tools work 
    well for both beginners and advanced users.&nbsp;</p><p>I invite you to get started by 
    <a href="./ckedit">editing this page</a>.&nbsp;</p><p>&nbsp;</p>
            appRoot['green'] = TreeLeaf(title='Green leaf', body='A summer leaf')
            appRoot['yellow'] = TreeLeaf(title='Yellow leaf', body='An automn leaf')
            transaction.manager.commit()
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
        ${context(view)}
         
    </body>
</html>"""
