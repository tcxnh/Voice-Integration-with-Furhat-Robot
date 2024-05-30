To run this program, remember to download the checkpoints from https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md

add AWS key add make the bucket public to allow furhat access 
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
