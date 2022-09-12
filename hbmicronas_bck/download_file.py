from microdot import Microdot 
from microdot import send_file


download_file_app = Microdot() 


@download_file_app.get('')
def get_file(request, name): 
    nm = name.replace('..', '').replace('files', '').replace('/', '')
    if len(nm) > 0:
       # send file to client
       print('downloading file: ' + nm)
       #return send_file('/static/index.html')
       #return 'downloading file: ' + nm, 202
       return send_file(nm)
    else:
       return get_filelist()


def get_filelist(): 
    # return all customers 
    print('getting file list')
    #return send_file('/static/index.html')
    return 'file list', 202
 
 # process a file download request
   #with open(filename, "r") as f:
   #   return f.read()
   #return send_file(filename)
