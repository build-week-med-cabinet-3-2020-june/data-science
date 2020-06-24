# med_app.py
# set FLASK_ENV=development
# set FLASK_APP=med_app
# flask run 

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config 
import json
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import os, sys
import numpy as np
import pandas as pd
# import spacy, re
# import spacy.cli
# spacy.cli.download("en_core_web_lg")
# import en_core_web_lg
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix
# # from wtforms import StringField, PasswordField, SubmitField, BooleanField
# # from wtforms.validators import DataRequired, Length, Email, EqualTo
# from joblib import load
import pandas as pd
import os
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv

load_dotenv()


# import spacy
# import spacy.cli
# spacy.cli.download("en_core_web_lg")
# import en_core_web_lg
# from joblib import load

db = SQLAlchemy()
migrate = Migrate()

MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "rfc_lg.joblib")
nlp = en_core_web_lg.load()


class Medcab(db.Model):
    id = db.Column(db.Integer, primary_key = True) # pylint: disable=maybe-no-member
    Effects = db.Column(db.String(200), unique=True) # pylint: disable=maybe-no-member
    Type = db.Column(db.String(200), unique = True) # pylint: disable=maybe-no-member

    def __repr__(self):
        return f'<Medcab {self.effects} {self.type_str}'


def parse_records(database_records):
    parsed_records = []
    for record in database_records:
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records        

#Init app

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)

    ENV = 'dev'
        
    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///med_cab.db"
    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = ''

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    engine = create_engine('sqlite:///med_cab.db')
    Medcab.metadata.create_all(engine)
    # file_name = 'https://raw.githubusercontent.com/kellischeuble/strain_recommender/master/data/merged.csv'
    df = pd.read_csv('merged.csv')

    # def get_word_vectors(docs):
    #     return [nlp(doc).vector for doc in docs]
    # def cann_pred(user_input):
    #     request = [f'{user_input}']
    #     custom = get_word_vectors(request)
    #     output = rfc_lg.predict(custom)[0]

    #     if output == 'hybrid':
    #         prob = rfc_lg.predict_proba(custom)[0][0]
    #     elif output == 'indica':
    #         prob = rfc_lg.predict_proba(custom)[0][1]
    #     else:
    #         prob = rfc_lg.predict_proba(custom)[0][2]
    #     return(f"We're {prob*100:.0f}% confident you should try the {output} strain!")

    # def load_model():
    #     with open(MODEL_FILEPATH, "rb") as model_file: # r - read the file, rb - read the binary file
    #         saved_model = joblib.load(model_file)
    #     return saved_model

    @app.route('/')
    @app.route('/home')
    def index():
        return f'Hello World!'

    @app.route('/effects/<effect>', methods=['GET']) 
    def eff(effect):
        # FETCHING FROM THE DATATBASE
        effects = Medcab.query.filter_by(effect=effect)
        parsed = parse_records(effects.all())
        input_user = get_word_vectors(parsed)
        input_user1 = cann_pred(input_user)
        return jsonify(input_user1)

    @app.route('/results')
    def results():
        return f"Hello"

    return app

    # Run Server
    if __name__ == "__main__":
        app.run(debug=True)
