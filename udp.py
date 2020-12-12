from socket import *

s = socket(AF_INET, SOCK_DGRAM)

def checkUdp(ip, port):
  s.bind((ip, port))
  data, addr = s.recvfrom(1024)
  print('Recevie from {}:{} :{}'.format(addr[0], addr[1], data.decode('utf-8')))
  #sendto的另一个参数为客户端socket地址
  s.sendto('信息已成功收到!'.encode('utf-8'), addr)

def sendUdp(md5, ip, port):
  s.sendto(md5.encode('utf-8'), (ip, port))
  res = s.recv(1024).decode('utf-8')
  print(res)