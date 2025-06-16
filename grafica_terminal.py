from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, StringVar, Entry

# crea los frames que se van a utilizar en la interfaz gráfica
def crear_frames(self):
      """Define los frames que se van a utilizar en la interfaz gráfica."""
      color_fondo_titulo_1 = '#cedee1'
      color_fondo_titulo_2 = '#ce9ee1'
      color_fondo_1 = '#c8e6c9'
      color_fondo_2 = '#e8f5e9'
      color_test_1 = '#000000'
      color_test_2 = '#FFFFFF'
      color_test_3 = '#FF0000'
      color_test_4 = '#00FF00'
      borde_ancho = 2
      borde_tipo = 'groove'  # 'groove' es un tipo de borde que simula un surco o canal|

      '''relief='solid': define el tipo de borde. Otros valores posibles son:

'flat' (predeterminado, sin relieve)

'raised' (bordes elevados)

'sunken' (bordes hundidos)

'ridge' (bordes biselados hacia afuera)

'groove' (bordes biselados hacia adentro)

'solid' (borde plano y definido, el que simula un contorno visible)'''

        # Crea los frames con los colores definidos
      
      # frame para demas configuraciones de la interfaz
      self.frame_a = Frame(self.master, bg=color_fondo_titulo_1, bd=0, relief=borde_tipo)
      self.frame_a.grid(column=0, row=0, sticky='nsew')

      self.frame_b = Frame(self.master, bg=color_fondo_titulo_2, bd=0, relief=borde_tipo)
      self.frame_b.grid(column=1, row=0, sticky='nsew')

      self.frame_c = Frame(self.master, bg=color_test_4, bd=0, relief=borde_tipo)
      self.frame_c.grid(column=2, row=0, sticky='nsew')

      # se crean botones para accder a la informacion de los pozos
      self.boton = [[None for _ in range(3)] for _ in range(21)]
      for j in range(3):
        for i in range(1,21):
            color = color_fondo_1 if i % 2 == 1 else color_fondo_2
            self.boton[i][j] = Button(
                self.master,
                text=f'Pozo {i+j*20}',
                bg=color,
                bd=borde_ancho,
                relief=borde_tipo,
                font=('Arial', 10),
                command=lambda i=i, j=j: self.pozo_accion(i, j)  # Asigna una función de acción al botón
            )
            self.boton[i][j].grid(column=j, row=i, sticky='nsew')



