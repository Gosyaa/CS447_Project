from tkinter import Tk
from GuiApp import GuiApp

if __name__ == "__main__":
    root: Tk = Tk()
    root.geometry("1280x720")
    app: GuiApp = GuiApp(root)
    app.start()
    root.mainloop()
