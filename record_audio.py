"""
To run this file, make sure the pyaudio and pydub are installed 
"""

import os
import pyaudio
import wave
import uuid

def record_audio(duration):
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=16000,
                        input=True,
                        frames_per_buffer=1024)

    # Generate a unique output file name
    output_filename = f"{uuid.uuid4().hex}.wav"
    output_file_path = os.path.join("recordings", output_filename)

    # Create a wave file
    wf = wave.open(output_file_path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)

    # Start recording
    frames = []
    for i in range(int(16000 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # Stop the stream and close PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Write the audio data to the wave file
    wf.writeframes(b''.join(frames))
    wf.close()

    return output_file_path

