from src.controllers.ETL.extract import ExtractController
from src.controllers.ETL.transform import TransformController
from src.controllers.ETL.load import LoadController
from src.infra.database.connection_db import DBConnectionHandlerSQL
from src.infra.webdriver.chrome import Chrome
from src.infra.webdriver.firefox import Firefox

def main():

  instance_database = DBConnectionHandlerSQL()
  
  instance_webdriver = Chrome()
  webdriver = instance_webdriver.get_driver

  controller_extract = ExtractController(browser=webdriver)
  controller_response_extract = controller_extract.handle()

  controller_transform = TransformController(extract=controller_response_extract)
  controller_transform = controller_transform.handle()
  
  controller_load = LoadController(data=controller_transform, repositorie=instance_database)
  controller_load.handle()


  a=1