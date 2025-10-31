import socket
import sys
import threading
from smartTV import SmartTV
from functions import handle_command

class TVServer:
    def __init__(self, host="127.0.0.1", port=1238):
        self.host = host
        self.port = port
        self.tv = SmartTV()
        self.clients = {}  # Store connected clients {client_id: (conn, addr)}
        self.client_id_counter = 1
        self.lock = threading.Lock()  # Ensure thread-safe operations

    def broadcast(self, message, exclude_client=None):
        """Send a message to all connected clients except the excluded one."""
        with self.lock:
            for client_id, (conn, _) in self.clients.items():
                if client_id != exclude_client:
                    try:
                        conn.sendall(f"[BROADCAST] {message}\n".encode())
                    except Exception:
                        print(f"Failed to send message to Remote {client_id}")

    def handle_client(self, conn, addr, client_id):
        """Handle communication with a single client."""
        print(f"Remote control {client_id} connected from {addr}")
        conn.sendall(f"Welcome, Remote Control {client_id}! Type '7' for available commands.\n".encode())
        try:
            while True:
                command = conn.recv(1024).decode().strip()
                if not command or command.lower() == "quit":
                    conn.sendall(b"Goodbye!\n")
                    break
                response = handle_command(command)
                conn.sendall((response + "\n").encode())
                # Broadcast the change to other clients
                self.broadcast(f"Remote {client_id} made a change: {response}", exclude_client=client_id)
        except Exception as e:
            print(f"Error with Remote Control {client_id}: {e}")
        finally:
            with self.lock:
                del self.clients[client_id]
            conn.close()
            print(f"Remote control {client_id} disconnected")

    def start(self):
        """Start the TV server."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"TV server listening on {self.host}:{self.port}")
            while True:
                conn, addr = server_socket.accept()
                with self.lock:
                    client_id = self.client_id_counter
                    self.clients[client_id] = (conn, addr)
                    self.client_id_counter += 1
                threading.Thread(target=self.handle_client, args=(conn, addr, client_id), daemon=True).start()
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            server_socket.close()
            print("TV server closed")

if __name__ == "__main__":
    server = TVServer()
    server.start()