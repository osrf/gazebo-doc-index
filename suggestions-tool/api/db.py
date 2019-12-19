import psycopg2, os
from urllib.parse import urlparse

result = urlparse(os.environ['DATABASE_URL'])
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname

def connect():
    try:
        connection = psycopg2.connect(
            database = database,
            user = username,
            password = password,
            host = hostname
        )
        cursor = connection.cursor()
        connection.autocommit = True
        return cursor

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
