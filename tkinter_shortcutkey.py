import tkinter as tk
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.master.geometry("300x300")
        self.master.title("Menubar Sample")
        self.create_menubar()

    def create_menubar(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.onOpen, accelerator="Ctrl+O")
        self.master.config(menu=menubar)
        self.bind_all("<Control-o>", self.onOpen)

    def onOpen(self, event=None):
        print("on open")


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
