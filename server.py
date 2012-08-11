import hashlib
import json
import urllib2

from flask import Flask
from gevent.pywsgi import WSGIServer
from lxml import html

app = Flask(__name__)
app.debug = True

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
        
if __name__ == "__main__":
    http = WSGIServer(('', 8000), app)
    http.serve_forever()