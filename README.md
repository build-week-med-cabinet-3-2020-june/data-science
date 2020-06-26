## Data Science

# Installation 

![alt text](https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.squarespace-cdn.com%2Fcontent%2Fv1%2F57ed9f4cbe65948d363da3f8%2F1551592356804-JOIZY1YXIPVN9V6QH08D%2Fke17ZwdGBToddI8pDm48kPnsf5mMwK3KDy1tisBlUmRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpyS4d2ygLGTER2Ftu3sSYRLmU3LUrpV3s4CHzcPlb2Kt5_AyYgzyUvA4JRlWfdald8%2FMarijuana.png)

''' 

git clone https://github.com/build-week-med-cabinet-3-2020-june/data-science.git
cd data-science

'''

Setup

'''

pipenv install

''''

## Usage 

# On Windows:

'''
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
export doesn't work use set instead
Open in a debug mode
set FLASK_ENV=development
set FLASK_APP=med_app
flask run 

'''

## Migrate the DATABASE 

Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=med_app flask db init #> generates app/migrations dir

run both when changing the schema:
FLASK_APP=med_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=med_app flask db upgrade #> creates the specified 

pip3 install config

Heroku - create a database and upload to heroku  
pip install heroku 

heroku login
Clone the repository

heroku git:clone -a med-cab-api

Deploy your changes

'''
git add .
git commit -am "Creating an API"
git push heroku master

heroku run bash ==> 
FLASK_APP=med_app flask db init 
FLASK_APP=med_app flask db migrate
FLASK_APP=med_app flask db upgrade
'''
run data_pipeline.py file to insert data 
