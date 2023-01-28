from src.useCases.ETL.transform import TransformProcessUseCase


transform_data = TransformProcessUseCase()


data_test = [
{'liq_dia': '499.972', 'ult_rend': 'R$ 0,10', 'div_yield': '0,99%', 'pat_liq': 'R$ 2,3 bi', 'vlr_pat': 'R$ 10,11', 'ren_mes': '1,90%', 'p_vp': '', 'fundo': 'mxrf11'},
{'liq_dia': '236.868', 'ult_rend': 'R$ 0,09', 'div_yield': '0,96%', 'pat_liq': 'R$ 667,5 mi', 'vlr_pat': 'R$ 9,16', 'ren_mes': '5,68%', 'p_vp': '', 'fundo': 'vghf11'},
{'liq_dia': '32.464', 'ult_rend': 'R$ 0,56', 'div_yield': '0,85%', 'pat_liq': 'R$ 1,9 bi', 'vlr_pat': 'R$ 75,57', 'ren_mes': '-0,78%', 'p_vp': '', 'fundo': 'bcff11'},
{'liq_dia': '69.802', 'ult_rend': 'R$ 0,07', 'div_yield': '0,78%', 'pat_liq': 'R$ 311,2 mi', 'vlr_pat': 'R$ 10,42', 'ren_mes': '-0,33%', 'p_vp': '', 'fundo': 'vslh11'},
{'liq_dia': '9.436', 'ult_rend': 'R$ 0,10', 'div_yield': '1,14%', 'pat_liq': 'R$ 213,4 mi', 'vlr_pat': 'R$ 9,83', 'ren_mes': '-1,55%', 'p_vp': '', 'fundo': 'game11'},
{'liq_dia': '124.205', 'ult_rend': 'R$ 0,10', 'div_yield': '1,11%', 'pat_liq': 'R$ 302,9 mi', 'vlr_pat': 'R$ 9,37', 'ren_mes': '2,02%', 'p_vp': '', 'fundo': 'mchf11'},
{'liq_dia': '27.392', 'ult_rend': 'R$ 2,20', 'div_yield': '1,34%', 'pat_liq': 'R$ 3,6 bi', 'vlr_pat': 'R$ 154,03', 'ren_mes': '2,45%', 'p_vp': '', 'fundo': 'hglg11'},
{'liq_dia': '45.790', 'ult_rend': 'R$ 0,90', 'div_yield': '0,91%', 'pat_liq': 'R$ 2,1 bi', 'vlr_pat': 'R$ 101,27', 'ren_mes': '5,74%', 'p_vp': '', 'fundo': 'xpml11'},
{'liq_dia': '18.475', 'ult_rend': 'R$ 1,00', 'div_yield': '0,71%', 'pat_liq': 'R$ 3,9 bi', 'vlr_pat': 'R$ 159,84', 'ren_mes': '-0,63%', 'p_vp': '', 'fundo': 'knri11'},
{'liq_dia': '16.501', 'ult_rend': 'R$ 1,10', 'div_yield': '0,89%', 'pat_liq': 'R$ 1,9 bi', 'vlr_pat': 'R$ 156,89', 'ren_mes': '-4,49%', 'p_vp': '', 'fundo': 'hgre11'},
{'liq_dia': '19.936', 'ult_rend': 'R$ 1,20', 'div_yield': '1,17%', 'pat_liq': 'R$ 1,6 bi', 'vlr_pat': 'R$ 100,96', 'ren_mes': '0,67%', 'p_vp': '', 'fundo': 'hgcr11'},
{'liq_dia': '46.857', 'ult_rend': 'R$ 0,86', 'div_yield': '0,86%', 'pat_liq': 'R$ 1,1 bi', 'vlr_pat': 'R$ 97,31', 'ren_mes': '1,90%', 'p_vp': '', 'fundo': 'rztr11'},
{'liq_dia': '26.746', 'ult_rend': 'R$ 2,00', 'div_yield': '1,64%', 'pat_liq': 'R$ 2,3 bi', 'vlr_pat': 'R$ 122,89', 'ren_mes': '0,35%', 'p_vp': '', 'fundo': 'hgru11'},
{'liq_dia': '423.811', 'ult_rend': 'R$ 0,15', 'div_yield': '1,51%', 'pat_liq': 'R$ 696,4 mi', 'vlr_pat': 'R$ 9,53', 'ren_mes': '1,81%', 'p_vp': '', 'fundo': 'vgia11'},
{'liq_dia': '236.868', 'ult_rend': 'R$ 0,09', 'div_yield': '0,96%', 'pat_liq': 'R$ 667,5 mi', 'vlr_pat': 'R$ 9,16', 'ren_mes': '5,68%', 'p_vp': '', 'fundo': 'vghf11'},
{'liq_dia': '45.790', 'ult_rend': 'R$ 0,90', 'div_yield': '0,91%', 'pat_liq': 'R$ 2,1 bi', 'vlr_pat': 'R$ 101,27', 'ren_mes': '5,74%', 'p_vp': '', 'fundo': 'xpml11'},
{'liq_dia': '28.186', 'ult_rend': 'R$ 0,85', 'div_yield': '0,80%', 'pat_liq': 'R$ 2,3 bi', 'vlr_pat': 'R$ 123,83', 'ren_mes': '3,29%', 'p_vp': '', 'fundo': 'visc11'}
]


def test_columns_equals_data_test():
  cols_test = ['liq_dia', 'ult_rend', 'div_yield', 'pat_liq', 'vlr_pat', 'ren_mes', 'p_vp', 'fundo']
  data_df = transform_data.dataframe_dict(data=data_test)
  
  assert cols_test == list(data_df.columns) 

