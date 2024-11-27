import mysql.connector
from ..constants.common import DB_HOST, DB_PASS


def create_db_if_not_exists():
    mysqldb = mysql.connector.connect(
        host=DB_HOST, user="root", passwd=DB_PASS
    )
    mysql_cursor = mysqldb.cursor()
    query = "CREATE DATABASE IF NOT EXISTS users_db"
    mysql_cursor.execute(query)
    mysql_cursor.execute("SHOW DATABASES")

    for eachdb in mysql_cursor:
        print(eachdb)
