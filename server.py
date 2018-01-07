# -*- coding: utf-8 -*-

import os
from loader import PythonConfiguration



def init_db(db):
    with PythonConfiguration('config.json') as config:
       """
       Initialize the ZODB if needed.
       """
       from cromdemo.models import Root, Leaf
       conn = db.open()
       root = conn.root()
       if not hasattr(root,'applicationRoot'):
          appRoot=Root()
          root.applicationRoot=appRoot
          appRoot.__name__='root'
          import transaction
          transaction.commit()           
#          appRoot['yellow'] = Leaf()
          appRoot['green'] = Leaf('Green leaf', 'A summer leaf')
          appRoot['yellow'] = Leaf('Yellow leaf', 'An automn leaf')

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
    from cromlech.sessions.jwt import key_from_file
    from cromlech.sessions.jwt import JWTCookieSession 

    key = key_from_file(config['session']['jwt_key'])
    session_wrapper = JWTCookieSession(
        key, int(config['session']['timeout']))
    
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


