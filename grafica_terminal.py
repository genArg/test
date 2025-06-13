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

      self.frame_c = Frame(self.master, bg=color_fondo_titulo_2, bd=0, relief=borde_tipo)
      self.frame_c.grid(column=2, row=0, sticky='nsew')

      # columna 1
      self.frame_1 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_1.grid(column=0, row=1, sticky='nsew')

      self.frame_2 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_2.grid(column=0, row=2, sticky='nsew')

      self.frame_3 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_3.grid(column=0, row=3, sticky='nsew')

      self.frame_4 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_4.grid(column=0, row=4, sticky='nsew')

      self.frame_5 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_5.grid(column=0, row=5, sticky='nsew')

      self.frame_6 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_6.grid(column=0, row=6, sticky='nsew')

      self.frame_7 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_7.grid(column=0, row=7, sticky='nsew')

      self.frame_8 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_8.grid(column=0, row=8, sticky='nsew')

      self.frame_9 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_9.grid(column=0, row=9, sticky='nsew')

      self.frame_10 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_10.grid(column=0, row=10, sticky='nsew')

      self.frame_11 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_11.grid(column=0, row=11, sticky='nsew')

      self.frame_12 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_12.grid(column=0, row=12, sticky='nsew')

      self.frame_13 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_13.grid(column=0, row=13, sticky='nsew')

      self.frame_14 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_14.grid(column=0, row=14, sticky='nsew')

      self.frame_15 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_15.grid(column=0, row=15, sticky='nsew')

      self.frame_16 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_16.grid(column=0, row=16, sticky='nsew')

      self.frame_17 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_17.grid(column=0, row=17, sticky='nsew')

      self.frame_18 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_18.grid(column=0, row=18, sticky='nsew')

      self.frame_19 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_19.grid(column=0, row=19, sticky='nsew')

      self.frame_20 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_20.grid(column=0, row=20, sticky='nsew')

      # columna 2

      self.frame_21 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_21.grid(column=1, row=1, sticky='nsew')

      self.frame_22 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_22.grid(column=1, row=2, sticky='nsew')

      self.frame_23 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_23.grid(column=1, row=3, sticky='nsew')

      self.frame_24 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_24.grid(column=1, row=4, sticky='nsew')

      self.frame_25 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_25.grid(column=1, row=5, sticky='nsew')

      self.frame_26 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_26.grid(column=1, row=6, sticky='nsew')

      self.frame_27 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_27.grid(column=1, row=7, sticky='nsew')

      self.frame_28 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_28.grid(column=1, row=8, sticky='nsew')

      self.frame_29 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_29.grid(column=1, row=9, sticky='nsew')

      self.frame_30 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_30.grid(column=1, row=10, sticky='nsew')

      self.frame_31 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_31.grid(column=1, row=11, sticky='nsew')

      self.frame_32 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_32.grid(column=1, row=12, sticky='nsew')

      self.frame_33 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_33.grid(column=1, row=13, sticky='nsew')

      self.frame_34 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_34.grid(column=1, row=14, sticky='nsew')

      self.frame_35 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_35.grid(column=1, row=15, sticky='nsew')

      self.frame_36 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_36.grid(column=1, row=16, sticky='nsew')

      self.frame_37 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_37.grid(column=1, row=17, sticky='nsew')

      self.frame_38 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_38.grid(column=1, row=18, sticky='nsew')

      self.frame_39 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_39.grid(column=1, row=19, sticky='nsew')

      self.frame_40 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_40.grid(column=1, row=20, sticky='nsew')

      # columna 3
      self.frame_41 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_41.grid(column=2, row=1, sticky='nsew')

      self.frame_42 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_42.grid(column=2, row=2, sticky='nsew')

      self.frame_43 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_43.grid(column=2, row=3, sticky='nsew')

      self.frame_44 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_44.grid(column=2, row=4, sticky='nsew')

      self.frame_45 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_45.grid(column=2, row=5, sticky='nsew')

      self.frame_46 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_46.grid(column=2, row=6, sticky='nsew')

      self.frame_47 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_47.grid(column=2, row=7, sticky='nsew')

      self.frame_48 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_48.grid(column=2, row=8, sticky='nsew')

      self.frame_49 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_49.grid(column=2, row=9, sticky='nsew')

      self.frame_50 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_50.grid(column=2, row=10, sticky='nsew')

      self.frame_51 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_51.grid(column=2, row=11, sticky='nsew')

      self.frame_52 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_52.grid(column=2, row=12, sticky='nsew')

      self.frame_53 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_53.grid(column=2, row=13, sticky='nsew')

      self.frame_54 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_54.grid(column=2, row=14, sticky='nsew')

      self.frame_55 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_55.grid(column=2, row=15, sticky='nsew')

      self.frame_56 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_56.grid(column=2, row=16, sticky='nsew')

      self.frame_57 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_57.grid(column=2, row=17, sticky='nsew')

      self.frame_58 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_58.grid(column=2, row=18, sticky='nsew')

      self.frame_59 = Frame(self.master, bg=color_fondo_1, bd=borde_ancho, relief=borde_tipo)
      self.frame_59.grid(column=2, row=19, sticky='nsew')

      self.frame_60 = Frame(self.master, bg=color_fondo_2, bd=borde_ancho, relief=borde_tipo)
      self.frame_60.grid(column=2, row=20, sticky='nsew')
