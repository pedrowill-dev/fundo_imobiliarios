from src.useCases.ETL.extract import ExtractFundoUseCase
class ExtractController:

  fundos = ['mxrf11', 'vghf11', 'bcff11', 'vslh11', 'game11', 'mchf11', 'hglg11', 'xpml11', 'knri11', 'hgre11', 'hgcr11', 'rztr11', 'hgru11', 'vgia11', 'vghf11', 'xpml11', 'visc11', 'mall11', 'lvbi11']
  
  def __init__(self, browser):
    self.browser = browser
    self.extract_use_case = ExtractFundoUseCase(self.browser)
    
  def handle(self) -> list:
    data_fundos = []
    
    for fundo in self.fundos:
      self.extract_use_case.open_browser_fundo(fundo)
      element_info_fundo = self.extract_use_case.take_info_fundo()
      extract_values_fundos = self.extract_use_case.extract_values_fundos(element_info_fundo)
      structured_data_fundos = self.extract_use_case.structured_data_fundo(extract_values_fundos, fundo)
      data_fundos.append(structured_data_fundos)
    
    return data_fundos
      
