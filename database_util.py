import psycopg2
import os

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = None
config = {
  'host': os.environ.get('DATABASE_URI'),
  'user': os.environ.get('DATABASE_USER'),
  'password': os.environ.get('DATABASE_PASSWD'),
  'dbname': 'postgres'
}
def setup():
  global connection, config
  if connection is not None:
      return connection
  connection = psycopg2.connect(**config)
  connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
  return connection

def handler(event, context):
  response = None; cursor = None
  try:
    cursor = setup().cursor()
    cursor.execute(event['command'])
  except Exception as err:
    response = {'message': str(err), 'error': True}
  else:
    response = {'message': 'ok'}
  finally:
    if cursor is not None:
      cursor.close()
  return response
