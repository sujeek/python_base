from wsgi_route import app
from wsgiref.simple_server import make_server


@app.route('/')
def index():
    return "hello world"


@app.route('/hello')
def hello():
    log()
    return "I say hello"


def log():
    print "logging"


if __name__ == "__main__":
    httpd = make_server("127.0.0.1",8888,app)
    httpd.serve_forever()