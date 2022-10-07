# **Django Migrations**

Install a virtual environment for the project
```
# install python module venv at directory venv
python -m venv venv
```

Activate venv

```
. venv/scripts/activate
```

Install the requirements
```
pip install -r requirements.txt
```

Install a package and then add it to requirements.txt
```
pip install django && pip freeze > requirements.txt
```

Run server from within ./MigrationHell
```
python manage.py runserver
```