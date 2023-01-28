from src.models.DB.connection import DbSqlA
from src.infra.interfaces.repositories.connection import DBConnection

from src.config import ConfigurationDabatase


class DBConnectionHandlerSQL(DBConnection):
  

  instance_config = ConfigurationDabatase()

  def __init__(self):   
    self.__connection_string = self.instance_config.connection_string

  def connection(self):
    connection_db = DbSqlA(self.__connection_string)
    connection_db = connection_db.engine
    return connection_db

