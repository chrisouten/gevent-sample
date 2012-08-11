gevent-sample
=============

Just a simple project for messing around with gevent.

Setup
=============

You will need the python packages in the requirements.pip file

    pip install -r requirements.pip
    
If you have issues installing the requirements here are some libraries you might need

    libxml2-dev
    libxslt1-dev
    libevent-dev
    

Running the Server
=============

The server is a simple Flask/gevent server

    python server.py
    
Functions
=============

Getting a fibonacci number

    $ curl -s 'http://127.0.0.1:8000/fib/13'
    {"response":233}
    
Getting the sha-1 of the body content from google.com

    $ curl -s 'http://127.0.0.1:8000/google-body'
    {"response": "b86941fa05cc1b5f2bad1076dcdba8df1c520a87"}
    
    
    
    