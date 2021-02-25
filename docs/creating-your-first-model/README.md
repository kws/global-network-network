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

But before we can

```python
python manage.py makemigrations    
```

```python
python manage.py sqlmigrate skillsfinder 0001   
```

```python
python manage.py migrate 
```
