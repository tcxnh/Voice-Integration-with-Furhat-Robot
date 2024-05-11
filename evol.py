from amazons3 import upload_audio
from furhat_remote_api import FurhatRemoteAPI

from generate_cloned_voice import generate_cloned_voice
from record_audio import record_audio

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')
# Get the users detected by the robot 
users = furhat.get_users()

# Attend the user closest to the robot
furhat.attend(user="CLOSEST")

# Attend a user with a specific id
furhat.attend(userid="virtual-user-1")

# Say "Hi there!"
furhat.say(text="Hi there! I am here to show your the voice cloning function of furhat robot. Please say something to me and I will try to mimic your voice")

# Listen for speech
answer = furhat.listen()

if answer.message != "":
    furhat.say(text="I think you said, " + answer.message, blocking=True)
else:
    furhat.say(text="I don't think you said anything", blocking=True)

record_audio(duration=60, output_filename='recorded_audio.wav')
generate_cloned_voice("recorded_audio.wav", "I love u, can you hang out with me tomorrow")

#每次url必须不同， 虽然s3 bucket里更新了， 但是不知道为什么furhat还是只看老版本
s3url = upload_audio("outputs/output_chinese.wav")

# Play an audio file (with lipsync automatically added) 
furhat.say(url=s3url)

# Listen to user speech and return ASR result
#while(True):
    #result = furhat.listen()
    #print(result)
