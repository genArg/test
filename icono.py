from tkinter import Tk

ventana = Tk()
ventana.title("Mi App con ícono")
ventana.geometry("400x300")

# Esta línea tiene efecto completo solo si se compila a .exe
ventana.iconbitmap("icono.ico")

ventana.mainloop()