import os

from bottle import route, run


@route('/')
def index():
    raise RuntimeError("There is an error!")
    return


@route('/success')
def index():
    return


@route('/fail')
def index():
    raise RuntimeError("There is an error!")
    return


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)