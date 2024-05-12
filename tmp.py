import pyaudio
import wave
from amazons3 import upload_audio
from furhat_remote_api import FurhatRemoteAPI
from generate_cloned_voice import generate_cloned_voice
from record_audio import record_audio

furhat = FurhatRemoteAPI("localhost")

# 目前的问题就是把furhat说的也录进去了, 而且一定要say something要不然出bug

import random
import time
import wave

greetings = [
    "Hi there!",
    "Hello, how are you?",
    "Greetings!",
    "Hey there, friend!",
    "Good day to you!",
    "Hello, it's nice to meet you!",
    # Add more greetings as desired
]

def continuous_loop():
    while True:
        user_speech = record_audio(10)

        if user_speech:
            # Choose a random greeting from the list
            input_text = random.choice(greetings)
            generate_cloned_voice(user_speech, input_text)

            s3url = upload_audio("outputs/output_en_default.wav")

            # Get the length of the audio file
            with wave.open("outputs/output_en_default.wav", "r") as wav:
                audio_length = wav.getnframes() / wav.getframerate()

            furhat.say(url=s3url)

            # Wait for the audio to finish playing
            time.sleep(audio_length + 1)  # Sleep for the audio length plus an extra second
        else:
            furhat.say(text="I didn't catch that. Please try again.")
            time.sleep(2)  # Adjust the sleep duration as needed

continuous_loop()