Installation instructions with Explanation
========================

These are installation instructions assuming that you have a debian server.
Python 3 please.

First the commands, then explanations.

$>bash
$>git clone https://github.com/PythonLinks/Demo
$>cd Demo
$>virtualenv -p /usr/bin/python3 .
$>source bin/activate
$>python bootstrap.py
$>bin/buildout
$>uwsgi --http :8081 -p1 --honour-stdin --wsgi-file server.py


Here is how to install venv.
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash


First fire up bash, then get a copy of the git repository.

```
$>bash
$> git clone https://github.com/PythonLinks/CromlechDemo
```

Now we install a virtual env.

If your server's main python in python3.3+

```
$> pyvenv .
$> source bin/activate
```

#  OR WHAT I HAD TO DO ON LINUX WHERE THE DEFAULT PYTHON IS 2.something
```
$>virtualenv -p /usr/bin/python3 .
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

And of coures in the unlikely event that  you install multiple times,
then your browser gets a key, but the server key is different.
So you get a jwt error. 