# Creating your first Model

This is a very simple example to help us design the data model for the skills site. For a much more detailed 
walkthrough of how to create a Django project from scratch, follow the excellent [Django 
Tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/).

## What is a Model?

The [Django documentation](https://docs.djangoproject.com/en/3.1/topics/db/models/) defines a model as: single, 
definitive source of information about your data. It contains the essential fields and behaviors of the data you’re 
storing.

In [relational database](https://en.wikipedia.org/wiki/Relational_model) terminology, this is mostly the same as a 
table, and in Excel we would probably refer to this as a table or worksheet. 

Each model models a concept in our application. We have already seen how Django ships with models for User and Group. 
Note the user of singular, the model instance is a single record, but the database table holds a set of instances.

But enough theory, let's create our first model!

## Define a model

In Django, models are defined as snippets of Python code. These typically are stored in the file called `models.py`, 
so [open this file](../../skillsfinder/models.py) and let's add a first model definition:

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
```

We are building a people directory, so we want to be able to model a person within that directory. The first thing
we do is to name our model, and we have called it a Person. On the following lines we define the attributes of that
person. These will become the fields of our model, and columns in the database. 

Database columns can have different types, and in this case we have used two different fields that can hold text. Django
supports many [different field types](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types), and in this
case the CharField is usually used for smaller text values of a limited size, and TextFields for longer, multi-line
fields. 

In addition to the fields we see here, all Django models have one additional field that is automatically declared for 
you. This is the [Primary Key](https://en.wikipedia.org/wiki/Primary_key) and is a unique identifier for your model 
instance. By default the primary key is named 'id' and is an auto-incrementing integer, i.e. it starts at 1 and 
for every new model instance you create it will get the next biggest integer.

## Creating the 'migration'

Before we can use our model though, we need to translate the python definition into "database speak". Django does all 
hard work for us here. It tracks changes to your models through a series of "migrations", just like when we created 
our initial database. So the first thing we have to do is make django aware of our changes.

We use the management tool to scan our code and make the migration scripts for us:

```python
python manage.py makemigrations    
```

You should see some output indicating that Django has found your changes and created the 
migration:

```
> python manage.py makemigrations

Migrations for 'skillsfinder':
  skillsfinder/migrations/0001_initial.py
    - Create model Person

```
If you are interested, this command has created an automatically generated python file, 
as indicated in the output above. This file can be used to actually make the changes
to the database, in this case create the person table.

The management command can also be used to show the actual commands that will be sent to
the database:

```
> python manage.py sqlmigrate skillsfinder 0001

BEGIN;
--
-- Create model Person
--
CREATE TABLE "skillsfinder_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "bio" text NOT NULL);
COMMIT;
```

This shows how Django has translated the python migration into [SQL](https://www.w3schools.com/sql/) which is the 
language the database understands. This command is just for information, and you don't need to ask for this normally. 

We do however, need to ask Django to make the changes. This is again just as easy as when we first created the
database: 

```python
python manage.py migrate 
```

If you don't see any errors. Then you can assume this has worked. 

## Registering your model with Django Admin
Great! Now there is only one final step we need before we can start populating our model table. We need to let the 
Django admin tool know about our model.

In the file [admin.py](../../skillsfinder/admin.py) add the following lines:

```python
from skillsfinder.models import Person

admin.site.register(Person)
```
Start your server and head to the admin screens. Can you see your model? 

If you add a person, it should appear in the list of persons. However, it isn't very
easy to tell people apart. That's because we haven't given Django any information about how to
describe people. 

A very simple fix is to head back into our [models.py](../../skillsfinder/models.py) and change
the Person so it looks like this:

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
```

The bit we have added at the end, is a standard Python way of describing how to convert any Python class (an object or 
a thing) into text. In this case, we simply say that when trying to turn a Person into a string, 
simply use that persons 'name' attribute. 

You don't even need to restart the server, if you just refresh the person list and you should see the names appearing.

Now, remember every time you add or edit a model's definition, you will need to create a new  migration with 
`makemigrations` and then apply them to the database with `migrate`. 