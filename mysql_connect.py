import mysql.connector
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'port': 3306,
    'database': 'testdb',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    sql_query = 'select * from user ;'
    cursor.execute(sql_query)
    for i in cursor:
        print (i)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()

