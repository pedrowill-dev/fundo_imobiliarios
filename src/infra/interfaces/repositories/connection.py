from abc import abstractmethod, ABC


class DBConnection(ABC):
  @abstractmethod
  def connection():
    raise NotImplementedError


