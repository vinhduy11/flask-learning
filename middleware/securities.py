from functools import wraps
from flask import session, redirect, url_for
from libs.logger import logger

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if user is not logged in, redirect to login page      
        if not 'username' in session:
            return redirect(url_for('authorized.login_page'))
        # finally call f. f() now haves access to g.user
        return f(*args, **kwargs)
    return wrap