import socket
from threading import Thread
import os



def run_server(addr, thread_fn):
        # 주소 체계(address family) : IPv4, 소켓 타입 : TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 이미 열린 포트 출돌시 재사용 옵션 설정
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((addr))
    server_socket.listen()


    while True: # 서버를 계속 구동하기 위해서

        #accept 함수에서 대기, 클라이언트 접속 시 새로운 소켓을 리턴
        client_socket, addr = server_socket.accept()
        
        # 새로운 스레드로 threaded 실행
        t = Thread(target = thread_fn, args=(client_socket, addr))

        t.start()
    server_socket.close()

def file_read(file_path):
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data :
                break
            yield data
                
def send_file(addr, file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(addr)
            fileSize = os.path.getsize(file_path) # 파일의 size 크기를 int 사이즈로 받는다.

            # 파일명, 파일 크기 전송
            file_name = file_path.split('/')[-1]
            print("전송 파일 크기", fileSize)
            s.sendall(f'{file_name}/{fileSize}'.encode())

            # 준비 상태 수신
            isready = s.recv(1024).decode()
            if isready == "ready":
                # 파일 전송
                for data in file_read(file_path):
                    s.sendall(data)
                print("전송완료")
        except Exception as e:
            print(e)
    

BASE = "/Users/qbae/temp/received/"
    
def receive_file(client_socket, addr):
    try:
        ## 파일명, 파일 크기 수신
        data = client_socket.recv(1024)
        file_name, size = data.decode().split('/')
        size = int(size)
        print('file name', file_name)
        print('수신할 파일 크기:', size)
        
        # 준비상태 전송
        client_socket.send("ready".encode())
        
        # 파일 수신
        total_size = 0
        file_path = BASE + file_name
        with open(file_path, "wb") as f:
            while True:
                data = client_socket.recv(1024)
                f.write(data)
                total_size += len(data)
                if total_size >= size: break
                
            print(f"수신 환료: {total_size} bytes")
    except Exception as e:
        print(e)
    finally:
        client_socket.close()