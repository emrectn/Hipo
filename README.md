# The Ultimate Flicker Client

In this website, users will search photos by tags. The website will use the Flickr API and fetch the photos that contain the keyword that the user entered using Django.

Visit the link to test. Project deploy on Pythonanywhere.com
**https://emrec.pythonanywhere.com/**


# Installation

Assuming you've got Python3.6 installed, you'll need Django 2.0 or higher. Django is a Python framework that create web application.

Project is already on GitHub, you can just clone it from a **Bash Console**:

	git clone https://github.com/emrectn/Hipo.git

In your Bash console, create a virtualenv, naming it after your project, and choosing the version of Python you want to use (**recommended python3.6**):  

	mkvirtualenv --python=/usr/bin/python3.6 my-venv
	(my-venv)$ pip install -r requirements.txt

This project uses a database, you'll need to set that up.
Go to the Consoles tab, start a bash console, use cd to navigate to the directory where your Django project's manage.py lives, then run

	(my-venv)$ python manage.py migrate
	(my-venv)$ python manage.py makemigrations
	(my-venv)$ python manage.py runserver

Go visit http://127.0.0.1:8000/, it should be live! 

And go visit http://127.0.0.1:8000/admin to accesing admin page .  To log on to the Admin page, you must first create the superuser.

	(my-venv)$ python manage.py createsuperuser
		


