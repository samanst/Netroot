import time
from flask import g
from flask.sessions import SecureCookieSessionInterface


def timestamp() -> int:
    """
    Return the current timestamp as an integer
    :return: <int> timestamp
    """
    return int(time.time())


class SessionInterface(SecureCookieSessionInterface):

    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(SessionInterface, self).save_session(*args, **kwargs)
