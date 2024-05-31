### Prototype System of Voice Integration with Furhat Robot
The system works as follows: 

The user initiates a conversation with the Furhat Robot, and their speech is recorded by the "record audio module." The user's audio sample is then passed to the "OpenVoice module," which leverages advanced voice cloning technology to generate synthetic audio that mimics the user's unique voice characteristics. This cloned, synthetic audio is uploaded to cloud storage (AWS S3) by the "upload audio module." Subsequently, the Furhat robot retrieves the synthetic audio from the cloud and plays it back to the user, creating the impression of a natural conversation using the user's own voice. As the interaction continues, the user's recorded speech is continuously concatenated (combined), and the process of recording, cloning, uploading, and playback repeats in a loop. As the interaction continues, the system can get more and more voice samples from users to enhance the quality of the generated cloned voice, further creating a more natural and personalized conversational experience for users.

### Requirements to run this program 
1.To run this program, remember to download the checkpoints from https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md <br>
2. Add the AWS key and make the bucket public to allow Furhat access 
set the bucket policy as 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::furhataudios/*"
        }
    ]
}
<br>
add your key in "amazons3.py" os.environ['AWS_ACCESS_KEY_ID'] = '', os.environ['AWS_SECRET_ACCESS_KEY'] = ''<br>
3. install all the packages in the requirements. txt<br>
4. Put the IP address into "inte.py" the line 10: FurhatRemoteAPI("YOUR_FURHAT_IP_ADDRESS")
5. The main entry is in "inte.py", just need to run this script 

### Demo Video 
It can be found under the folder demo video


<br><br><br>
If have any questions please contact jocelynzhu6@gmail.com
