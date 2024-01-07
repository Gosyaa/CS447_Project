import tkinter as tk
import socket
import threading


class Messager:

    def __init__(self, ip, port):
        self.server_ip = ip
        self.server_port = port

    def reciever(self, conn):
        while True:
            message = conn.recv(1024).decode('utf-8')
            addr = conn.recv(1024).decode('utf-8')
            field_insert(text_field2, "Recieved Message from " + addr)
            field_insert(text_field1, message)

    def start(self):

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, self.server_port))
        field_insert(text_field2, "Connected to server" + str(self.server_ip) + "on port" + str(self.server_port))

    def sender(self, message):
        self.client_socket.send(message.encode('utf-8'))
        field_insert(text_field2, "Message Sent Succecfully")

def on_button_click():
    s = entry.get()
    if s != "":
        new_messager.sender(s)
        entry.delete(0, tk.END)

def field_insert(field, s):
    field.config(state=tk.NORMAL)
    s += '\n'
    field.insert(tk.INSERT, s)
    field.config(state=tk.DISABLED)


root = tk.Tk()
root.title("GUI App")

canvas1 = tk.Canvas(root, height=int(root.winfo_screenheight() * 0.45))
canvas1.pack(fill=tk.BOTH, expand=True, padx=5)

tk.Label(canvas1, text='Messages', font=('Arial', 12, 'bold')).pack(side=tk.TOP, fill=tk.X)
text_field1 = tk.Text(canvas1, wrap=tk.WORD, height=1, width=0, state=tk.DISABLED)
scrollbar1 = tk.Scrollbar(canvas1, command=text_field1.yview)
text_field1.config(yscrollcommand=scrollbar1.set)

text_field1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

canvas2 = tk.Canvas(root, height=int(root.winfo_screenheight() * 0.45))
canvas2.pack(fill=tk.BOTH, expand=True, padx=5)

tk.Label(canvas2, text='Service Information', font=('Arial', 12, 'bold')).pack(side=tk.TOP, fill=tk.X)
text_field2 = tk.Text(canvas2, wrap=tk.WORD, height=1, width=0, state=tk.DISABLED)
scrollbar2 = tk.Scrollbar(canvas2, command=text_field2.yview)
text_field2.config(yscrollcommand=scrollbar2.set)

text_field2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

canvas3 = tk.Canvas(root, height=int(root.winfo_screenheight() * 0.1), bg='blue')
canvas3.pack(fill=tk.X, pady=15, padx=5)

entry = tk.Entry(canvas3)
button = tk.Button(canvas3, text="Submit", command=on_button_click)

entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
button.pack(side=tk.RIGHT, fill=tk.BOTH)

field_insert(text_field2, 'test')
new_messager = Messager('13.51.167.39', 12345)
new_messager.start()
reciever_thread = threading.Thread(target=new_messager.reciever, args=(new_messager.client_socket, ))
reciever_thread.setDaemon(True)
reciever_thread.start()

root.mainloop()
