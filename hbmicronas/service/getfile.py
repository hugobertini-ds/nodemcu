from microdot import Microdot

getfile_app = Microdot()

@getfile_app.get('')
def getfile(request):
    # get a specific file
    return 'Get File', 202, {'Content-Type': 'text/html'}
