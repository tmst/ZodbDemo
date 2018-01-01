

Installation instructions are below.

For python2.7+
--------------

```
bash
$> git clone https://github.com/PythonLinks/CromlechDemo
$> virtualenv .
$> source bin/activate
$> python bootstrap.py
$> ./bin/buildout
$> pip install uwsgi
$> uwsgi --http :8080 --wsgi-file server.py
```


For python3.3+
--------------

```
bash
$> git clone https://github.com/PythonLinks/CromlechDemo
$> pyvenv .

#  OR WHAT I HAD TO DO ON LINUX FOR PYTHON 3
#  virtualenv -p /usr/bin/python3 .

$> source bin/activate
$> python bootstrap.py
$> ./bin/buildout
$> pip install uwsgi
$> uwsgi --http :8080 --wsgi-file app.py
```
To debug the uwsgi easily, just use : --honour-stdin, in the
command line when launching it.
it will allow you to use PDB without problems.
You can also reduce the number of workers to 1.
Use the option -p 1

Here is the command I use. 
 uwsgi --http :8081  -p1  --honour-stdin --wsgi-file server.py

Note that port 8081 works for me, you may want a different port number.

And when you download a new versoin use the commands
bin/develop update

to update all the packages which have been downloaded. 