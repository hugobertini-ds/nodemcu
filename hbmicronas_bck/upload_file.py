from microdot import Microdot 


upload_file = Microdot() 


@upload_file.get(request) 
def get_file(request): 
   # display the file upload form
   with open("file_upload.html", "r") as f:
      return f.read(), 202, {'Content-Type': 'text/html'}
   

@download_file.post('<filename>') 
def new_customer(request): 
   # process a file upload request
   #TODO: implement upload logic
   return "uploading a file...", 202, {'Content-Type': 'text/html'}
   