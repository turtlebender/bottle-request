"""
Exceedingly simple bottle plugin to add request as a "stateless" parameter to
web calls.. Having everything accessed through the "magic" thread
local is pretty ugly, and this lets us treat the request as a stateless object.
Note, even though this looks stateless, it is still the same threadlocal, but
it can be easily swapped.
"""
import inspect
from bottle import request

def inject_request(callback):
    """
    Wrap the function in a decorator which adds the request parameter if
    necessary.
    """
    args = inspect.getargspec(callback)[0]
    if 'request' not in args:
        return callback
    def wrapper(*args, **kwargs):
        """
        Pass request object as a function parameter if signature contains
        "request" as a parameter.
        """
        kwargs['request'] = request
        return callback(*args, **kwargs)
    return wrapper

Plugin = inject_request
