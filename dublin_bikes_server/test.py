import os
from dublin_bikes_server import main
import unittest
import tempfile
from dublin_bikes_server.link_to_mysql import *


'''class MyTest(TestCase):
    rds_db = rds_config()
    rds_db.db_config_setup()
    
    host = rds_db.db_endpoint
    name = rds_db.db_username
    password = rds_db.db_password
    db = rds_db.db_name
    port = 3306

    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://{}:{}@{}:{}/{}"
                               .format(name, password, host, port, db), echo=True)
    TESTING = True

    def create_app(self):
        # pass in test configuration
        return create_app(self)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()'''