# A Web Store using Django & Bootstrap


+ 1_ first create virtual environment : `python -m venv .venv` and activate it with `./.venv/Scripts/activate`.
+ 2_ install django 
+ 3_ create a project : django-admin startproject mysite <folder_name = website_name> :
-  4_ ..cd
-  5_ django-admin startproject mysite .
it will create a `mysite` folder.
+ 6_ cd Django_webstore
+ 7_ create an app : `python manage.py startapp store`
+ 8_ create a blog : `python manage.py startapp blog`
+ 9_ `python manage.py runserver`

+ 10_ create pages of the site in `views.py`.
+ 11_ create a folder in in store folder, named `templates` and put html files in that. and put html files in it.

+ At the end we have to add our app into `INSTALLED_APPS` list in setting.py.


## How to use static files using (Django + Bootstrap) :
+ Using static files : https://docs.djangoproject.com/en/5.1/howto/static-files/ 
```
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "store/static")] 
```
and use `{% load static %}` in html files like this :
```
{% load static %}

.
.
<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
.
.
<script src="{% static 'js/main.js' %}"></script>
. 
```


# How to apply migrations :
```
python manage.py makemigrations store
```
then
```
python manage.py migrate
```
now you can run :
```
python manage.py runserver
```