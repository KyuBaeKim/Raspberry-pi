import spidev
import time
# 딜레이 시간(센서 측정 간격)
delay = 0.5

# #MCP3008 채널 중 센서에 연결한 채널 설정
pot_channel = 0 # 조도 센서

# SPI 인스턴스 spi 생성
spi = spidev.SpiDev()

# SPI 통신 시작하기
spi.open(0, 0)

# SPI 통신 속도 설정
spi.max_speed_hz = 100000

# 0~7 까지 8개의 채널에서 SPI 데이터 읽기
def readabc(abcnum):
    if abcnum < 0 or abcnum > 7:
        return -1

    r = spi.xfer2([1, 8+abcnum <<4, 0]) # 요청 및 값 리턴
    data = ((r[1] & 3) << 8) + r[2] # 10비트 해석

    return data

while True:
    # readabc 함수로 pot_channel의 SPI 데이터를 읽기
    pot_value = readabc(pot_channel)
    print("---------------------------")
    print("LDR Value: %d" %pot_value)
    time.sleep(delay)