#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Aug 02 2022
@author: Zhen
Initialize the database
to initialize, run:
flask --app remedies init-db
"""

import sqlite3

import click
from flask import current_app, g
# current_app: the Flask application handling the request
# g: store data that might be accessed by multiple functions during the request. 
#    The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request.

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row tells the connection to return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # design of db see schema.sql
    # open_resource no need explicit location of the .sql file
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# defines a command line command called init-db that calls the init_db function and
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# register close_db and init_db_command to the app will be generated from App Factory in __init__
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)