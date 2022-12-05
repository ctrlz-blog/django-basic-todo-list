# django-todo
A simple to-do list app built with Django.

## Tutorials

- [Project Introduction](https://ctrlzblog.com/tutorial-create-a-to-do-list-app/)
- [How to install Django](https://ctrlzblog.com/to-do-list-part-1-installing-django/)
- [How to create tasks in the database](https://ctrlzblog.com/to-do-list-part-2-apps-models/)
- [Add fake entries to your todo list](https://ctrlzblog.com/how-to-generate-fake-data-for-your-django-project-with-faker/)
- [How to add URLs, Views & Templates](https://ctrlzblog.com/to-do-list-part-3-urls-views-templates/)
- [How to add a form](https://ctrlzblog.com/to-do-list-part-4-adding-a-form/)
- [Add CSS to templates](https://ctrlzblog.com/to-do-list-part-5-improve-the-ui/)
- [CRUD: updating objects](https://ctrlzblog.com/to-do-list-part-6-edit-objects/)
- [CRUD: deleting objects](https://ctrlzblog.com/to-do-list-part-7-deleting-tasks/)
- [Filtering lists](https://ctrlzblog.com/to-do-list-part-8-filtering-tasks/)


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
