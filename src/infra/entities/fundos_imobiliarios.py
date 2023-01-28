from pydantic import BaseModel

class FundoImobiliario(BaseModel):
  fundo: str
  liq_dia : int
  ult_rend : float
  div_yield : float
  vlr_pat : float
  ren_mes : float
  p_vp : float


  

