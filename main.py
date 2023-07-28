from tkinter import *
from tkinter import messagebox
import tkinter.colorchooser as cc
import pyperclip


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # Creo la interfaz grafica
    def create_widgets(self):
        self.label = Label(self, text="Color", width=20, height=10)
        self.label.pack(side="left", padx=10, pady=20)
        self.copy_button = Button(self, text="Copiar", command=self.copy_text)
        self.copy_button.pack(side="left", padx=10)
        self.button = Button(root, text="Seleccionar color", command=self.choose_color)
        self.button.pack(pady=10)

    # Metodo para copiar el texto del color seleccionado al portapapeles
    def copy_text(self):
        text = self.label.cget("text")
        pyperclip.copy(text)
        messagebox.showinfo("Copiado", "Texto copiado al portapapeles")

    # Metodo para seleccionar el color
    def choose_color(self):
        color = cc.askcolor()
        if color:
            hex_value = color[1]
            self.label.config(bg=hex_value, text=hex_value)


root = Tk()
root.title("Paleta de colores")
root.geometry("250x250")
root.resizable("0", "0")
app = Application(master=root)
app.mainloop()
