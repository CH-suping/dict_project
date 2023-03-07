import mysql_rw

# 初始word表对象
word_db = mysql_rw.Database_rw("word")

# 将字典写入数据库

# 判断数据库有没字典数据，没有就添加字典数据
if not len(word_db.get_table_row_num()):
    # 添加字典到数据库
    # add_dict_database()
    print("开始添加")

