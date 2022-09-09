import re
from microdot import Microdot

uploadfile_app = Microdot()

@uploadfile_app.get('')
def get_file(request):
    # file upload form
    with open('uploadfile.html', 'r') as f:
        return(f.read()), 202, {'Content-Type': 'text/html'}


@uploadfile_app.post('')
def post_file(request):
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
    #print(f"Request body: {bd}")
    
    # get file name 
    ref_start_str = 'filename="'
    ref_end_str   = '"'
    fn = bd.partition(ref_start_str)[2].partition(ref_end_str)[0]
    print(f"file name: {fn}")
        
    # get file content
    ref_start_str = "Content-Type: text/plain\r\n\r\n"
    ref_end_str   = "----"
    fc = bd.partition(ref_start_str)[2].partition(ref_end_str)[0]
    #print(f"File content: {fc}")
    
    # saving the file locally
    with open(fn, "w") as f:
        f.write(fc)
    
    return fn + " uploaded.</h2>", 202, {'Content-Type': 'text/html'}
