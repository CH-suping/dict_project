"""
数据库读写类
"""
import pymysql

class Database_rw:
    def __init__(self, host='192.168.1.67', port=3306, user='root', password='123456',
                 database='dict' ,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        # self.table = table
        self.__link_db()
        print("初始完成")

    def __link_db(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user,
                          password=self.password, database=self.database, charset=self.charset)

    # 创建游标函数
    def create_cur(self):
        self.cur =self.db.cursor()

    # 关闭游标和数据库函数
    def close(self):
        self.cur.close()
        self.db.close()


    def select_column(self, table):
        """
                :return: 返回table的数据 元组
        """
        # sql = "select 字段名1,字段名2 from 表名 where 条件;"
        sql = "select * from %s;" % table
        self.cur.execute(sql)
        row_data = self.cur.fetchall()
        return row_data


    def insert_into_table(self, *args, table):
        """
            向 table 插入数据
        :param args: 两个元组 第一个字段名   第二个要插入的数据 传入的字符串为单引号
        :param table: 目的表名  字符串格式
        :return:
        """
        # 获得字段名参数

        column = str(args[0]).replace("'",'')   # 获得要添加的字段名 转化为字符串 并去掉引号

        data = str(args[1])   # 获得要添加的数据  转为字符串
        # 获得sql语句
        sql = "insert into %s %s values %s;" % (table, column, data)
        # print(sql)
        try:
            # 游标方法
            self.cur.execute(sql)
            # 提交数据库
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            print("写入数据库错误", e)





if __name__ == '__main__':
    pass
    db = Database_rw()

    db.insert_into_table(('word','mean'), ('this','this is mean'), table='word')

