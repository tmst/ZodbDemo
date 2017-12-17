# -*- coding: utf-8 -*-

import os
from loader import PythonConfiguration


def get_key(path):
    from cromlech.jwt.components import JWTHandler
    if not os.path.isfile(path):
        with open(path, 'w+', encoding="utf-8") as keyfile:
            key = JWTHandler.generate_key()
            export = key.export()
            keyfile.write(export)
    else:
        key = JWTHandler.load_key_file(path)
    return key


def init_db(db):
    with PythonConfiguration('config.json') as config:
       """We create two leaves here.. We get the DB connection object.
       We need to open and to close it. It doesn't need to return anything.
       Make sure to use a transaction manager to have it correctly persisted.
       """
       from cromdemo.models import Root, Leaf
       conn = db.open()
       root = conn.root()
       if not hasattr(root,'applicationRoot'):
          appRoot=Root()
          root.applicationRoot=appRoot
          appRoot.__name__='root'
          appRoot['green'] = Leaf(u'Green leaf', u'A summer leaf')
          appRoot['yellow'] = Leaf(u'Yellow leaf', u'An automn leaf')
          import transaction
          transaction.commit()           


with PythonConfiguration('config.json') as config:

    # We setup the cache for Chameleon templates
    os.environ["CHAMELEON_CACHE"] = config['templates']['cache']

    # Bootstrapping the Crom registry
    from crom import monkey, implicit
    monkey.incompat()
    implicit.initialize()

    # We read the zodb conf and initialize it
    from cromlech.zodb import init_db_from_file
    with open(config['zodb']['config'], 'r') as fd:
        db = init_db_from_file(fd, init_db)
        
    # Getting the crypto key and creating the JWT service
    from dolmen.sessions.jwt import JWTCookieSession
    key = get_key(config['session']['jwt_key'])
    session_wrapper = JWTCookieSession(
        key, int(config['session']['timeout'])).wrapper
    
    # read the ZCML
    from cromlech.configuration.utils import load_zcml
    load_zcml(config['app']['zcml'])

    # load translation
    from cromlech.i18n import load_translations_directories
    load_translations_directories()

    # Create the application, including the middlewares.
    # I LEAVE THE FOLLOWING THREE LINES IN THE SOURCE CODE
    # BECAUSE THEY ARE PROALY NOT DOCUMENTED ANYWERHE,
    # BUT VERY IMPORTANT MAGICAL INCANTATIONS
    # First we do dispatch
    #from rutter import urlAmap
    #router = urlmap.URLMap()
    #router['/demo'] = demo
    
    from cromlech.zodb.middleware import ZODBApp
    from cromdemo.app import demo_application
    zodb_app =ZODBApp(demo_application, db, key="zodb.connection")
    application =session_wrapper(zodb_app)


