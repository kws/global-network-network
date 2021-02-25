Django Starter Project
======================

This is a project for us to experiment with [Django](https://www.djangoproject.com/)
which is a web framework that makes developing web applications quick and with
minimal amounts of code.

We will roughly follow the plan of the 
[Django Tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
without a lot of the inital setup as I have already created the site
application configurations we will be using. 

## Getting Started

‼️ If you have followed the steps in our [Using PyCharm Community Edition](./docs/README.md) guide, you can skip this 
section. ‼️

Assuming you have by now used git to check out a local copy of this repository 
and used the python environment manager of your choice (we use 
[Anaconda](https://www.anaconda.com/products/individual)) to create a new
environment for this project, you are now ready to install the required libraries to
run this project. The simplest is to install with:

```shell
pip install -r requirements.txt
```

You can have a look at [requirements.txt](./requirements.txt) to see what
this file contains. This is 
[a list of libraries](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format), 
most notably the Django
distribution itself, that we need for this test project. If, as we develop
the site, we need more libraries, we can update the requirements.txt 
and re-run the above command to download the extra libraries. 

## Creating the database and a superuser

Once you have installed the libraries, you can create a new database file 
(the default development configuration uses [SQLite](https://www.sqlite.org/)
which is a file-based relational database system that can run straight from your
hard-disk without requiring additional processes). Django supports 
[many different databases](https://docs.djangoproject.com/en/3.1/ref/databases/)
and allows you to write code without worrying about what database system sits underneath. 

The database is used to store system information, such as which users are allowed to 
log in, their permissions etc. and you can add your own data objects 
([Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)) that
can store custom data. 

Django also remembers changes you make to your models, and allows you to 
easily upgrade (or [migrate](https://docs.djangoproject.com/en/3.1/topics/migrations/))
your database from one version to the next. 

Since we have never run django at all, we need to run the first set of migrations
to make sure our database exists, and with the models we need for 
running the server.

```shell
python manage.py migrate
```

This will have created everything you need to run the server. You should see a file called `db.sqlite3` in the
project directory. This file holds all the information in the database. 

## Running the server

This is the exciting step when we can actually launch the web server itself. Again, we use the manage command
to tell the server to start up:

```shell
python manage.py runserver
```

This should print out a little bit of information, such as

```text
> python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 25, 2021 - 07:16:46
Django version 3.1.7, using settings 'website.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you see that message, then everything has gone well, and you can visit your site on the URL shown.

Just a few notes about URLs, the generic format is: `<protocol>://<host>:<port>/<path><querystring>` - there are a few
other bits as well, but we can ignore those for now. We're used to URLs such as https://www.k-si.com/ and breaking this down
we see that the protocol is `https` - this is the secure, encrypted version of `http`, but both http and https offers
the same functionality. 

Next we see that the host is `www.k-si.com` - this hostname is actually registered with 
something called [DNS (Domain Name System)](https://en.wikipedia.org/wiki/Domain_Name_System) and the computer
can look up that text value to get the network address (IP Address) of the server. In the case of `www.k-si.com` we can
[look this up](https://mxtoolbox.com/SuperTool.aspx?action=a%3awww.k-si.com&run=toolpage) and see that the 
IP Address is (at the time I wrote this) 52.218.20.194. The computer can then connect to that address to download
the webpage. 

In our example URL, the port is missing. That's because, by default, http pages are hosted on port 80 and https on 
port 443. You may wonder [what a port is](http://www.steves-internet-guide.com/tcpip-ports-sockets/)? It is part of how 
computer networks communicate, and just like the IP address 
identifies the computer, the port identifies the application on that computer. A computer can run multiple applications
but can only host one application per port. 

The bits are the path and querystring. Paths are used to point at specific content (or "pages") on the server. Any path 
that ends with a / is often referred to as an "index page", and in the example above, where the entire path is just "/"
that is often referred to as the server "root". 

So, to get back to the actual URL to our server, we can now see that it refers to the root index page of a server
at 127.0.0.1 running on port 8000. 127.0.0.1 is a special IP address, and always refers to the current computer. It
is often also referred to as "localhost" or simply "home", leading to 
[jokes like this](https://9gag.com/gag/a2ZEXEE). 

Have you tried opening it yet? 

## Views and dispatching

Now that we have hopefully managed to connect to the server, it's worth talking about what actually happened. Using the
URL, our browser figured out which host and port to connect to, and then using the 
[http protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) (this is 
the [Tim Berners-Lee](https://www.w3.org/People/Berners-Lee/) bit) it requested the content at the root index.

The first bit Django does (it probably isn't the first - but it's the first bit we need to worry about) is to figure out
what content to serve for the requested path. This information is held in a file called 
[urls.py](./skillsfinder/urls.py) and in the basic form looks as simple as:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

This piece of code creates a list of `urlpatterns` that the server uses to translate (or 
[dispatch](https://docs.djangoproject.com/en/3.1/topics/http/urls/)) the requested URL 
to a piece of code called the [View](https://docs.djangoproject.com/en/3.1/topics/http/views/) in Django. 

You need to understand a bit of python to see what's going on there. We start by importing the file `views` from
the current directory indicated by a simple `.`. In [this file](./skillsfinder/views.py) we find that there is a 
function called `index` and this is declared in the pattern as `path('', views.index)`: for the empty path `''`, direct
to the function `index` within the file `views`. We additionaly give it the name 'index' (`name='index'`), but this
optional, but may become useful later. 

Ok, what about the index function, what does that do? 

```python
def index(request):
    context = {
        'site_name': 'Skillsfinder',
    }
    return render(request, 'skillsfinder/index.html', context)
```

It does two basic things:

1. Creates a Python dictionary object called `context` that maps the key 'site_name' to the value 'Skillsfinder'
2. It then returns a handy [Django shortcut function](https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/) 
   called render that takes the incoming request object, the name of 
   a template and the dictionary we just created. This is all Django requires to then display the page. 
   
So the final piece of the magic here is the actual template. This holds the HTML and logic needed to display the page.
The template is [skillsfinder/index.html](./skillsfinder/templates/skillsfinder/index.html)
and can be found within the `templates` folder in our 'skillsfinder' app.

This is a very basic page that holds the [HTML](https://www.w3schools.com/html/) of the page that we display. The 
interesting thing here, which we will use later, is the placeholder tags `{{ site_name }}` - when Django finds these
it goes to the `context` we passed to the render function and looks up the value of 'site_name' there - and in this
case replacing the value with 'Skillsfinder' as provided in views.py.

Feel free to edit any of these files and then reload the page and see what happens.

## Admin pages

Before we start properly, there is one more key part of Django that is also important to be aware. Django
ships with an awesome admin framework that can automatically create forms to interact with the database and
settings. This can be used to create, read, update and delete 
([CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)) records in the database, such as users and any
custom models we create.

To access the admin screens though, you need be logged in to the site as an admin user. So far we only have a blank
database, so we have no way of logging in. This is where the 
[django management command](https://docs.djangoproject.com/en/3.1/ref/django-admin/), manage.py, comes in very handy.

Stop the server if it still running by pressing CTRL-C in the terminal, and then run the following command:

```shell
python manage.py createsuperuser
```

This will ask you for a username and password, and update the database with these details so that you can log in. 

Once that has completed, you can launch the server again with `python manage.py runserver` and open the site
URL. Add `/admin/` to the path (e.g. http://127.0.0.1:8000/admin) and hit return, you should now be asked to log in. 
Enter the username and password you set earlier (or go through the createsuperuser steps again if you've 
forgotten) and then you should see the admin pages.

Have a play with this - you can see how you can do all the CRUD operations (if you delete the superuser, just create
another one) on Groups and Users. We will later use the same functionality on our own models.

You are now ready to move on to [creating your first model](./docs/creating-your-first-model/README.md).
