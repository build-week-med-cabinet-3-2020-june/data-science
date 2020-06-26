## Data Science

# Installation 

    git clone https://github.com/build-week-med-cabinet-3-2020-june/data-science.git
    cd data-science

Setup

    pipenv install

## Usage 

### On Windows:

    export FLASK_APP=web_app # one-time thing, to set the env var
    flask run
    
Export doesn't work, use set instead.
Open in a debug mode and set:
    FLASK_ENV=development
    FLASK_APP=med_app
    flask run 

### Migrate the Database

Windows users can omit the "FLASK_APP=web_app" part...
    FLASK_APP=med_app flask db init #> generates app/migrations dir

run both when changing the schema:
    FLASK_APP=med_app flask db migrate #> creates the db (with "alembic_version" table)
    FLASK_APP=med_app flask db upgrade #> creates the specified 

    pip3 install config

### Heroku
#### Create a database and upload to Heroku  

    pip install heroku 

1. Heroku login
2. Clone the repository

    heroku git:clone -a med-cab-api

Deploy your changes with:

    git add .
    git commit -am "Creating an API"
    git push heroku master

Run Bash

    FLASK_APP=med_app flask db init 
    FLASK_APP=med_app flask db migrate
    FLASK_APP=med_app flask db upgrade

Run:

    data_pipeline.py #file to insert data 



# Flask API project

This project shows one of the possible ways to implement RESTful API server.

There are implemented two models: User and Todo, one user has many todos.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.
4. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── README.md
├── app.py
├── endpoints
│   ├── __init__.py
│   ├── todos
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── resource.py
│   └── users
│       ├── __init__.py
│       ├── model.py
│       └── resource.py
├── manage.py
├── requirements.txt
└── settings.py
```

* endpoints - holds all endpoints.
* app.py - flask application initialization.
* settings.py - all global app settings.
* manage.py - script for managing application (migrations, server execution, etc.)

## Running 

1. Clone repository.
2. pip install requirements.txt
3. Run following commands:
    1. python manage.py db init
    2. python manage.py db migrate
    3. python manage.py db upgrade
4. Start server by running python manage.py runserver

## Usage
### Users endpoint
POST http://127.0.0.1:5000/api/users

REQUEST
```json
{
	"name": "John John"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "John John",
    "todos": []
}
```
PUT http://127.0.0.1:5000/api/users/1

REQUEST
```json
{
	"name": "Smith Smith"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "Smith Smith",
    "todos": []
}
```
DELETE http://127.0.0.1:5000/api/users/1

RESPONSE
```json
{
    "id": 3,
    "name": "Tom Tom",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users

RESPONSE
```json
{
    "count": 2,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        },
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users/2
```json
{
    "id": 2,
    "name": "Smith Smith",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users?name=John John
```json
{
    "count": 1,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users?limit=1&offset=1
```json
{
    "count": 1,
    "users": [
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```

Todo endpoint is similar to Users endpoint.
