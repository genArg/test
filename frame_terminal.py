import sys
import tkinter as tk

class ConsolaEnTk:
    def __init__(self, widget_texto):
        self.widget = widget_texto

    def write(self, mensaje):
        self.widget.insert(tk.END, mensaje)
        self.widget.see(tk.END)  # Auto-scroll

    def flush(self):
        pass  # Necesario para compatibilidad con sys.stdout

# Interfaz principal
root = tk.Tk()
root.title("Salida de consola en Tkinter")

frame_consola = tk.Frame(root)
frame_consola.pack(padx=10, pady=10)

# Widget tipo consola
texto_consola = tk.Text(frame_consola, height=15, width=60, bg="black", fg="lime")
texto_consola.pack()

# Redirigir print()
sys.stdout = ConsolaEnTk(texto_consola)

# Prueba
print("Hola desde consola")
print("Esto reemplaza al terminal")

root.mainloop()
