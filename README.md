# django-blog

The Polling App
Our Django blog site will have two separate functions: blogging and polling. Whereas the `mysite` project directory governs the entire site, the specific blogging and polling features will each be contained in their own separate app.

For demonstration purposes, I'm going to quickly create the polling app. We'll go through all of these same steps much more slowly when we create the blogging app. Oh, and in the video I log into the Django admin with the username "jaschilz". You'll log into your Django admin using whatever username and password you created for your superuser with the `python manage.py createsuperuser` command.

The Blog Post Model
Within an app, Django divides up functionality by module or file. You’ll create ORM model classes in the models.py file, view code in the views.py file, and so on. We’ll start by defining the main Python class for our blog system, a Post.

Any Python class in Django that is meant to be persisted must inherit from the Django Model class. This base class hooks in to the ORM functionality converting Python code to SQL. You can override methods from the base Model class to alter how this works or write new methods to add functionality.

The Django Query API
The manager on each model class supports a full-featured query API. API methods take keyword arguments, where the keywords are special constructions combining field names with field lookups. The double-underscore character separates the name of a field from the lookup value.

title__exact=”The exact title”
text__contains=”decoration”
id__in=range(1,4)
published_date__lte=datetime.datetime.now()
Each keyword argument adds to the query that will be used to find matching objects.

QuerySets
A QuerySet is a special type of object that maintains a relationship to the database. Query API methods can be divided into two basic groups: methods that return QuerySets and those that do not.
