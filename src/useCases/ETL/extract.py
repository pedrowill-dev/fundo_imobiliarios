from selenium.webdriver.common.by import By

class ExtractFundoUseCase:

  url_fundos = 'https://www.fundsexplorer.com.br/funds/'

  def __init__(self, browser):
    self.browser = browser

  def open_browser_fundo(self, fundo):
    self.browser.get(self.url_fundos + fundo)

  def take_info_fundo(self):
    class_name = 'indicator-value'
    element_classname = self.browser.find_elements(By.CLASS_NAME, class_name)
    return element_classname

  def extract_values_fundos(self, element_fundos):
    fundos = []
    for fundo in element_fundos:
      fundos.append(fundo.text)
    return fundos
      
  
  def structured_data_fundo(self, fundos_data, fundo):
    keys_fundos = ['liq_dia', 'ult_rend', 'div_yield', 'pat_liq', 'vlr_pat', 'ren_mes', 'p_vp']
    value_final_structured = dict(zip(keys_fundos, fundos_data))
    value_final_structured.update({'fundo': fundo})
    return value_final_structured
