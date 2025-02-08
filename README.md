# VideoStreaming_MultipleDevices
_________________________________________________________________________________________

# TCP video streaming to RTSP server

### Using Mediamtx for hosting a RTSP or RTMP server:
Run this part only to set up server on Host machine

1. Download mediamtx (ready to use media server) from Releases: https://github.com/bluenviron/mediamtx/releases 
2. Extract mediamtx files
3. Configuration settings can be modified in mediamtx.yaml file. Change the IP address to IP of the host device or localhost (Use ipconfig or ifconfig to find IP)

In MacOS:

1. Intall homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Inside homebrew install mediamtx brew install mediamtx
3. Run mediamtx.yml /opt/homebrew/opt/mediamtx/bin/mediamtx /opt/homebrew/etc/mediamtx/mediamtx.yml

_______________________________________________________________________________________

### To live stream and access videos:
This is run on the client side. Such as edge devices, drones, laptops, etc.

In Windows:

1. Install ffmpeg. Eg: winget install ffmpeg
2. To list connected devices, use ffmpeg -list_devices true -f dshow -i dummy. Note the camera name, eg: "Integrated Camera"
3. Run the exe file of mediamtx
4. In another terminal, run ffmpeg -f dshow -i video="<NAME_OF_CAMERA>" -c:v libx264 -preset ultrafast -b:v 2000k -f rtsp rtsp://<IP_ADDRESS>:8554/camera1/pass1


In Linux:

1. Install ffmpeg. sudo apt install ffmpeg
2. If required, install v4l-utils. sudo apt-get install v4l-utils
3. List connected camera using v4l2-ctl --list-devices in terminal. Note the name of device eg: /dev/video0
4. In a terminal, run ./mediamtx 
5. In another terminal, run ffmpeg -f v4l2 -i /dev/video0 -preset ultrafast -b:v 2000k -f rtsp rtsp://<IP_ADDRESS>:8554/camera1/pass1

In MacOS:
1. Install ffmpeg brew install ffmpeg
2. Run ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -pixel_format uyvy422 -i "default" -preset ultrafast -b:v 2000k -f rtsp rtsp://127.0.0.1:8554/camera1/pass1

_______________________________________________________________________________________

### Next steps:
This can be done from any device in the network

1. To run multiple streams, change as required eg: rtsp://<IP_ADDRESS>:8554/camera2/pass2 and so on.
2. To access live video stream on VLC media player: Go to Media > Open Network Stream. Enter URL as rtsp://<IP_ADDRESS>:8554/camera1/pass1. Video should start playing after a few seconds.
3. To save the video in mp4 format, run ffmpeg -i rtsp://<IP_ADDRESS>:8554/camera1/pass1 -c copy output1.mp4 on the host
4. To save the stream in separate jpg images, create a folder and run ffmpeg -i rtsp://<IP_ADDRESS>:8554/camera1/pass1 -vf "fps=1" output_%03d.jpg

In MacOS:
1. Open vlc —>file —>open network—>copy address :rtsp://127.0.0.1:8554/camera1/pass1

__________________________________________________________________________________________

### Live Streaming from DJI Drones:

1. Connect phone to RC. Open DJI app, such as DJI GO4. Check which app is compatible with the model of drone in https://www.dji.com/nl/downloads/djiapp. 
2. Running mediamtx starts RTMP server in the host.
3. In the DJI app, go to Options (usually top right button) > Live Streaming Option > RTMP. Enter RTMP address as rtmp://<IP_ADDRESS>/dji/pass
4. When the drone starts streaming, the live stream icon appears on top left and turns blue to show time elapsed. Can click and see stream parameters like fps. 

________________________________________________________________________________________

# Socket programming for transferring rosbag files and ros-topics
This is to transfer rosbag files or rostopics from server to client. This can be used even if client does not have ROS installed.

1. Run the rosbag_server.py or rostopics_server.py on the server side
2. Run the rosbag_client.py or rostopics_client.py on the client side


