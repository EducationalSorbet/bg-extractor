# Sender
import socket
import os

# Replace this with the server's local IP address
HOST ='192.168.0.105'
PORT = 65432

file_name = "Movie.mp4"

# Create a scoket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    # Connect to the server using the server's local IP
    print(f"Connecting to {HOST}:{PORT}...")
    stream.connect((HOST, PORT))
    print("Connected.")

    send_file = input("Want to send File(\"Yes\" or \"No\"): ").strip().lower() == "yes"
    if (send_file):
        try:
            # Check if file exists before trying to send
            if not os.path.exists(file_name):
                 print(f"Error: File '{file_name}' not found.")
                 stream.sendall(b"False") # Notify receiver we won't send
                #  return
            
            # Notify the server that we want to send a file
            stream.sendall(b"True")
            print("Sending initiation signal...")

            # Send the file name (encoded as bytes)
            stream.sendall(file_name.encode("utf-8"))
            print(f"Sending filename: {file_name}")
            
            # Open the file in binary mode and send it in chunks
            bytes_sent = 0
            with open(file_name, 'rb') as f:
                while (chunk := f.read(1024)):  # Read file in 1 KB chunks
                    # Send data to the server
                    stream.sendall(chunk)
                    bytes_sent += len(chunk)
            
            print(f"Finished sending file data. Total bytes sent: {bytes_sent}")
            
            # **CRITICAL FIX:** Signal to the receiver that we are done sending data
            # This causes the receiver's conn.recv() to return b''
            stream.shutdown(socket.SHUT_WR)
            print("Shut down write side of the connection.")

            # Receive Response from the server
            data = stream.recv(1024)
            print(f"Received from the server: {data.decode()}")
        except Exception as e:
            print(f"An error occurred during send: {e}")