import flask
import requests
from raven.contrib.flask import Sentry
sentry = Sentry(app, dsn='https://ac2b341ce6744566b291474271ee0b83:dfdc9efac37c4eaea54455bd8c9d40d0@sentry.io/236271')
app = flask.Flask(__name__)

dad_headers = {
    'Accept': 'text/plain',
    'User-Agent': 'flsk (Flask API) - https://github.com/tilda/flsk'
}

uagent = {
    'User-Agent': 'flsk (Flask API) - https://github.com/tilda/flsk'
}

@app.route("/api/joke")
def joke():
    jok = requests.get('https://icanhazdadjoke.com', headers=dad_headers)
    return jok.text

@app.route("/api/neko")
def neko():
    n = requests.get('https://nekos.life/api/neko', headers=uagent)
    return n['neko']