import pyaudio
import wave
from amazons3 import upload_audio
from furhat_remote_api import FurhatRemoteAPI
from generate_cloned_voice import generate_cloned_voice
from record_audio import record_audio

#### Not working, input overflow 

furhat = FurhatRemoteAPI("localhost")

CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
SILENCE_THRESHOLD = 500  # Adjust this value as needed
SILENCE_DURATION = 1  # Adjust this value as needed (in seconds)

"""
def record_user_speech(output_filename):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    silence_frames = 0

    furhat.say(text="I'm listening. Please speak.")
    speech_result = furhat.listen()

    while speech_result.message or silence_frames < SILENCE_DURATION * RATE // CHUNK:
        data = stream.read(CHUNK)
        frames.append(data)

        if max(data) < SILENCE_THRESHOLD:
            silence_frames += 1
        else:
            silence_frames = 0

        if speech_result.message:
            speech_result = furhat.listen()

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return b''.join(frames)
"""

while True:
    user_speech = record_audio(30,"recorded_audio.wav")
    if user_speech:
        generate_cloned_voice
        ("recorded_audio.wav", "I love u, can you hang out with me tomorrow")
        s3url = upload_audio("outputs/output_chinese.wav")
        furhat.say(url=s3url)
    else:
        furhat.say(text="I didn't catch that. Please try again.")