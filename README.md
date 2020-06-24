# data-science

# Installation 


'''sh 
git clone https://github.com/build-week-med-cabinet-3-2020-june/data-science.git
cd data-science

#Setup

'''sh
pipenv install
''''

#Usage 

'''sh

# Windows:
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
# export doesn't work use set instead
set FLASK_ENV=development
set FLASK_APP=med_app
flask run 


## Migrate the DATABASE 

# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified 

pip3 install config