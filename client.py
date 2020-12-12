from socket import *
import struct
import json
import os

# 用户的文件夹路径
FILEPATH = os.getcwd() + "/share/"

# 创建客户端
client = socket(AF_INET, SOCK_STREAM)

def connect(ip_port):
    print("connecting...")
    # ip_port = ('192.168.89.129', 22000)
    client.connect(ip_port)
    print('connet success')

def sendFile(filePath):
    buffSize = 1024
    client.send(bytes('1', "utf-8"))
    fileName = filePath.split('\\')[-1]
    # 得到文件的大小
    filesize_bytes = os.path.getsize(filePath)
    # 创建字典用于报头
    dirc = {"fileName": fileName, "fileSize": filesize_bytes}
    # 将字典转为JSON字符，再将字符串的长度打包
    head_infor = json.dumps(dirc)
    head_infor_len = struct.pack('i', len(head_infor))
    # 先发送报头长度，然后发送报头内容
    client.send(head_infor_len)
    client.send(head_infor.encode("utf-8"))
    # 发送真实文件
    print(fileName)
    with open(filePath, 'rb') as f:
        data = f.read()
        client.sendall(data)
        f.close()
    # 服务器若接受完文件会发送信号，客户端接收
    completed = client.recv(buffSize).decode("utf-8")
    if completed == "1":
        print("上传成功")
