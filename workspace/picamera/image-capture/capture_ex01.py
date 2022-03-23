# 처음부터 jpg 이미지를 얻어서 네트워크로 전송할 예정임.
# 캡처한 이미지는 화면에 안보여줘도 됨.

from io import BytesIO
from time import sleep
from picamera import PiCamera



stream = BytesIO()
camera = PiCamera()

while True:
    camera.capture(stream, format='jpeg', use_video_port=True)
    # 캡쳐하고 난 후 파일의 읽기 위치는 마지막에 있다.
    
    data = stream.getvalue() # BytesIO의 전체 데이터 배열 얻기

    # data를 전송
    stream.seek(0)
    stream.truncate() # 현재 읽기 쓰기 위치에서 뒷부분을 잘라버린다(제거한다).
    
    