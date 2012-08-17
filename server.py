import hashlib
import json
import urllib2

from flask import Flask, request
from gevent.pywsgi import WSGIServer
from lxml import html
import redis

#Setting up our simple Flask server
#  Adding a redis db to it.  I'm pretty sure there is
#  a better way to do this, but I don't have a lot of
#  experience with Flask.
app = Flask(__name__)
app.debug = True
app.redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

#Our special key for the redis db store
REDIS_SV_KEY = 'special_value'

def get_fibonacci(val):
    '''
    Simple fibonacci function
    Takes a positive integer and returns the value
    '''
    if val in [0,1]:
        return val
    else:
        return get_fibonacci(val-1) + get_fibonacci(val-2)
        
def faster_fibonacci(val):
    a,b = 1,1
    for x in xrange(val-1):
        a,b = b, a + b
    return a

@app.route('/fib/<int:val>')
def fibonacci(val):
    fib_n = faster_fibonacci(val)
    return json.dumps({"response": fib_n})
    
@app.route('/google-body')
def google_body():
    # Get the html data using urllib2
    html_data = urllib2.urlopen('http://www.google.com')
    # Using lxml we get the body element's text content, then encode that
    # using the charset value from the headers
    body_data = html.parse(html_data).xpath('body')[0].text_content().encode(html_data.headers.getparam('charset'))
    return json.dumps({'response':hashlib.sha1(body_data).hexdigest()})
    
@app.route('/store')
def retrieve_value():
    return json.dumps({'response':app.redis_db.get(REDIS_SV_KEY)})

@app.route('/store', methods=["POST"])
def store_value():
    app.redis_db.set(REDIS_SV_KEY,request.form['value'])
    return json.dumps({'response':app.redis_db.get(REDIS_SV_KEY)})
        
if __name__ == "__main__":
    http = WSGIServer(('', 8000), app)
    http.serve_forever()