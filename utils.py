from flask import request
from flask_restx import abort
import jwt

from constants import JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algoruthms=[JWT_SECRET])
        except Exception as e:
            print('JWT Decode exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper



def admine_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            user = jwt.decode(token, JWT_SECRET, algoruthms=[JWT_SECRET])
            if user['role'] != 'admin':
                abort(401)

        except Exception as e:
            print('JWT Decode exception', e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


