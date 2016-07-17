"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, redirect, url_for, request
from utils.question import Question
import json
import logging

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return appindex()


@app.route('/me/index.html')
def index():
    """Return the index page for me"""
    return redirect(url_for('static', filename='mypage/index.html'))

@app.route('/app/index.html')
def appindex():
    return redirect(url_for('static', filename='apppage/index.html'))

@app.route('/app/show_store')
def print_store():
    storefile = open('store/store.json', 'r').read()
    logging.info("storefile: {}".format(str(storefile)))
    # store = json.loads(str(storefile))
    # return store
    return str(storefile)

@app.route('/question', methods=['POST'])
def question():
    if (request.data != None):
        process(request.data)
    else:
        raise Exception
    return ""

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    logging.warn("not found {}".format(e))
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    logging.error("Server problem {}".format(e))
    return 'Sorry, unexpected error: {}'.format(e), 500

def process(object):
    logging.info(str(object))
    q = Question()