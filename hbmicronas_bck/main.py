from microdot import Microdot


from download_file import download_file_app


def create_app(): 
   app = Microdot() 
   app.mount(download_file_app, url_prefix='/<re:files.*:name>') 
   return app 
   
   
app = create_app()
app.run(port=8080)
