import socket
import threading


class Server:

    def __init__(self, server_ip: str, server_port: int) -> None:
        self.server_ip = server_ip
        self.server_port = server_port
        self.clients = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_ip, self.server_port))
        self.server_socket.listen()

        print("Server Listening on ", server_ip, ': ', server_port, sep="")

    def start(self) -> None:
        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connection from {addr}")

#            message = "Hello from the server!"
#            conn.send(message.encode('utf-8'))
#            conn.send("Server\n".encode('utf-8'))
            self.clients[addr] = conn

            client_handler_thread = threading.Thread(target=self.__handle_client, args=(conn, addr), daemon=True)
            client_handler_thread.start()

    def __handle_client(self, conn, addr):
        while True:
            try:
                message = conn.recv(1024)
                if not message:
                    break

                print("\nMessage received from", addr)

                for client_address, client_conn in self.clients.items():
                    client_conn.send(message)
                    tmp = str(addr) + '\n'
                    client_conn.send(tmp.encode('utf-8'))
                    print("\nMessage sent to", client_address)

            except (Exception,):
                print("Client", addr, "disconnected")
                del self.clients[addr]
                break


if __name__ == "__main__":
    ip = '0.0.0.0'
    port = 12345

    server = Server(ip, port)
    server.start()
