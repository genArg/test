from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, StringVar, Entry
from comunicacion_serial import Comunicacion
from openpyxl import Workbook
from datetime import datetime
import threading
import time
import collections

## Define la una clase que se usara en el script
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

      ## define los frames en lo que se divide la interface grafica
      frame = Frame(self.master, bg=color_fondo, bd=4)
      #frame.grid(column=0, row=0, sticky='nsew')
      frame.pack(padx=10, pady=10)


      ## establece los tamaños relatitivos de ecpancion de las columas
      self.master.columnconfigure(0, weight=1)
      
      ## establece los tamaños relatitivos de ecpancion de las filas
      self.master.rowconfigure(0, weight=1)

      ## Crea una etiqueta que sera modificada por SMS
      self.valor_actual_1_t = Label(frame, text="----", font=('Arial', 12, 'bold'), bg=color_fondo)
      self.valor_actual_1_t.grid(row=0, column=0, padx=5, pady=5)


      ## define un boton
      
      self.bt_iniciar = Button(frame, text='conectar_serial', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.conectar_serial)
      self.bt_iniciar.grid(row=2, column=0, pady=5)

      ## extrae informacion de puertos y velocidades
      baud = self.datos_placa.baudrates
      self.combobox_baud = ttk.Combobox(frame, values=baud, justify='center', width=12, font='Arial')
      self.combobox_baud.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
      self.combobox_baud.current(3)
      try:
         port = self.datos_placa.puertos
         self.combobox_port = ttk.Combobox(frame, values=port, justify='center', width=12, font='Arial')
         self.combobox_port.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
         self.combobox_port.current(0)
      except:
         pass


      ## Crea un hilo para majar la parte logica del almacenamiento de los datos
      self.CrearHilo()


   def CrearHilo(self):
      
      hilo_principal = threading.Thread(target=self.HiloPrincipal)
      hilo_principal.setDaemon(1)
      hilo_principal.start() #Inicia el hilo principal


   def HiloPrincipal(self):
      while True:
         self.datos_placa.recibida.clear() #Limpia el evento
         self.datos_placa.recibida.wait() #Espera a que se active el evento nuevamente

         self.datos = self.datos_placa.datos_recibidos # guarda el texto obtenido en una variable
         self.valor_actual_1_t.config(text=self.datos)


   def conectar_serial(self):

      self.datos_placa.placa.port = self.combobox_port.get()
      self.datos_placa.placa.baudrate = self.combobox_baud.get()
      self.datos_placa.conexion_serial()
      self.enviar_sms()

    

   def enviar_sms(self):
    try:
        modem = self.datos_placa.placa  # Este es tu serial.Serial
        if not modem.is_open:
            self.valor_actual_1_t.config(text="Puerto cerrado")
            return

        def send_at(command, delay=1):
            modem.write((command + '\r').encode())
            time.sleep(delay)
            while modem.in_waiting:
                print(modem.read(modem.in_waiting).decode(errors='ignore'), end='')

        # Secuencia AT
        send_at('AT')                         # Prueba de conexión
        send_at('AT+CNMI=2,2,0,0,0')          # Mostrar mensajes entrantes
        send_at('AT+CMGF=1')                  # Modo texto
        send_at('AT+CMGS="+543815465274"')    # Número destino
        time.sleep(1)
        modem.write(b'ya esta funcionando, este mensaje lo envio desde el modulo')
        modem.write(bytes([26]))              # Ctrl+Z
        time.sleep(3)

        self.valor_actual_1_t.config(text="SMS enviado")

    except Exception as e:
        self.valor_actual_1_t.config(text="Error enviando SMS")
        print(f"Error: {e}")



## Inicia el bucle principal
if __name__ == "__main__":
   terminal = Tk()
   terminal.geometry('742x535')
   terminal.config(bg='#010808', bd=4)
   terminal.wm_title('Central de pozos')
   terminal.minsize(width=700, height=400)  # Corregido el nombre de 'minisize' a 'minsize'
   terminal.call('wm', 'iconphoto', terminal._w, PhotoImage(file='img1.png'))
   app = Grafica(terminal)  ## crea un elemento de una clase, en esta se establece el bucle que se va seguir
   app.mainloop()    ## ejecuta la funcion de principla de la clase

   