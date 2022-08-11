#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Aug 02 2022
@author: Zhen

Flask views:
* A view function respond to requests to your application. 
* views uses patterns to match the incoming request URL.
* The view returns data that Flask turns into an outgoing response. 
* Flask can also go the other direction and generate a URL to a view based on its name and arguments.

Flask Blueprints:
* views do not directly register to you app, but via Blueprints: view -register-blueprint-regester->app
* A Blueprint is a way to organize a group of related views and other code. 

session:
* session is a dict that stores data across requests. 
* When validation succeeds, the user id is stored in a new session. 
* The data is stored in a cookie that is sent to the browser, 
* and the browser then sends it back with subsequent requests. 
* Flask securely signs the data so that it can not be tampered with.

g:

endpoint and url_for:
endpoint: The name associated with a view, idea the function name, e.g., register, login, ...
url_for: takes the name/function of the view, and args for the name/function and generate an URL for the view
         example: url_for('hello', who='World')

# This Blueprint is for authentication functions, can create a separate one for other functions e.g., blog posts functions
"""

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# create blueprint auth
# __name__ indicate where it was defined
# url_prefix: in future bp.route == '~/auth/xxx'
bp = Blueprint('auth', __name__, url_prefix='/auth')
# now can import and register auth in __init__.py

# ------ register ------ #
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # why if POST
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                #  url_for() generates the URL for the login view based on its name.
                return redirect(url_for("auth.login"))
        # flash() stores messages that can be retrieved when rendering the template.
        flash(error)

    return render_template('auth/register.html')

# ------ login ------ #
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # Now that the user’s id is stored in the session, it will be available on subsequent requests. 
            # At the beginning of each request, if a user is logged in their information 
            # should be loaded and made available to other views.
            session.clear()
            session['user_id'] = user['id']
            # an index.html will be created under templates/blog/
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# ------ before app request ------ #
# bp.before_app_request() registers a function that runs before the view function, no matter what URL is requested.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# ------ logout ------ #
# To log out, you need to remove the user id from the session. Then load_logged_in_user won’t load a user on subsequent requests.
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# ------ require auth in other views ------ #
# create a decorator for all other views in blog
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # NOTE: this direct to the view login, 
            # because login is under the Blueprint auth so the name for url_for here is auth.login
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
