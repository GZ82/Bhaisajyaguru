#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Created on Aug 02 2022
@author: Zhen
The __init__.py serves double duty: 
it will contain the application factory, 
and it tells Python that the remedies directory should be treated as a package

run:
flask --app flaskr --debug run

"""


import os

from flask import Flask


# Application factory: return applications
def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config=True: configuration files are relative to the instance flolder, rather than the application-remedies
            # while data can keep outside instance folder will not be commited during version control
            # to use config in remedies: app.config.from_object('yourapplication.default_settings')
            # to use config in instance folder: app.config.from_pyfile('application.cfg', silent=True
    # the instance folder can be specified by developer: app = Flask(__name__, instance_path='/path/to/instance/folder')
    # otherwise it will be in parallel with the package folder, i.e., Bhaisajyaguru/Bhaisajyaguru/instance
    # for installed package: either $PREFIX/lib/pythonX.Y/site-packages/myapp or $PREFIX/var/myapp-instance
    # to get instance folder: app.instance_path
    # to open file in instance folder: with app.open_instance_resource('application.cfg') as f: config = f.read()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'remedies.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # register close_db and init_db_command to the app
    from . import db
    db.init_app(app)

    return app
