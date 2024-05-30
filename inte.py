import wave
from amazons3 import upload_audio
from furhat_remote_api import FurhatRemoteAPI
from generate_cloned_voice import generate_cloned_voice
from record_audio import record_audio
import random
import time
import os

furhat = FurhatRemoteAPI("localhost")

# Say "Hi there!"
furhat.say(text="Hi there! I am here to show your the voice cloning function of furhat robot. Please say something to me and I will try to mimic your voice")
time.sleep(10)

greetings = [
    "Hello, it's nice to meet you!",
    "Welcome! It's a pleasure to have you here.",
    "Hey, how's it going? Great to see you!",
    "Good morning/afternoon/evening! How can I assist you today?",
    "Hi, thanks for stopping by! How may I help you?",
    "Hello and welcome! What brings you here today?",
    "Greetings and salutations! How are things with you?",
    "Hey there, nice to meet you! How's your day been so far?",
    "Well hello there! It's wonderful to make your acquaintance.",
    "Hi, I hope you're having a fantastic day! What can I do for you?",
    "Hello, thanks for reaching out! How may I be of service?",
    "Hey, great to connect with you! What's on your mind?",
    "Good day, friend! How are you feeling today?",
    "Hello, it's a joy to have you here! What's new with you?",
    "Hi there, I'm thrilled to meet you! How can I make your day better?",
]

def continuous_loop():
    concatenated_speech = []
    output_dir = "concatenated_recordings"
    os.makedirs(output_dir, exist_ok=True)

    while True:
        output_file_path = record_audio(8)
        
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