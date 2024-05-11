"""
To run this file, make sure the pyaudio and pydub are installed 
"""

import pyaudio
import wave

def record_audio(duration, output_filename):
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=16000,
                        input=True,
                        frames_per_buffer=1024)

    # Create a wave file
    wf = wave.open(output_filename, 'wb')
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
    return True

# Call the record_audio function to capture audio
# record_audio(duration=5, output_filename='recorded_audio.wav')

from pydub import AudioSegment

def concatenate_audios(file1, file2, output_file):
    """
    Concatenates two audio files and exports the combined audio to a new file.

    Args:
        file1 (str): Path to the first audio file.
        file2 (str): Path to the second audio file.
        output_file (str): Path to the output file for the combined audio.

    Returns:
        None
    """
    # Load the first audio file
    audio1 = AudioSegment.from_file(file1, format=file1.split(".")[-1])
    # Load the second audio file
    audio2 = AudioSegment.from_file(file2, format=file2.split(".")[-1])
    # Concatenate the two audio segments
    combined_audio = audio1 + audio2
    # Export the combined audio to the output file
    combined_audio.export(output_file, format=output_file.split(".")[-1])

    print(f"Combined audio exported to {output_file}")

# 
# Example usage
#concatenate_audios("audio1.wav", "audio2.wav", "combined_audio.wav")

