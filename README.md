Tatoeba2 Django Bridge
====

This is a standalone python package to interface with tatoeba's db using django's orm. Should just work after you hook it up in your project.

Requirements
-----

django and python's mysql driver

```sh
pip install -r requirements.txt
```


Installation
----

grab it with pip:

```sh
pip install -e git+https://github.com/Tatoeba/dj-tatoeba2#egg=tatoeba2
```

Configuration
----

In your settings.py add it to your installed apps tuple:

```py
INSTALLED_APPS += ('tatoeba2',)
```

Also make sure the mysql server is running and the connection is properly configured in your settings.py
