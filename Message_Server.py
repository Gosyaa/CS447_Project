import socket
import threading

clients = {}


def client_handler(conn, addr):
    while True:
        try:
            message = conn.recv(1024)
            print("\nMessage recieved from", addr)
            for client_address in clients.keys():
                clients[client_address].send(message)
                clients[client_address].send(str(addr).encode('utf-8'))
                print("\nMessage send to", client_address)
        except Exception as e:
            print("Client", addr, "disconected")
            del clients[client_address]
            break


server_ip = '0.0.0.0'
server_port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_ip, server_port))
s.listen()

print("Server listening on ", server_ip, ':', server_port, sep='')

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    message = "Hello from the server!"
    conn.send(message.encode('utf-8'))
    conn.send("Server".encode('utf-8'))
    clients[addr] = conn
    client_handler_thread = threading.Thread(target=client_handler, args=(conn, addr))
    client_handler_thread.start()
