import socket

def receive_file(server_ip, server_port, output_file):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = (server_ip, server_port)
    print(f"Starting server on {server_ip}:{server_port}")
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    while True:
        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Connection from {client_address}")
            with open(output_file, 'wb') as f:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"File received and saved as {output_file}")
            break
        finally:
            connection.close()

# Replace with your laptop's IP and desired port
server_ip = '127.0.0.1'
server_port = 65432
output_file = 'received_rosbag.bag'
receive_file(server_ip, server_port, output_file)

