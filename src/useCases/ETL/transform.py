import pandas as pd
from pandas import DataFrame

class TransformProcessUseCase:

  def dataframe_dict(self, data: dict) -> DataFrame:
    return pd.DataFrame(data)
  
  
  def remove_caracteres(self, data):
    caracters_clean = {
      'liq_dia': [['.', '']],
      'ult_rend': [['R', ''], ['$', ''], [',', '.'], [' ', '']],
      'div_yield': [[',', '.'], ['%', '']],
      'pat_liq': [['R', ''], ['$', ''], ['.', ''], [',', ''], [' ', ''], ['mi', '0'*5], ['bi', '0'*10]],
      'vlr_pat':  [['R', ''], ['$', ''], [',', '.'], [' ', '']],
      'ren_mes': [[',', '.'], ['%', '']],
      'p_vp': [[',', '.']]
    }
    for item_caracter in caracters_clean:
      if len(caracters_clean[item_caracter]) > 1:
        for item_sub in caracters_clean[item_caracter]:
          caracter_before = item_sub[0]
          caracter_after = item_sub[1]
          data[item_caracter] = data[item_caracter].str.replace(caracter_before, caracter_after)
      else:
        caracter_before = caracters_clean[item_caracter][0][0]
        caracter_after = caracters_clean[item_caracter][0][1]
        data[item_caracter] = data[item_caracter].str.replace(caracter_before, caracter_after)
    
    return data