import mysql_rw
from socket import *
from multiprocessing import Process
import sys
import signal

def do_request(c,w_db):
    data = c.recv(1024)
    print(data)

# 搭建tcp网络
def main():
    # 初始word表对象,通过对象 对表进行读写
    w_db = mysql_rw.Database_rw()

    # 创建网络链接
    sock_fd = socket()
    sock_fd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  # 端口重用
    sock_fd.bind(("0.0.0.0", 8004))
    sock_fd.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 等待客户端链接
    while True:
        print("listen port 8000 ...")
        try:
            c, addr = sock_fd.accept()
            print('connect from:',addr)
        except KeyboardInterrupt:
            c.close()
            sys.exit("系统退出")
        except Exception as e:
            print("未知错误",e)
            continue

        # 没有出现异常 创建子进程处理客户端请求
        p = Process(target=do_request,args=(c,w_db))
        p.daemon = True  # 父进程退出 子进程跟到退出
        p.start()


if __name__ == '__main__':
    main()
