import mysql.connector
from config import Config


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

    def insert(self,data):
        try:
            cnn = mysql.connector.connect(**self.config)
            cursor = cnn.cursor()
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))

        try:
            sql_query = 'insert into httptest_record(case_no,run_result,run_date) VALUES (%s,%s,now())'
            cursor.execute(sql_query,data)
            # re = cursor.fetchall()
            # print(re)

        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()



def main():
    data = (1,'/futureloan/mvc/api/member/recharge','pass')
    Mysql().insert(data)


if __name__ == '__main__':
    main()