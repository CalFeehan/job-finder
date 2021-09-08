from flask import Blueprint, json, request, jsonify, session, redirect
import re
import bcrypt
from functools import wraps
import jwt
import datetime
import uuid
from .db import User


def create_bcrypt_hash(password: str) -> str:
    '''creates a salt and hashes password'''

    # converts password to bytes
    password_bytes = password.encode()
    # generates salt
    salt = bcrypt.gensalt(8)
    # calculate hash as bytes
    password_hash_bytes = bcrypt.hashpw(password_bytes, salt)
    # converts bytes to string
    password_hash_str = password_hash_bytes.decode()

    return password_hash_str


def verify_password(password: str, stored_hash_str: str) -> bool:
    '''checks input password against stored hashed password'''

    password_bytes = password.encode()
    hash_bytes = stored_hash_str.encode()
    # this automatically retreives salt from stored hash,
    # combines it with input password, hashes this and compares to stored hash.
    if bcrypt.checkpw(password_bytes, hash_bytes):
        return True

    return False


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(
                public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator


auth = Blueprint('auth', __name__)


@auth.post('/login')
def login():
    # get from JQuery form.js
    email = request.form['login_email']
    password = request.form['login_password']

    #  if email already exists, gets stored password, else returns error
    if User.check_user_exists(email):
        stored_password = User.get_stored_password(email)
        # checks if input password matches stored password, if correct returns success, else returns error
        if verify_password(password, stored_password):
            token = jwt.encode({'public_id': User.public_id, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('UTF-8')})

    return jsonify({'error': 'Incorrect Username or Password'})


@auth.post('/create-account')
def create_account():
    # get from JQuery form.js
    email = request.form['create_account_email']
    password = request.form['create_account_password']
    confirm_password = request.form['create_account_confirm_password']

    # Checks if valid email input
    if not (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)):
        return jsonify({'error': 'Invalid Email Address'})
    # Checks is password at least 8 characters from allowed list
    elif not (re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password)):
        return jsonify({'error': 'Password must be at least 8 characters'})
    # Checks if password and confirm passwords match
    elif password != confirm_password:
        return jsonify({'error': 'Passwords do not match'})
    # Checks if email already in use
    elif User.check_user_exists(email):
        return jsonify({'error': 'Email already in use'})
    else:
        # Creates user, starts session
        User.add_user(str(uuid.uuid4()), email, create_bcrypt_hash(password))
        session['user_id'] = User.get_user_id(email)
        return jsonify({'success': 'login'})


@auth.post('/delete-user')
def delete_user():
    check = request.form['delete-text']
    if check == 'DELETE':
        User.delete_user(session['user_id'])
        return redirect('/logout')
    return "Please type DELETE"


@auth.post('/change-password')
def change_password():
    password = request.form['current-password']
    new_password = request.form['new-password']
    confirm_new_password = request.form['confirm-new-password']

    if not (re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', new_password)):
        return "Password must contain at least 8 characters"
    # Checks if password and confirm passwords match
    elif new_password != confirm_new_password:
        return "Passwords do not match"

    if verify_password(password, User.get_stored_password(User.get_user_email(session['user_id']))):
        new_password = create_bcrypt_hash(new_password)
        User.change_password(session['user_id'], new_password)

    return "Password changed"


@auth.route('/logout')
def logout():
    session['user_id'] = None

    return redirect('/')
