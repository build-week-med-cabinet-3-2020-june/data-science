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
