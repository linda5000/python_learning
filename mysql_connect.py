import mysql.connector
# import pymysql

config = {
    'host': '39.108.136.60',
    'user': 'student2',
    'password': 'student2@',
    'port': 3306,
    'database': 'test_xiaohei',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
    cursor = cnn.cursor()
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))


try:
    sql_query = 'update student set update_date = now() '

    data = [("xiaotao", "boy"),
            ("hudiefeifei", "girl"),
            ("huixie", "boy"),
            ("yongheng", "boy")]

    cursor.execute(sql_query)
    # cursor.executemany(sql_query,data)
    # re = cursor.fetchall()
    # print(re)

except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()

