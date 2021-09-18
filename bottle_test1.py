import sentry_sdk

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


app.run(host='localhost', port=8080)