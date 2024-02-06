import json
from socket import socket

m = '{"id": 2, "name": "abc"}' # a real dict.
data = m.encode()

content_type = "application/json"
content_length = len(data)
host = str('192.168.100.8') + ":" + str(3000)

headers = ("POST / HTTP/1.1\r\nContent-Type: {}\r\nContent-Length: {}\r\nHost: {}/envio\r\nConnection: close\r\n\r\n").format(
    content_type, content_length, host).encode()
# print(headers)

payload = headers + data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.100.8', 3000))

sock.sendall(payload)
print("######################################\n######################################")
response = sock.recv(4096)
sock.close()
print(response.decode())
