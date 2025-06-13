from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, StringVar, Entry
from comunicacion_serial import Comunicacion
from openpyxl import Workbook
from datetime import datetime
import threading
import time
import collections
import grafica_terminal 


### Define la una clase que se usara en el script
class Grafica(Frame):

   ## esta definicion se ejecuta una sola vez al inicio
   def __init__(self,master, *args):
      super().__init__(master, *args)
      ## en esta seccion se definen clases que se van a utilizar en el resto del codigo   
       
      ## crea una placa para comunicacion
      self.datos_placa = Comunicacion()
      self.datos_placa.puertos_disponibles()
    
      self.datos_placa.recibida.clear() #Se limpia el evento del hilo principal por primera vez
      self.widgets()    ## Se llama al metodo que confugura la interface grafica


   ##
   def widgets(self):
      color_fondo = '#cedee1'
      color_boton = '#546981'
      fondo_etiqueta = '#1a2d45'
      color_letra = '#FBFBFB'
      color_test = '#000000'
      color_test_2 = '#FFFFFF'
      color_test_3 = '#FF0000'
      color_test_4 = '#00FF00'

      # Crea un un metodo para definir los frames que se van a utilizar
      grafica_terminal.crear_frames(self)

      ## establece los tamaños relatitivos de ecpancion de las columas
      self.master.columnconfigure(0, weight=1)
      self.master.columnconfigure(1, weight=1)
      self.master.columnconfigure(2, weight=1)
      ## establece los tamaños relatitivos de ecpancion de las filas
      self.master.rowconfigure(0, weight=5)
      self.master.rowconfigure(1, weight=1)
      self.master.rowconfigure(2, weight=1)
      self.master.rowconfigure(3, weight=1)
      self.master.rowconfigure(4, weight=1)
      self.master.rowconfigure(5, weight=1)
      self.master.rowconfigure(6, weight=1)
      self.master.rowconfigure(7, weight=1)
      self.master.rowconfigure(8, weight=1)
      self.master.rowconfigure(9, weight=1)
      self.master.rowconfigure(10, weight=1)
      self.master.rowconfigure(11, weight=1)
      self.master.rowconfigure(12, weight=1)
      self.master.rowconfigure(13, weight=1)
      self.master.rowconfigure(14, weight=1)
      self.master.rowconfigure(15, weight=1)
      self.master.rowconfigure(16, weight=1)
      self.master.rowconfigure(17, weight=1)
      self.master.rowconfigure(18, weight=1)
      self.master.rowconfigure(19, weight=1)
      self.master.rowconfigure(20, weight=1)


      # Crea una etiqueta que sera modificada por SMS
      self.valor_actual_1_t = Label(self.frame_b, text="----", font=('Arial', 12, 'bold'), bg=color_fondo)
      self.valor_actual_1_t.grid(row=0, column=0, padx=5, pady=5)


      # define un boton
      
      self.bt_iniciar = Button(self.frame_c, text='conectar_serial', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.conectar_serial)
      self.bt_iniciar.grid(row=2, column=0, pady=5)

      # define botones para accder a las diferentes parametros de pozos
      fuente = ('Arial', 12, 'bold')
      ancho_boton = 10
      self.bt_p1 = Button(self.frame_1, text='Pozo 1', font=fuente, width=ancho_boton, bg=color_boton, fg=color_letra)
      self.bt_p1.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')



      # Crea un hilo para majar la parte logica del almacenamiento de los datos
   

   ## define un metodo que se ejecuta al pulsar el boton
   def conectar_serial(self):
      None

### Inicia el bucle principal
if __name__ == "__main__":
   terminal = Tk()
   terminal.geometry('1366x768')    #('742x535')
   terminal.config(bg='#010808', bd=4)
   terminal.wm_title('Central de pozos')
   terminal.minsize(width=700, height=400)  # Corregido el nombre de 'minisize' a 'minsize'
   terminal.call('wm', 'iconphoto', terminal._w, PhotoImage(file='img1.png'))
   app = Grafica(terminal)  ## crea un elemento de una clase, en esta se establece el bucle que se va seguir
   app.mainloop()    ## ejecuta la funcion de principal de la clase