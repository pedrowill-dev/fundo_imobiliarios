import urllib

"""File configurantion database"""
class ConfigurationDabatase:
  
  driver = 'SQL Server'
  host_server = ''
  database = ''
  user = ''
  password = ''
  connection_string = f'mssql+pyodbc://{user}:{urllib.parse.quote_plus(password)}@{host_server}/{database}?driver={driver}'
