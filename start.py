from tkinter import Tk
from GuiApp import GuiApp

if __name__ == "__main__":
    root: Tk = Tk()
    app: GuiApp = GuiApp(root, "Maksim")
    app.start()
    root.mainloop()
