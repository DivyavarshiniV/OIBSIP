import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))  # Host and Port
server_socket.listen(1)

print("✅ Server started. Waiting for connection...")
conn, addr = server_socket.accept()
print(f"🔗 Connected with {addr}")

while True:
    # Receive message from client
    msg = conn.recv(1024).decode()
    if not msg or msg.lower() == "bye":
        print("❌ Client disconnected.")
        break
    print(f"Client: {msg}")

    # Send reply
    reply = input("You: ")
    conn.send(reply.encode())
    if reply.lower() == "bye":
        break

conn.close()
server_socket.close()
