from src.infra.interfaces.repositories.connection import DBConnection
from pandas import DataFrame
import pandas as pd

class LoadUseCase():

  def __init__(self, repositorie: DBConnection):
    self.repositorie = repositorie.connection()

  def upload(self, table, data: DataFrame):
    if not data.empty:
      data.to_sql(table, self.repositorie, index=False, if_exists='append')
  
  def select(self, query):
    return pd.read_sql(query)

  def delete(self, query):
    self.connection.execute(query)
  
  def create(self, query):
    self.connection.execute(query)
    
      