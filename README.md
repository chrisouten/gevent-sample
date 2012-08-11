gevent-sample
=============

Just a simple project for messing around with gevent.

Setup
=============

You will need the python packages in the requirements.pip file

    pip install -r requirements.pip
    

Running the Server
=============

The server is a simple Flask/gevent server

    python server.py
    
Functions
=============

Getting a fibonacci number

    $ curl -s 'http://127.0.0.1:8080/fib/13'
    {"response":233}
    
    