## ServerStatus

### How to run the server? 
1. Make sure you have `python` and `flask` installed
2. run `python3 server.py`

```
> python3 server.py
 * Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 940-971-154
127.0.0.1 - - [23/Apr/2024 23:11:35] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [23/Apr/2024 23:11:37] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [23/Apr/2024 23:11:39] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [23/Apr/2024 23:11:41] "GET /status HTTP/1.1" 200 -
^C

```

### How to use the client library? 
```
# Usage
client = StatusClient("http://127.0.0.1:5000")

In real world, we replace `http://127.0.0.1:5000` with the server url. Client might include API key in the request in order to call the server.
```

The client library implemented a naive approach to wrap the errors. A more advanced approach would be calling the server with retry. For example, with a fixed backoff of 500ms and retry for maximum of 3 times; or with an exponential backoff. I'm more familiar with Java and have used `spring retry`. I did some reserch and for Python there's a library called `Tenacity` can be used. 

```
> python3 client.py
completed
```

### How to run integration test? 
```
python3 IntegrationTest.py
```

Result: 

```
> python3 IntegrationTest.py
 * Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [23/Apr/2024 23:09:30] "GET /status HTTP/1.1" 200 -
.
----------------------------------------------------------------------
Ran 1 test in 1.018s

OK
```