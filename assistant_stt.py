import io
import sounddevice as sd
import numpy as np
import wave 
import speech_recognition as sr

buf = io.BytesIO()
r = sr.Recognizer()

print("Говорите щось... (натисніть Ctrl+C для завершення)")

duration = 5
rate = 44100

record = sd.rec(int(5 * 44100), samplerate=44100, channels=1, dtype='float-32')
sd.wait()

record_int16 = np.int16(record * 32767)
with wave.open(buf, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(44100)
    wf.writeframes(record_int16.tobytes())

buf.seek(0)

with sr.AudioFile(buf) as audio:
    audio_data = r.record(audio)
    try:
        text = r.recognize_google(audio_data, language="ru-RU")
        print(f"Ви сказали: {text}")
    except sr.UnknownValueError:
        print("Не вдалося розпізнати мову")
    except sr.RequestError as e:
        print(f"Помилка сервісу розпізнавання мови; {e}")
