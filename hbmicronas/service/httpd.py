
from microdot import Microdot


from download_file import download_file_app
from upload_file import upload_file_app
from show_storage import show_storage_app
#from system import system_app


def create_app(): 
   app = Microdot() 
   app.mount(download_file_app, url_prefix='/<re:download.*:name>') 
   app.mount(upload_file_app, url_prefix='/upload')      
   app.mount(show_storage_app, url_prefix='/<re:show_storage.*:name>')    
   #app.mount(system_app, url_prefix='/<re:system.*:action>')       
   return app 


app = create_app()   

@app.route('/')
def index(request):
    return 'Hello, world!'
    

def start_server(a, p):
    print('Starting microdot app')
    try:
        print(f"bringing http service up on port {p}...")
        a.run(port=p)
    except:
        print("bringing http service down...")
        a.shutdown()
        
        

start_server(app, 8080)







@app.route('/shutdown')
def shutdown(request):
    app.shutdown()

@app.get('/users/<username>')
def get_user(request, username):
    return 'User: ' + username

@app.get('/users/<firstname>/<lastname>')
def get_1st_last(request, firstname, lastname):
    return 'User: ' + firstname + ' ' + lastname



