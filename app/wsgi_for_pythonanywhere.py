# when testing locally, path can be commented out
# flask --app wsgi.py run
# should be run inside the app/ folder

# replace the contents in
#  /var/www/nurbujang_pythonanywhere_com_wsgi.py
# with these

import sys

path = "/home/nurbujang/mysite/bigproject-WSAA/app"
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application

if __name__ == "__main__":
    application.run()
    print("running from __main__")
