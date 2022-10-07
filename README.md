# django-todo
A simple to-do list app built with Django and htmx

### How to use this repository

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
