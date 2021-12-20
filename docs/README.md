# Documentation

Here documentation for development. please add document section if needed.

## preparing
preparing this software at least you need, `pip`, `python>=3.5` `django>=3.0`

### Virtual Environment
this optional, but very recommended. you can use favorite 
virtual environment. here we use virtualenv.

```bash
virtualenv .venv
```
install `pipenv` used to manage depedency in this project

```bash
pip install pipenv
```

### Install Depedency
depedency for this project,
- Django 3.2.2
- django-simple-bulma 2.2.0
- python 3.8

for simple step you can type this command to install 
all depedency.
```bash
pipenv install 
```

## testing
for run this django project you should run following step.
```bash
python manage.py migrate
```
you can also create superuser to manage panel admin
```bash
python manage.py createsuperuser admin
```
and now running django server to see the result.
```bash
python manage.py runserver
```