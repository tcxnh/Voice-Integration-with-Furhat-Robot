from furhat_remote_api import FurhatRemoteAPI

from generate_cloned_voice import generate_cloned_voice

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# Say "Hi there!"
furhat.say(text="Hi there!")

# Play an audio file (with lipsync automatically added) 
furhat.say(url="https://furhataudios.s3.ap-southeast-2.amazonaws.com//Users/yunzhu/Desktop/OpenVoice/outputs/output_chinese.wav", lipsync=True)

# Perform a named gesture
furhat.gesture(name="BrowRaise")

# Perform a custom gesture
furhat.gesture(body={
    "frames": [
        {
            "time": [
                0.33
            ],
            "params": {
                "BLINK_LEFT": 1.0
            }
        },
        {
            "time": [
                0.67
            ],
            "params": {
                "reset": True
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    })

# Get the users detected by the robot 
users = furhat.get_users()

# Attend the user closest to the robot
furhat.attend(user="CLOSEST")

# Attend a user with a specific id
furhat.attend(userid="virtual-user-1")

# Attend a specific location (x,y,z)
furhat.attend(location="0.0,0.2,1.0")

# Set the LED lights
furhat.set_led(red=200, green=50, blue=50)

#generate_cloned_voice("resources/Wafa_sample.mp3")

# Listen to user speech and return ASR result
while(True):
    result = furhat.listen()
    print(result)