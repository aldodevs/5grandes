from flask import render_template
from flask import Flask, request
import facebook
from flask import json
app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/fb_success/')
def fb_success():
    access_token = request.args.get('access_token', '')

    try:
        graph = facebook.GraphAPI(access_token)
        profile = graph.get_object('me')
        query_string = 'posts?limit={0}'.format(10)
        posts = graph.get_connections(profile['id'], query_string)
        response = app.response_class(
            response=json.dumps(posts),
            status=200,
            mimetype='application/json'
        )
        return response
    except facebook.GraphAPIError:
        return None
