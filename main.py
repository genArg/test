from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, StringVar, Entry
from comunicacion_serial import Comunicacion
from openpyxl import Workbook
from datetime import datetime
import threading
import time
import collections
import grafica_terminal 
import webbrowser

pantalla_ancho = 1366
pantalla_alto = 768  


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
      self.master.rowconfigure(0, weight=10)
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

      #cofigura el tamaño de los frames
      self.master.grid_rowconfigure(0, minsize=100)
      self.master.grid_columnconfigure(0, minsize=pantalla_ancho//3)

      self.master.grid_rowconfigure(0, minsize=100)
      self.master.grid_columnconfigure(1, minsize=pantalla_ancho//3)

      self.master.grid_rowconfigure(0, minsize=100)
      self.master.grid_columnconfigure(2, minsize=pantalla_ancho//3)



      # Crea una etiqueta que sera modificada por SMS
      self.valor_actual_1_t = Label(self.frame_b, text="----", font=('Arial', 12, 'bold'), bg=color_fondo)
      self.valor_actual_1_t.grid(row=0, column=0, padx=5, pady=5)
      self.valor_actual_2_t = Label(self.frame_b, text="----", font=('Arial', 12, 'bold'), bg=color_fondo)
      self.valor_actual_2_t.grid(row=1, column=0, padx=5, pady=5)
      self.bt_conectar = Button(self.frame_b, text='localizacion', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.localizar)
      self.bt_conectar.grid(row=2, column=0, pady=5)


      ## extrae informacion de puertos y velocidades
      baud = self.datos_placa.baudrates
      self.combobox_baud = ttk.Combobox(self.frame_a, values=baud, justify='center', width=12, font='Arial')
      self.combobox_baud.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
      self.combobox_baud.current(6)
      try:
         port = self.datos_placa.puertos
         self.combobox_port = ttk.Combobox(self.frame_a, values=port, justify='center', width=12, font='Arial')
         self.combobox_port.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
         self.combobox_port.current(0)
      except:
         pass

      self.bt_conectar = Button(self.frame_a, text='conectar_serial', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.conectar_serial)
      self.bt_conectar.grid(row=0, column=2, pady=5)

      # Crea un hilo para majar la parte logica del almacenamiento de los datos
      self.CrearHilo()
   
   ## define un metodo que se ejecuta al pulsar el boton
   def pozo_accion(self, i, j):
       print(f"Hola desde el pozo {i},{j}")
       pass

   ## define un metodo que se ejecuta al pulsar el boton
   def conectar_serial(self):
      self.datos_placa.placa.port = self.combobox_port.get()
      self.datos_placa.placa.baudrate = self.combobox_baud.get()
      self.datos_placa.conexion_serial()
      print(f"Conectando a {self.datos_placa.placa.port} a {self.datos_placa.placa.baudrate} baudios")
      self.configurar_modem()

   def configurar_modem(self):
      try:
          modem = self.datos_placa.placa  # Este es tu serial.Serial
          if not modem.is_open:
              self.valor_actual_1_t.config(text="Puerto cerrado")
              return

          modem.write(b'AT+CMGF=1\r')  # Configura el modo de mensaje de texto
          time.sleep(0.5)  # Espera un poco para que el comando se procese
          modem.write(b'AT+CNMI=2,2,0,0,0\r')  # Configura la notificación de nuevos mensajes
          time.sleep(0.5)  # Espera un poco para que el comando se procese
          self.valor_actual_2_t.config(text="Modem configurado")
      except Exception as e:
          self.valor_actual_2_t.config(text=f"Error: {str(e)}")

   ## crea un hilo para manejar la recepcion de datos
   def CrearHilo(self):
      
      hilo_principal = threading.Thread(target=self.HiloPrincipal)
      hilo_principal.setDaemon(1)
      hilo_principal.start() #Inicia el hilo principal

   ## define el metodo que se ejecuta en el hilo principal
   def HiloPrincipal(self):
      while True:
         self.datos_placa.recibida.clear() #Limpia el evento
         self.datos_placa.recibida.wait() #Espera a que se active el evento nuevamente

         self.datos_1 = self.datos_placa.datos_recibidos_1 # guarda el texto obtenido en una variable
         self.datos_2 = self.datos_placa.datos_recibidos_2
         self.valor_actual_1_t.config(text=self.datos_1)
         print(self.datos_1)  # Imprime los datos recibidos en la consola
         print(self.datos_2)

         dato = self.datos_1.split('"')  # Divide los datos en una lista usando la coma como separador
         #identificador = dato[0].split('"')  # Divide el primer elemento en dos partes usando el ':' como separador


         try:
            self.identificacion_alfa = dato[1]            
            self.valor_actual_2_t.config(text=self.datos_2) # se muestra el texto en la etiqueta
            if (self.identificacion_alfa == '+5493815465274'):
               self.boton[1][0].config(bg='#FF0000')  # Cambia el color del botón a rojo
         except:
            pass

   ## define un metodo para establece la localizacion mediante google maps
   def localizar(self):
      print("Localizando...")
      self.valor_actual_2_t.config(text="Localizando...")
      # URL de Google Maps
      url = 'https://maps.app.goo.gl/XuEL6btjdLmpPGTL9'
      # Abre la URL en el navegador predeterminado
      webbrowser.open(url)
      pass

### Inicia el bucle principal
if __name__ == "__main__":
   terminal = Tk()
   terminal.geometry(f"{pantalla_ancho}x{pantalla_alto}")#('1366x768')    #('742x535')
   terminal.config(bg='#010808', bd=4)
   terminal.wm_title('Central de pozos')
   terminal.minsize(width=700, height=400)  # Corregido el nombre de 'minisize' a 'minsize'
   terminal.call('wm', 'iconphoto', terminal._w, PhotoImage(file='img1.png'))
   app = Grafica(terminal)  ## crea un elemento de una clase, en esta se establece el bucle que se va seguir
   app.mainloop()    ## ejecuta la funcion de principal de la clase