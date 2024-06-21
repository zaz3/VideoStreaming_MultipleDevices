import rospy
import socket
from sensor_msgs.msg import Imu
from geometry_msgs.msg import PointStamped
import time

def send_data(sock, data):
    sock.sendall(data.encode('utf-8'))

def imu_callback(data):
    imu_data = f"imu|{data.header.stamp}, {data.orientation.x}, {data.orientation.y}, {data.orientation.z}, {data.angular_velocity.x}, {data.angular_velocity.y}, {data.angular_velocity.z}, {data.linear_acceleration.x}, {data.linear_acceleration.y}, {data.linear_acceleration.z}\n"
    send_data(sock, imu_data)
    time.sleep(0.001)

def leica_position_callback(data):
    leica_data = f"leica|{data.header.stamp}, {data.point.x}, {data.point.y}, {data.point.z}\n"
    send_data(sock, leica_data)
    time.sleep(0.001)

# Replace with the laptop's IP and desired port
server_ip = '127.0.0.1'
server_port = 65432

# Initialize the ROS node
rospy.init_node('drone_publisher', anonymous=True)

# Create a socket connection to the laptop
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

# Subscribe to the ROS topics
rospy.Subscriber("/imu0", Imu, imu_callback)
rospy.Subscriber("/leica/position", PointStamped, leica_position_callback)

# Spin the node
rospy.spin()

# Close the socket
sock.close()

