#!/usr/bin/env python3
import ipdb
from app import app
from models import *

if __name__ == "__main__":
    with app.app_context():

        # Code to query the database goes here
        pass

    ipdb.set_trace()

    """
    Once you invoke the debugger, you will lose the app context, which means you will not be able to exacute new queries or session commits without it.  However, you can reqcquire it in the ipdb prompt by running 'with app.app_context():' again followed by your code
    """
