"""
数据库读写类
"""
import pymysql

class Database_rw:
    def __init__(self, table, host='192.168.1.67', port=3306, user='root', password='123456',
                 database='dict' ,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.table = table
        self.__link_db()
        print("初始完成")

    def __link_db(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user,
                          password=self.password, database=self.database, charset=self.charset)
        self.cur = self.db.cursor()


    def get_table_row_num(self):
        """
                :return: 返回table的数据 元组
        """
        sql = "select * from %s;" % self.table
        self.cur.execute(sql)
        row_data = self.cur.fetchall()
        return row_data


    def insert_into_table(self, table, *args):
        """
            向 table 插入数据
        :param args: 两个元组 第一个字段名   第二个要插入的数据
        :param table: 目的表名
        :return:
        """
        # 获得字段名参数
        column = '('
        for i in args[0]:
            column += i
            column += ' '
        column = column.strip()
        column += ')'

        data = str(args[1])
        sql = "insert into %s %s values %s;" % (table, column, data)
        print(sql)



if __name__ == '__main__':
    print("初始开始")
    db = Database_rw("word")
    print(db.get_table_row_num())
    db.insert_into_table('word',('word','ssdf',), ('this is data111..',))

