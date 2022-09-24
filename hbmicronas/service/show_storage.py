import os
#from utl import get_storage_space

from microdot import Microdot

show_storage_app = Microdot()

@show_storage_app.get('')
def list_files(request):
    resp = ""
    # get storage status
    resp += "<p>"
    resp += get_storage_space()
    resp += "</p>"

    # list files
    resp += "<p>"
    files = os.listdir()
    for f in files:
        resp += f"<a href='getfile/{f}'>{f}</a><br>"
    resp += "</p>"

    print(f"resp: {resp}")
    return resp, 202, {'Content-Type': 'text/html'}
