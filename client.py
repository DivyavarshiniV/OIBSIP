import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

print("✅ Connected to server. Type 'bye' to exit.")

while True:
    # Send message
    msg = input("You: ")
    client_socket.send(msg.encode())
    if msg.lower() == "bye":
        break

    # Receive reply
    reply = client_socket.recv(1024).decode()
    if not reply or reply.lower() == "bye":
        print("❌ Server disconnected.")
        break
    print(f"Server: {reply}")

client_socket.close()
