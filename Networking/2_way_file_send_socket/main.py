# Reciver
import socket

# Replace this with the server's actual local IP address (found using ipconfig or ifconfig)
HOST = '192.168.0.105'  # Example: 192.168.1.100
PORT = 65432          # Port to bind to

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    # Bind the socket to the address
    stream.bind((HOST, PORT))
    # Listen for incoming connections
    stream.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    # Accept an incoming connection
    conn, addr = stream.accept()
    with conn:
        print(f"Connected by {addr}")
        
        # Receive and send data
        data = conn.recv(1024)
        if data == b"True":
            try:
                # Recieve and save the file in chunks
                # We need to ensure we only get the filename data, not more.
                file_name_bytes = conn.recv(1024)
                file_name = "Received_" + file_name_bytes.decode('utf-8').strip('\x00')
                print(f"Preparing to receive file: {file_name}")
                
                # Recieve and save the file in chunks
                bytes_received = 0
                with open(file_name, "wb+") as f:
                    while True:
                        # **CRITICAL FIX:** conn.recv(1024) will return b'' 
                        # when the sender closes their writing side.
                        chunk = conn.recv(1024)
                        if not chunk: # End of file signal from sender (stream.shutdown(SHUT_WR))
                            break
                        f.write(chunk)
                        bytes_received += len(chunk)
                        
                
                print(f"File received and saved as {file_name}. Total bytes: {bytes_received}")
                
                # Send confirmation back to the sender
                conn.sendall(b'File received successfully')
                
            except Exception as e:
                print(f"An error occurred during receive: {e}")
                conn.sendall(f'Error receiving file: {e}'.encode('utf-8'))
        else:
             print("Sender declined to send a file or failed pre-check.")