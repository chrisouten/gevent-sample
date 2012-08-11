import hashlib
import json
import urllib2

from flask import Flask, request
from gevent.pywsgi import WSGIServer
from lxml import html
import redis

app = Flask(__name__)
app.debug = True
app.redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

REDIS_SV_KEY = 'special_value'

def get_fibonacci(val):
    if val in [0,1]:
        return val
    else:
        return get_fibonacci(val-1) + get_fibonacci(val-2)

@app.route('/fib/<int:val>')
def fibonacci(val):
    fib_n = get_fibonacci(val)
    return json.dumps({"response": fib_n})
    
@app.route('/google-body')
def google_body():
    html_data = urllib2.urlopen('http://www.google.com')
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