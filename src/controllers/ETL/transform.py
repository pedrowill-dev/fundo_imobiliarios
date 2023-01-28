from src.useCases.ETL.transform import TransformProcessUseCase
from pandas import DataFrame
class TransformController:

  keys_fundos = ['liq_dia', 'ult_rend', 'div_yield', 'vlr_pat', 'ren_mes', 'p_vp', 'fundo']
  
  def __init__(self, extract):
    self.data_extract = TransformProcessUseCase()
    self.data = extract

  def handle(self) -> DataFrame: 
    transform_data = self.data_extract.dataframe_dict(self.data)
    transform_data_df = self.data_extract.remove_caracteres(transform_data)
    return transform_data_df
    
    
      
