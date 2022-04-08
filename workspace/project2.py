import sounddevice as sd
import soundfile as sf


# GPIO-ZERO
from gpiozero import Button, LED, AngularServo

# wheather API
import requests as req
import json
from pydub import AudioSegment
from pydub.playback import play
import io 
from os import sys 


from time import sleep
from signal import pause
import requests



# Button
button = Button(26, bounce_time= 0.05)

# Servo
servo = AngularServo( 14, min_angle = -90, max_angle = 90, min_pulse_width = 0.0004, max_pulse_width=0.0024)

# LED
led = LED(20)

# wheather api key
city = 'Seoul'
API_KEY = '93ec9acd67f5e6d7fd08ff43c857eeac'
URL_W = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&lang=kr'

# sound synthesis
URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"  # 음성 합성일때 synthesize
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK f8f69a8e0b29fc826bfe20c5bb36a55d" 
}


# sound device는 지원됨
fs = 16000 # Sample rate 
seconds = 3 # Duration of recording

# 버튼 인식을 위한 상수
count = 0

# wheather 정보 얻기
def get_weather(city='Seoul'):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&lang=kr' 
    print(URL)
    weather = {}
    res = req.get(URL)
    if res.status_code == 200:
        result = res.json()
        weather['main'] = result['weather'][0]['main'] 
        weather['description'] = result['weather'][0]['description'] 
        icon = result['weather'][0]['icon'] 
        weather['icon'] = f'http://openweathermap.org/img/w/{icon}.png' 
        weather['etc'] = result['main']
    else:
        print('error', res.status_code)
    return weather
weather = get_weather()
how_weather = weather['description']
temp = weather['etc']['temp']
humidity = weather['etc']['humidity']




while True:
    if button.is_pressed:
        print("Button is pressed")
        myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
        sd.wait() # wait until recording is finished
        sf.write('output.wav', myrecording, fs) # save as WAV file

        count = 1
    elif(count == 1):
        kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize" # 음성 인식 recognize

        rest_api_key = 'f8f69a8e0b29fc826bfe20c5bb36a55d'

        headers = {
            "Content-Type": "application/octet-stream",
            "X-DSS-Service": "DICTATION",
            "Authorization": "KakaoAK "+ rest_api_key,
        }

        with open('output.wav', 'rb') as fp:
            audio = fp.read()

        res = requests.post(kakao_speech_url, headers=headers, data=audio)

        is_success = True

        start = res.text.find('{"type":"finalResult"')
        end = res.text.rindex('}') +1

        if start == -1: # 인식 실패
            start = res.text.find('{"type":"errorCalled"')
            is_success = False

        result_json_string = res.text[start:end]
        result = json.loads(result_json_string)

        if is_success :
            print('인식 결과:', result['value'])
            if((result['value']=="문 열어")|(result['value']=="문 여러")|(result['value']=="문 열러")|(result['value']=="문 열어라")):
                servo.angle = -90

            elif((result['value']=="문 닫아")|(result['value']=="문 다다")|(result['value']=="문 다다라")|(result['value']=="문 닫아라")):
                servo.angle = 90
            elif((result['value']=="전등 켜")|(result['value']=="전등 커")|(result['value']=="전등 켜라")|(result['value']=="전등 켤아")):
                led.on()
            elif((result['value']=="전등 꺼")|(result['value']=="전등 끄")|(result['value']=="전등 껄아")|(result['value']=="전등 꺼라")):
                led.off()
            elif((result['value']=="날씨 알려줘")|(result['value']=="날씨 알려 줘")|(result['value']=="서울 날씨 알려줘")|(result['value']=="날씨")):
                DATA = f""" 
                <speak>
                날씨는 {how_weather} 입니다.
                그리고 온도는 {temp-273.15:.1f}도 이고 습도는 {humidity} 입니다.
                </speak>
                """
                res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8')) 
                if res.status_code != 200:
                    print(res)
                    print(res.text)
                    sys.exit(0)

                sound = io.BytesIO(res.content)
                song = AudioSegment.from_mp3(sound)

                play(song)
            elif((result['value']=="재희 뭐하고 있어")):
                DATA = f""" 
                <speak>
                정재희님은 빵집에서 아르바이트 중입니다.
                </speak>
                """
                res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8')) 
                if res.status_code != 200:
                    print(res)
                    print(res.text)
                    sys.exit(0)

                sound = io.BytesIO(res.content)
                song = AudioSegment.from_mp3(sound)

                play(song)
            else:
                DATA = f""" 
                <speak>
                포함되어 있지 않은 기능 입니다. 다시 말씀 해주세요
                </speak>
                """
                res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8')) 
                if res.status_code != 200:
                    print(res)
                    print(res.text)
                    sys.exit(0)

                sound = io.BytesIO(res.content)
                song = AudioSegment.from_mp3(sound)

                play(song)

                
        else:
            print('인식 실패:', result['value'])
        count = 0

        

