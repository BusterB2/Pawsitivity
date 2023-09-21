Create Github repo
Clone it locally using Github Desktop
Create a VSCode workspace
.gitignore -> https://www.toptal.com/developers/gitignore
Add workspace file to .gitignore

Create a steps.txt file
py -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject pawsitivity .
pip install psycopg2
Create DB_name in pgAdmin or psql

DB Config in settings.py DATABASES variable
pip install python-dotenv
.env file creation
adding venv, .env file to
import os
from dotenv import load_dotenv
load_dotenv()
os.getenv('VAR_NAME')

Create blogs app
Add to INSTALLED_APPS in settings.py
Create models
Register the models in admin.py
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
Login to admin and view the models

py manage.py collectstatic
Add static/ to .gitignore
