import flask
app = flask.Flask(__name__)

@app.route("/api/hi/<friendo>")
def hi(friendo):
    return "Oh hey, %s" % friendo
