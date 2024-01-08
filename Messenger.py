import socket
from RSA import RSA


class Messenger:
    def __init__(self, ip: str, port: int, app, username: str) -> None:
        self.server_ip = ip
        self.server_port = port
        self.client_socket = None
        self.app = app
        self.username = username
        self.encryptor = RSA()

    def receive_message(self, conn) -> None:
        while True:
            message = conn.recv(1024).decode('utf-8')
            try:
                message = self.encryptor.decrypt(message)
                field = self.app.text_field1
            except (Exception, ):
                if 'line' in message:
                    field = self.app.text_field1
                else:
                 field = self.app.text_field2
            addr = conn.recv(1024).decode('utf-8')
            if addr != "Server":
                self.app.field_insert(self.app.text_field2, "Received Message from " + addr)
            self.app.field_insert(field, message)

    def start(self) -> None:
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        self.app.field_insert(
            self.app.text_field2,
            "Connected to Server " + str(self.server_ip) + " on port " + str(self.server_port))
        self.client_socket.send(self.username.encode('utf-8'))

    def send_message(self, message: str) -> None:
        tmp = self.encryptor.encrypt(message)
        self.client_socket.send(tmp.encode('utf-8'))
        self.app.field_insert(self.app.text_field2, "Message Sent Successfully")
