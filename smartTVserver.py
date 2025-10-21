import socket
from functions import handle_command

def main():
    host = "127.0.0.1"
    port = 65432
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TV server listening on {host}:{port}")
        conn, addr = server_socket.accept()
        print(f"Connected to remote control at {addr}")
        conn.sendall(b"Welcome to the Smart TV server! Type 'help' for commands.\n")
        while True:
            command = conn.recv(1024).decode().strip()
            if not command or command.lower() == "quit":
                conn.sendall(b"Goodbye!\n")
                break
            response = handle_command(command)
            conn.sendall((response + "\n").encode())
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("TV server closed")

if __name__ == "__main__":
    main()