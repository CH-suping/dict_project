from socket import *


# 搭建tcp网路
def create_tcp(addr):
    sock_fd = socket()
    try:
        sock_fd.connect(addr)
        return sock_fd
    except Exception:
        return False


# 主界面
def main_interface():
    print('='*60)
    print("~~~~~~ l >> 登 录~~~~~~ r >> 注 册~~~~~~ q >> 退 出~~~~~~")
    print('=' * 60)


# 注册函数
def regedit_fun(sock_fd):
    user = input('user：')
    password = input('password：')

    send_data = 'r ' + user + ' ' + password
    # 向服务器发送 注册数据
    sock_fd.send(send_data.encode())

    # 等待服务器返回信息


    # sock_fd.close()


if __name__ == '__main__':
    addr = ('192.168.1.67', 8004)  # 要连接的服务器地址 端口
    sock_fd = create_tcp(addr)     # 连接服务器 得到套接字
    if sock_fd:
        while True:
            main_interface()  # 显示主界面
            choose_function = input('选择：')

            if choose_function == 'l':
                # 登录函数
                pass

            elif choose_function == 'r':
                # 注册函数
                regedit_fun(sock_fd)

            elif choose_function == 'q':
                break

            else:
                print("input error replace input~")



    else:
        print('connection fail...please check the network..')
