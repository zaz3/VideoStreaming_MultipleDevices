import socket

def send_file(server_ip, server_port, file_path):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    server_address = (server_ip, server_port)
    print(f"Connecting to server at {server_ip}:{server_port}")
    client_socket.connect(server_address)
    
    try:
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.sendall(data)
        print(f"File {file_path} sent successfully.")
    finally:
        client_socket.close()

# Replace with the laptop's IP and desired port
server_ip = '127.0.0.1'
server_port = 65432
file_path = 'MH_01_easy.bag'
send_file(server_ip, server_port, file_path)

