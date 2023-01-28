from abc import abstractmethod, ABC


class WebdriverBrowser(ABC):

  @abstractmethod
  def get_driver():
    raise NotImplementedError






