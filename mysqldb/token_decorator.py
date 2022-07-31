from Jwt import decode
from flask import request
from functools import wraps

def token_required(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        token = request.headers.get('token')
        if not token:
           return "Token Not Provided",403
        try:
           decode(token)
           return func(*args,**kwargs)
        except:
           return "Invalid Token",403
    return decorator
