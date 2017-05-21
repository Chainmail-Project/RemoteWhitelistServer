import os
import json

import flask

app = flask.Flask(__name__)

whitelist_path = os.path.join(os.getcwd(), "whitelist.json")
if not os.path.isfile(whitelist_path):
    whitelist = {}
    with open(whitelist_path, "w") as f:
        json.dump(whitelist, f)
else:
    with open(whitelist_path) as f:
        whitelist = json.load(f)


@app.route("/auth")
def handle_auth():
    uuid = flask.request.args.get("uuid")
    if uuid in whitelist:
        return flask.jsonify(whitelisted=True)
    else:
        return flask.jsonify(whitelisted=False)


app.run("0.0.0.0", "8796")
