# django-todo
A simple to-do list app built with Django.

## Tutorials

#### Project Intro
https://ctrlzblog.com/tutorial-create-a-to-do-list-app/

#### Part 1: Install Django
https://ctrlzblog.com/to-do-list-part-1-installing-django/

#### Part 2: Apps & Models
https://ctrlzblog.com/to-do-list-part-2-apps-models/

#### Part 3: URLs, Views & Templates
https://ctrlzblog.com/to-do-list-part-3-urls-views-templates/

#### Part 4: Forms
https://ctrlzblog.com/to-do-list-part-4-adding-a-form/

#### Part 5: Templates
https://ctrlzblog.com/to-do-list-part-5-improve-the-ui/

#### Part 6: Updating objects
https://ctrlzblog.com/to-do-list-part-6-edit-objects/

#### Part 7: Deleting objects
https://ctrlzblog.com/to-do-list-part-7-deleting-tasks/

#### Part 8: Filtering objects
https://ctrlzblog.com/to-do-list-part-8-filtering-tasks/


## How to use this repository

1. **Create a virtual environment**

```
python3 -m venv venv
```

Activate environment
```
source venv/bin/activate
```

2. **Install requirements**
```
pip install -r requirements.txt
```

3. **Create a .env file in mysite directory**

Add the following code:
```
SECRET_KEY=yoursecretkeywhichwillbemoresecurethanthisone
```

4. **Test the server runs**
```
python manage.py runserver
```

5. **Migrate**
```
python manage.py migrate
```

6. **Create a superuser**
```
python manage.py createsuperuser
```
