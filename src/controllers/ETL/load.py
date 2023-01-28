from src.useCases.ETL.load import LoadUseCase
import pandas as pd
from src.infra.interfaces.repositories.connection import DBConnection
class LoadController:

  fundos = ['mxrf11', 'vghf11', 'bcff11', 'vslh11', 'game11', 'mchf11', 'hglg11', 'xpml11', 'knri11', 'hgre11', 'hgcr11', 'rztr11', 'hgru11', 'vgia11', 'vghf11', 'xpml11', 'visc11', 'mall11', 'lvbi11']
  
  def __init__(self, repositorie: DBConnection, data: pd.DataFrame):
    self.repositorie = repositorie
    self.data = data
    self.load = LoadUseCase(self.repositorie)

  def handle(self):
    try:
      self.load.upload(table='FUNDOS_IMO', data=self.data,)
    except Exception as error:
      print(error)