import mysql.connector
from config import Config
from mylog import Log

log = Log('Mysql')

class Mysql:
    def __init__(self):
        self.config = {
            'host': Config().getConfig("database", "host"),
            'user': Config().getConfig("database", "user"),
            'password': Config().getConfig("database", "password"),
            'port': Config().getConfig("database", "port"),
            'database': 'test_xiaohei',
            'charset': 'utf8'
        }

    def select(self,sql):
        try:
            cnn = mysql.connector.connect(**self.config)
            cursor = cnn.cursor()
        except mysql.connector.Error as e:
            log.error('connect fails!{}'.format(e))

        try:
            cursor.execute(sql)
            re = cursor.fetchall()
            return re
        except mysql.connector.Error as e:
            log.error('query error!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()

    def ddl(self,sql):
        try:
            cnn = mysql.connector.connect(**self.config)
            cursor = cnn.cursor()
        except mysql.connector.Error as e:
            log.error('connect fails!{}'.format(e))

        try:
            cursor.execute(sql)
        except mysql.connector.Error as e:
            log.error('query error!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()

    def insert(self,sql,data):
        try:
            cnn = mysql.connector.connect(**self.config)
            cursor = cnn.cursor()
        except mysql.connector.Error as e:
            log.error('connect fails!{}'.format(e))

        try:
            cursor.execute(sql,data)
        except mysql.connector.Error as e:
            log.error('query error!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()



def main():
    sql = 'show tables'
    result = Mysql().select(sql)
    print(result)


if __name__ == '__main__':
    main()