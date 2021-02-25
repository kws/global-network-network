# Displaying your data

So far you should have installed everything you need to work, created a database, and added a model and some data. 

Having got this far, it all seems a bit pointless if you can't do anything more useful with 
that information. At a bare minimum you need to be able to display the information before
your site does much good. 

Remember we already discussed the [view and template](../../README.md#views-and-dispatching) and how we could add 
context variables to that? We can do the same with our models.

Django models support a powerful [query framework](https://docs.djangoproject.com/en/3.1/topics/db/queries/) that 
allows us to filter and update data in the models. The amazing django management command has a tool to help us with 
this as well. Let's launch the interactive Django shell:

```shell
python manage.py shell
```

This will open a strange input prompt that allows us to interact with the django environment directly. First of all
let's see if we can use our Person model. The first thing we have to do is to import it. 

```
>>> from skillsfinder.models import Person
```
That will have loaded the Person object into the shell, and we can now start using it. 

```
>>> Person.objects.all()
<QuerySet [<Person: Me>]>
```
(In these examples, you only need to type what comes after >>> - in the rest of the block I'll include some sample 
output if applicable)

Here we have asked django to give us all Person objects in the database. I only had one, but you may have already
created more through admin. But we don't need ot use admin to create instances, we can also do it in code:

```
>>> Person.objects.create(name="Kaj", bio="")
<Person: Kaj>
```
In this case it didn't return a queryset, but just a single Person instance. Why don't you try creating a few more
people with different attributes. Let's see what happens if we list them now:

```
>>> Person.objects.all()
<QuerySet [<Person: Me>, <Person: Kaj>, <Person: Kaj2>, <Person: Kaj3>, <Person: No more Kajs please!>]>
```

We can also filter the objects. How about if we just want to see the Kajs? 

```
>>> Person.objects.filter(name="Kaj")
<QuerySet [<Person: Kaj>]>
>>> 
```
That has given us one Kaj, because the default option is an exact match. However, we can also do other searches such as 
["contains", "greater than", "less than" etc.](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups) 
Let's try 'icontains' which does a case-insensitive contains:

```
>>> Person.objects.filter(name__icontains="kaj")
<QuerySet [<Person: Kaj>, <Person: Kaj2>, <Person: Kaj3>, <Person: No more Kajs please!>]>
```

Ok, now that we have figure out how to query the data, let's put it to some use on our website. 
First of all, you can quit the django shell by typing `exit()`. Then, let's go and edit our 
[view](../../skillsfinder/views.py) so that it returns the Person instances:

```python
from django.shortcuts import render
from skillsfinder.models import Person


def index(request):
    context = {
        'site_name': 'Skillsfinder',
        'people': Person.objects.all(),
    }
    return render(request, 'skillsfinder/index.html', context)
```

If you compare with our previous version, so you will see there are two changes:

1. We import the Person model, and
2. We add a new context mapping from the key 'people' to the Person instances.

We can now pick this up in our [template](../../skillsfinder/templates/skillsfinder/index.html):
just below the `<p> ... </p>` section. 
```html
<ul>
    {% for person in people %}
    <li>{{ person.name }}</li>
    {% endfor %}
</ul>
```

Using the [Django Template Language](https://docs.djangoproject.com/en/3.1/topics/templates/) this means add
a [&lt;ul>](https://www.w3schools.com/tags/tag_ul.asp) tag then loop over each item in the context object called people
(that we have just added to our view), call each item "person" and then add the "name" attribute of person
surrounded by the [&lt;li>](https://www.w3schools.com/tags/tag_li.asp) tag.

Check out the front page of your site and see if anything has changed. 
