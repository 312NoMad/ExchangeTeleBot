import psycopg2
from sqlalchemy import create_engine
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user='hello', password='1')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
sql_create_database = 'exchange'

cursor.execute('create database sqlalchemy_tuts')

cursor.close()
connection.close()

engine = create_engine('postgresql+psycopg2://hello:1@8000/mydb',
                       echo=True, pool_size=6, max_overflow=10, encoding='latin1')
engine.connect()

print(engine)
