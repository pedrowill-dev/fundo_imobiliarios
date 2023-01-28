from sqlalchemy import orm
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime as dt

class DbSqlA():
  
    base        = declarative_base()
    def __init__(self,ConnectionString):
        self.engine                 = sa.create_engine(ConnectionString)
        self.session                = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=self.engine))
        self.base.query             = self.session.query_property()
        self.orm_session            = orm.scoped_session(orm.sessionmaker())(bind=self.engine)
        self.base.metadata.bind     = self.engine    

    def create_all(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.base.metadata.create_all(self.engine)
    
    def test_connection(self):
      return self.session.connection()

    def get_engine(self):
      return self.engine


