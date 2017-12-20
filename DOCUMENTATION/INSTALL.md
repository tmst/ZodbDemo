

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