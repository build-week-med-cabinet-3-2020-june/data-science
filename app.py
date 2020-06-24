import spacy
import spacy.cli
spacy.cli.download("en_core_web_lg")
import en_core_web_lg
from joblib import load
from flask import Flask, request, send_from_directory, jsonify

nlp = en_core_web_lg.load()
rfc_lg = load("rfc_lg.joblib")

def get_word_vectors(docs):
    return [nlp(doc).vector for doc in docs]

def cann_pred(user_input):
    request = [f'{user_input}']
    custom = get_word_vectors(request)
    output = rfc_lg.predict(custom)[0]
    # output2 = rfc_lg_strains.predict(custom)[0] # [Stretch goal - 2nd model]
    if output == 'hybrid':
        prob = rfc_lg.predict_proba(custom)[0][0]
    elif output == 'indica':
        prob = rfc_lg.predict_proba(custom)[0][1]
    else:
        prob = rfc_lg.predict_proba(custom)[0][2]
    return(f"We're {prob*100:.0f}% confident you should try the {output} strain!")
    # This is a stretch goal
    # return(f"We're {prob*100:.0f}% confident you should try the {output} strain and {output2} fits your criteria the most!")

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("", "index.html")

@app.route("/predictions", methods=["POST"])
def predictions():

    if request.form:
        input = request.form["effects"]
    else:
        input = request.json["effects"]
    custom = get_word_vectors(input)
    output = rfc_lg.predict(custom)[0]

    if output == 'hybrid':
        prob = rfc_lg.predict_proba(custom)[0][0]
    elif output == 'indica':
        prob = rfc_lg.predict_proba(custom)[0][1]
    else:
        prob = rfc_lg.predict_proba(custom)[0][2]

    return jsonify({"strain": output, "proba": prob})



if __name__ == "__main__":
    app.run()
