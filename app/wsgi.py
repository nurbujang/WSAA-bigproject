
# entry point
#import sys
#path = '/home/nurbujang/mysite/bigproject-WSAA/'
# when testing locally, use this:
# path = '.'

# if path not in sys.path:
#     sys.path.insert(0, path)

from app import app

#from app.application import app #as application
# replace above

# wsgi (this file) doesn't work
# flask --app wsgi.py run
# should be run inside the app/ folder
if __name__=='__main__':
    app.run()
    print('running from __name__')

print('wsgi file')