## Data Science

# Installation 

![alt text](https://www.google.com/imgres?imgurl=https%3A%2F%2Fdynaimage.cdn.cnn.com%2Fcnn%2Fc_fill%2Cg_auto%2Cw_1200%2Ch_675%2Car_16%3A9%2Fhttps%253A%252F%252Fcdn.cnn.com%252Fcnnnext%252Fdam%252Fassets%252F191031084204-marijuana-flower-stock.jpg&imgrefurl=https%3A%2F%2Fwww.cnn.com%2F2020%2F01%2F14%2Fhealth%2Fweed-impact-driving-wellness%2Findex.html&tbnid=8RTmXeqTOwnH0M&vet=12ahUKEwjIzfiWmJ7qAhUbUM0KHeGzCIQQMygXegUIARC-AQ..i&docid=oTigYOrkHnj0xM&w=1200&h=675&q=marijuana&ved=2ahUKEwjIzfiWmJ7qAhUbUM0KHeGzCIQQMygXegUIARC-AQ)
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
