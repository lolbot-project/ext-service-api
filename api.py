import flask
import requests
from flask import jsonify
from raven.contrib.flask import Sentry
secret_sentry = open('./secrets/sentry')
secret_udic = open('./secrets/urban')
app = flask.Flask(__name__)
sentry = Sentry(app, dsn=secret_sentry.read())

dad_headers = {
    'Accept': 'text/plain',
    'User-Agent': 'flsk (Flask API) - https://github.com/tilda/flsk'
}

uagent = {
    'User-Agent': 'flsk (Flask API) - https://github.com/tilda/flsk'
}

urban_headers = {
    'X-Mashape-Key': secret_udic.read().rstrip(),
    'X-Mashape-Host': 'mashape-community-urban-dictionary.p.mashape.com',
    'Accept': 'application/json'
}

@app.route("/")
def root():
    res = {
            'message': 'Welcome to flsk!',
            'source': 'https://github.com/tilda/flsk',
            'thanks': 'for visiting!'
          }
    return jsonify(res)
@app.route("/api/joke")
def joke():
    jok = requests.get('https://icanhazdadjoke.com', headers=dad_headers)
    return jok.text

@app.route("/api/neko")
def neko():
    n = requests.get('https://nekos.life/api/neko', headers=uagent)
    return n.json()['neko']

@app.route("/api/urban/<word>")
def urban(word):
    u = requests.get('https://mashape-community-urban-dictionary.p.mashape.com/define?term={0}'.format(word), headers=urban_headers)
    if u.status_code == 200:
        d = u.json()
        d = d['list'][0]
        res = {
            'definition': d['definition'],
            'link': d['permalink']
        }
        return jsonify(res)
    else:
        res = {'error': u.status_code}
        print(u.text)
        return jsonify(res), u.status_code

