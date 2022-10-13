# **Django Migrations**

Optional: install sqlite3 command-line shell: https://www.sqlite.org/download.html

## **SQLite Commands**

```
.mode column # sets the output to be structured columns
.headers on # sets headers on the output
SELECT * FROM farming_farm;
SELECT * FROM farming_farmer;
SELECT * FROM django_migrations;
DELETE FROM django_migrations WHERE name='0003_data_migrations';
```

<hr/>

## **Python Setup**

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

<hr/>

## **Migration Commands**

Make migrations from ./MigrationHell
```
python manage.py makemigrations
```

Apply migrations from ./MigrationHell
```
python manage.py migrate
```

Run server from within ./MigrationHell
```
python manage.py runserver
```

Load fixtures from within ./MigrationHell
```
python manage.py loaddata farmers
python manage.py loaddata farms
```

Create an empty migration from ./MigrationHell
```
python manage.py makemigrations {app_name} --name {name-without-numbers} --empty
```

