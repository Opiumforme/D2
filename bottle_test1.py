import sentry_sdk
import os

from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://bfc844c58c804666a4873c2dfe157ace@o1005073.ingest.sentry.io/5965960",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    raise RuntimeError("There is an error!")
    return


@app.route('/success')
def index():
    return


@app.route('/fail')
def index():
    raise RuntimeError("There is an error!")
    return


if os.environ.get('APP_LOCATION') == 'heroku-20':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    app.run(host='localhost', port=8080, debug=True)