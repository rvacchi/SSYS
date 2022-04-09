from flask import Flask,json
import os
import datetime as dt

app = Flask(__name__)

@app.route("/")
def hello_world():
    return json.dumps( { 
        "objetivo": "Desafio Tecnico da SSYS",
        "feito por": "Rodolfo Soares",
        "data": dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')               
    },  indent=4, sort_keys=False)

if __name__ == '__main__': 
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port)
    
#pull request 1
