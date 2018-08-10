from app import app, jwt
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from models import *
from functools import wraps

def is_admin(current_user):
    if current_user.status == 'admin':
        return True

def check_like(likes, current_user):
    for like in likes:
        if like.owner_id == current_user.id:
            return True
        else:
            pass

def member_only(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Set to true atm, set to be implemented at a later stage.
        return True
        # Check if the current user is a member.
        # current_user = load_user(get_jwt_identity())
        # current_user = User.query.filter_by(username=get_jwt_identity()).first()
        # if current_user.member == True:
        #     pass
        # else:
        #     return {'message': 'You are not a member!'}, 401
        return f(*args, **kwargs)
    return decorated

def load_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {'message': 'User does not exist!'}, 404
    else:
        return user