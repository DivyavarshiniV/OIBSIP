import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# ---------- Networking ----------
HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, f"Server: {msg}\n")
            chat_window.config(state=tk.DISABLED)
        except:
            break

def send_message():
    msg = entry_message.get()
    if msg:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {msg}\n")
        chat_window.config(state=tk.DISABLED)
        client_socket.send(msg.encode())
        entry_message.delete(0, tk.END)
        if msg.lower() == "bye":
            client_socket.close()
            root.quit()

# ---------- GUI ----------
root = tk.Tk()
root.title("Python Chat App")
root.geometry("400x450")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_message = tk.Entry(root, width=40)
entry_message.pack(side=tk.LEFT, padx=10, pady=5, expand=True)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=5)

try:
    client_socket.connect((HOST, PORT))
    threading.Thread(target=receive_messages, daemon=True).start()
except Exception as e:
    messagebox.showerror("Connection Error", str(e))
    root.destroy()

root.mainloop()
