Installation instructions with Explanation
========================

These are installation instructions assuming that you have a unix server.
First fire up bash, then get a copy of the git repository.

```
bash
$> git clone https://github.com/PythonLinks/CromlechDemo
```

Now we install a virtual env.

For python3.3+

```
$> pyvenv .

#  OR WHAT I HAD TO DO ON LINUX WHERE THE DEFAULT PYTHON IS 2.something
#  virtualenv -p /usr/bin/python3 .

$> source bin/activate
```


When you first download this there is a file in the root called bootstrap.py.
you run
```
$>python bootstrap.py 
```
to create bin/buildout.

Then you run
```
$>bin/buildout
```

, it downlaods all the required software, and creates
all the files and directories needed to run the application.
In particular it creates config.json, which includes all the Python Path
information.

$>pip install uwsgi

And now we run the application.
```
$> uwsgi --http :8080 --wsgi-file server.py
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
```
$>bin/develop update
```

to update all the packages which have been downloaded. 