import json

from flask import Flask
from gevent.pywsgi import WSGIServer

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
        
if __name__ == "__main__":
    http = WSGIServer(('', 8000), app)
    http.serve_forever()