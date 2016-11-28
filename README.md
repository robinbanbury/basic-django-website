# basic-django-website

A list of things to do to get your website working on [PythonAnywhere.com](http://pythonanywhere.com):

* Clone the repo: `git clone https://github.com/robincsmith/basic-django-website.git`
* Replace the contents of `/var/www/<something>_com_wsgi.py` with the following:
```
import os
import sys

 project_home = u'/home/<user>/<project_root>'
 if project_home not in sys.path:
     sys.path.append(project_home)

 os.environ['DJANGO_SETTINGS_MODULE'] = '<settings_folder>.settings'

 from django.core.wsgi import get_wsgi_application
 application = get_wsgi_application()
```
Where `<user>` is your username, `<project_root>` is the ROOT of the entire project and `<settings_folder>` is the folder that contains your `settings.py`
* In the folder with your `settings.py`, open `sk.py` and provide your `SECRET_KEY`
* This project **doesn't** contain any database content, so some setup work is needed:
    * Migrate your databases (the models already exist): `python manage.py migrate`
    * Create an admin user: `python manage.py createsuperuser`
* If you **are** importing database content (e.g an SQLite database named `db.sqlite3`), make sure the database file is in your settings.py folder
    * Ensure the following is in your `settings.py`, then run `python manage.py syncdb` (not tested):
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
* Reload your app in the PythonAnywhere UI, under the 'Web' tab.

This has been adapted from PythonAnywhere's tutorial, available [here](https://help.pythonanywhere.com/pages/DjangoTutorial/)
