def app(env, start_response):
    data = b'Hello from PORT 8000!!!'
    headers = [('Content-Type', 'text/plain'),
              ('Content-Length', str(len(data)))]
    start_response('200 OK', headers)
    return [data]
