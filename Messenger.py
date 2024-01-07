import socket


class Messenger:
    def __init__(self, ip: str, port: int, app) -> None:
        self.server_ip = ip
        self.server_port = port
        self.client_socket = None
        self.app = app

    def receive_message(self, conn) -> None:
        while True:
            message = conn.recv(1024).decode('utf-8')
            addr = conn.recv(1024).decode('utf-8')
            self.app.field_insert(self.app.text_field2, "Received Message from " + addr)
            self.app.field_insert(self.app.text_field1, message)

    def start(self) -> None:
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        self.app.field_insert(
            self.app.text_field2,
            "Connected to Server " + str(self.server_ip) + " on port " + str(self.server_port))

    def send_message(self, message: str) -> None:
        self.client_socket.send(message.encode('utf-8'))
        self.app.field_insert(self.app.text_field2, "Message Sent Successfully")
