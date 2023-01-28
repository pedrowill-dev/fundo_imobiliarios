from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.firefox.service import Service
from src.infra.interfaces.webdriver.driver import WebdriverBrowser
from selenium import webdriver


class Firefox(WebdriverBrowser):

  def __init__(self):
    self.service = Service(GeckoDriverManager().install())
    self.browser = webdriver.Firefox(service=self.service)

  @property
  def get_driver(self):
    return self.browser
  