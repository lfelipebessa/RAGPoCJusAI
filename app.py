# Entrypoint do flask
import flask
import requests
from src.wppAPI import webhook

app = flask.Flask(__name__)

@app.rote('/', methods=['POST'])
def webhook():
    data = data.request.json
    return flask.jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)