# PyAudio로 Recording하기

import pyaudio
import wave

SAMPLE_RATE = 44100  # 음성데이터 샘플링 레이트 : 44100hz
FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024
RECORD_SECONDS = 5  #녹음하는 시간

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,    
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=CHUNK)

print('start recording')  #시작신호

frames = []

for i in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):  #10초동안 녹음한 음서을 frame 에 추가함
    data = stream.read(CHUNK)
    frames.append(data)

print('stop recording')

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open('output.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)
wf.writeframes(b''.join(frames))    #frame 에 관계된 데이터를 출력함
wf.close()