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
import os

greetings = [
    "Hi there!",
    "Hello, how are you?",
    "Greetings!",
    "Hey there, friend!",
    "Good day to you!",
    "Hello, it's nice to meet you!",
    # Add more greetings as desired
]

import random
import time
import wave
import os
import tempfile

greetings = [
    "Hi there!",
    "Hello, how are you?",
    "Greetings!",
    "Hey there, friend!",
    "Good day to you!",
    "Hello, it's nice to meet you!",
    # Add more greetings as desired
]

import random
import time
import wave
import os

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
    concatenated_speech = []
    output_dir = "concatenated_recordings"
    os.makedirs(output_dir, exist_ok=True)

    while True:
        output_file_path = record_audio(10)
        
        if output_file_path:
            with open(output_file_path, 'rb') as audio_file:
                user_speech = audio_file.read()
            concatenated_speech.append(user_speech)

            # Choose a random greeting from the list
            input_text = random.choice(greetings)

            try:
                # Create a new wave file for the concatenated audio
                concatenated_file_path = os.path.join(output_dir, f"concatenated_{len(concatenated_speech)}.wav")
                with wave.open(concatenated_file_path, 'wb') as concatenated_wave:
                    concatenated_wave.setnchannels(1)
                    concatenated_wave.setsampwidth(2)  # Assuming 16-bit audio
                    concatenated_wave.setframerate(16000)
                    concatenated_wave.writeframes(b''.join(concatenated_speech))

                # Call the generate_cloned_voice function with the concatenated file path
                generate_cloned_voice(concatenated_file_path, input_text)
                s3url = upload_audio("outputs/output_en_default.wav")

                # Get the length of the audio file
                with wave.open("outputs/output_en_default.wav", "r") as wav:
                    audio_length = wav.getnframes() / wav.getframerate()

                furhat.say(url=s3url)

                # Wait for the audio to finish playing
                time.sleep(audio_length + 2)  # Sleep for the audio length plus an extra second
                print(audio_length)
            
            except Exception as e:
                print(f"Error occurred: {e}")
                furhat.say(text="I'm sorry, I couldn't process the audio. Please try again.")
                time.sleep(3)

            finally:
                os.remove(output_file_path)  # Remove the temporary audio file
        else:
            furhat.say(text="I didn't catch that. Please try again.")
            time.sleep(2)

continuous_loop()