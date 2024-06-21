import socket

def receive_data(sock):
    data = sock.recv(1024).decode('utf-8')
    return data

# Replace with your laptop's IP and desired port
server_ip = '127.0.0.1'
server_port = 65432

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Starting server on {server_ip}:{server_port}")
connection, client_address = server_socket.accept()

try:
    print(f"Connection from {client_address}")

    # Open files to save the incoming data
    imu_file = open('imu_data.txt', 'w')
    leica_file = open('leica_position_data.txt', 'w')

    while True:
        data = receive_data(connection)
        if not data:
            break

        if data.startswith("imu"):
            imu_file.write(data[len("imu|"):])
        elif data.startswith("leica"):
            leica_file.write(data[len("leica|"):])

finally:
    connection.close()
    imu_file.close()
    leica_file.close()
