import os
import socket

HOST = '172.30.1.57'
PORT = 1234
FILE_PATH = "/home/pi/workspace/Opencv/data/vtest.avi"

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data :
                break
            yield data



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        fileSize = os.path.getsize(FILE_PATH) # 파일의 size 크기를 int 사이즈로 받는다.

        # 파일 크기 전송
        print("전송 파일 크기", fileSize)
        s.sendall(str(fileSize).encode())

        # 준비 상태 수신
        isready = s.recv(1024).decode()
        if isready == "ready":
            # 파일 전송
            for data in file_read(FILE_PATH):
                s.sendall(data)
            print("전송완료")
    except Exception as e:
        print(e)