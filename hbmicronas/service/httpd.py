
from microdot import Microdot

app = Microdot()

@app.route('/')
def index(request):
    return 'Hello, world!'

@app.get('/users/<username>')
def get_user(request, username):
    return 'User: ' + username

@app.get('/users/<firstname>/<lastname>')
def get_1st_last(request, firstname, lastname):
    return 'User: ' + firstname + ' ' + lastname

@app.route('/shutdown')
def shutdown(request):
    app.shutdown()


def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()