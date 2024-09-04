from datetime import datetime as dt
import os
name = dt.now()

file_path = "/"

def user_app():
    if os.path.exists('./file'):
        print('Good')
    else:
        print('No good')
        open('./file', 'w')

user_app()