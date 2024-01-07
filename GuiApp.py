import tkinter as tk
import threading


class GuiApp:
    def __init__(self, root: tk.Tk, username: str) -> None:
        self.root = root
        self.root.title("GUI App")
        self.root.geometry("1280x720")
        self.new_messenger = None
        self.receiver_thread = None
        self.username = username

        self.__setup_gui()

    def start(self) -> None:
        from Messenger import Messenger
        self.new_messenger = Messenger('13.51.167.39', 12345, self, self.username)
        self.new_messenger.start()

        self.receiver_thread = threading.Thread(
            target=self.new_messenger.receive_message,
            daemon=True,
            args=(self.new_messenger.client_socket,))

        self.receiver_thread.start()

    def __setup_gui(self) -> None:
        self.canvas1 = tk.Canvas(self.root, height=int(self.root.winfo_screenheight() * 0.45))
        self.canvas1.pack(fill=tk.BOTH, expand=True, padx=5)

        tk.Label(self.canvas1, text='Messages', font=('Arial', 12, 'bold')).pack(side=tk.TOP, fill=tk.X)

        self.text_field1 = tk.Text(self.canvas1, wrap=tk.WORD, height=1, width=0, state=tk.DISABLED)
        self.scrollbar1 = tk.Scrollbar(self.canvas1, command=self.text_field1.yview)
        self.text_field1.config(yscrollcommand=self.scrollbar1.set)

        self.text_field1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas2 = tk.Canvas(self.root, height=int(self.root.winfo_screenheight() * 0.45))
        self.canvas2.pack(fill=tk.BOTH, expand=True, padx=5)

        tk.Label(self.canvas2, text='Service Information', font=('Arial', 12, 'bold')).pack(side=tk.TOP, fill=tk.X)
        self.text_field2 = tk.Text(self.canvas2, wrap=tk.WORD, height=1, width=0, state=tk.DISABLED)
        self.scrollbar2 = tk.Scrollbar(self.canvas2, command=self.text_field2.yview)
        self.text_field2.config(yscrollcommand=self.scrollbar2.set)

        self.text_field2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas3 = tk.Canvas(self.root, height=int(self.root.winfo_screenheight() * 0.1), bg='blue')
        self.canvas3.pack(fill=tk.X, pady=15, padx=5)

        self.entry = tk.Entry(self.canvas3)
        self.button = tk.Button(self.canvas3, text="Submit", command=self.__on_button_click)
        self.root.bind('<Return>', self.__on_button_click)

        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.button.pack(side=tk.RIGHT, fill=tk.BOTH)

    def __on_button_click(self, event=None) -> None:
        s = self.entry.get()
        if s != "":
            s = self.username + ": " + s
            self.new_messenger.send_message(s)
            self.entry.delete(0, tk.END)

    @staticmethod
    def field_insert(field, s):
        field.config(state=tk.NORMAL)
        s += '\n'
        field.insert(tk.INSERT, s)
        field.config(state=tk.DISABLED)
