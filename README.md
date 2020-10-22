# django_CRUD_api
A Django api that allow to make simple CRUD operations


# info
This project was created using django webframe work

It is an API that handles CRUD apis

This project uses MySql as its main database

# Necessary Package:

- django

- mysqlclinet

- djangorestframework


# Befor cloning running the app make sure to:

1- have all the necessary packages installed

2- Create a database in the mySql command line (CREATE DATABASE dbName) but be sure to add the name to the DATABASE Configration in the settings file (if changed (I already put it to "django_api"))

3- change the database configration to your personal configs ( django_api => settings.py => DATABASE => change 'USER', 'PASSWORD')


# After cloning, all you need to do is to go to the terminal in the project's root and type: python manage.py runserver  (now you have a running server)

Methods	Urls	Actions

GET   ||	api/posts	        ||    get all posts

GET	 ||   api/posts/:id	    ||    get posts by id

POST ||   api/posts	        ||    add new posts

PUT	 ||   api/posts/:id	    ||    update posts by id ( add {"published": true} or {"likes": 20} to the request parameters)

DELETE ||	api/posts/:id	    ||    remove posts by id

DELETE ||	api/posts	        ||    remove all posts

GET	  ||  api/posts/published	||  find all published posts

GET	  ||  api/posts?title=Hello ||	find all posts which title 'Hello'
