from flask import session, redirect, url_for
from functools import wraps


def logged_in(f):
    """Wrapper that checks if the user is logged in to access a page."""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # If the user is not logged in, then redirect them.
        if not session.get("user"):
            return redirect(url_for("login.loginpage"))

        else:
            return f(*args, **kwargs)

    return wrapper
