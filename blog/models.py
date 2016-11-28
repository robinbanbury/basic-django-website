from django.db import models

# models.py is like your entire DATABASE
# In models.py we have classes - these are your database TABLES
# In a class, the variables are your table COLUMNS

# The underlying databases are in sqlite3 by default - yay!
# By using models, we are abstracted from writing database code.

class Post(models.Model):
    # These are the fundamental aspects of a blog post
    title = models.CharField(max_length=140)    # short text
    body = models.TextField()                   # longer text
    date = models.DateTimeField()               # datetime

    # This means you can print the 'Post' object itself - handy.
    def __str__(self):
        return self.title



#    class Person(models.Model):
#        first_name = models.CharField(max_length=30)
#        last_name = models.CharField(max_length=30)

# first_name and last_name are fields of the model.
# Each field is specified as a class attribute.
# Each attribute maps to a database column.

# The SQLite code generated is:
# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name"  varchar(30) NOT NULL
# );