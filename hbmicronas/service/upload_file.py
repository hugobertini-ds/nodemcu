import re
from microdot import Microdot

upload_file_app = Microdot()

@upload_file_app.get('')
def get_file(request):
    # file upload form
    with open('file_upload.html', 'r') as f:
        return(f.read()), 202, {'Content-Type': 'text/html'}


@upload_file_app.post('')
def post_file(request):
    #force files to be available at stream
    request.max_body_length = 0
    # process file upload
    print('Processing file upload...')
    r = f"""
    ... <h2>Request info</h2>
    ... method:        {request.method}<br>
    ... path:          {request.path}<br>
    ... args:          {request.args}<br>
    ... headers:       {request.headers}<br>
    ... cookies:       {request.cookies}<br>
    ... content_type:  {request.content_type}<br>
    ... content_length:{request.content_length}<br>
    ... client_addr:   {request.client_addr}<br>
    ... form name:     {request.form}<br>
    ... body:          {request.body}<br>
    """

    # get body
    bd = request.body.decode('utf-8')
    print(f"Request body: {bd}")
    
    # get file name 
    ref_start_str = '='
    fn = bd.partition(ref_start_str)[2]
    print(f"filename: {bd.partition(ref_start_str)}")        
    print(f"filename: {fn}")    

    # saving the file locally
    with open(fn, "w") as f:
        f.write()
    
    return fn + " uploaded.</h2>", 202, {'Content-Type': 'text/html'}






