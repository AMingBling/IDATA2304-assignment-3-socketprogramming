import socket

def display_status(sock):
    sock.sendall("6".encode())
    status = sock.recv(1024).decode().strip()
    print(f"\n---------- TV Status ----------\n{status}\n-------------------------------\n")

def main():
    host = "127.0.0.1"
    port = 1238
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        print(sock.recv(1024).decode())
        while True:
            display_status(sock)
            command = input("Remote>> ")
            sock.sendall(command.encode())
            response = sock.recv(1024).decode().strip()
            print(response)
            if command.lower() == "quit":
                break
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()