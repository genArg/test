
import serial, serial.tools.list_ports #Nos permite reconocer los puertos disponibles
from threading import Thread, Event #Sirve para crear subprocesos, ya que vamos a estar recibiendo datos y graficando

class Comunicacion():
  def __init__(self, *args): #Metodo constructor
    super().__init__(*args)
    self.datos_recibidos = "" #Se crea la variable "dato recibido"

    self.placa = serial.Serial() #Objeto placa para la comunicacion serial
    self.placa.timeout = 0.5 #Tiempo de espera de la comunicacion cuando termina

    self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200'] #Se crea la lista de la velocidad en baudios que luego se le asigna al COM2
    self.puertos = [] #Lista para asignar a los puertos

    self.señal = Event()
    self.hilo = None

    self.recibida = Event() #Se utiliza como bandera cuando se recibe una trama

  def puertos_disponibles (self): #Método para leer los puertos disponibles
    try:
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]
    except:
        pass

  def conexion_serial(self): #Método para abrir placa
      try:
          self.placa.open () #Se abre placa
      except: #Se crea una excepcion para que en caso de nos salga error, lo evitamos
          pass
      if (self.placa.is_open): #Si el placa está abierto se inicia el hilo
          self.iniciar_hilo()
          print ('Conectado')

  def enviar_datos(self, data): #Método para enviar datos
      if (self.placa.is_open): #Verifica si se está realizando la conexión
          self.datos = str(data) + "\n" #Obtenemos el dato
          self.placa.write(self.datos.encode()) #Escribimos el placa, asignandole los datos a enviar
      else:
          print ('Error') #Si no se realiza la conexión se imprime un error

  def leer_datos(self): #Método para leer los datos
      try: #Se crea una excepción para que no dé error
          while (self.señal.isSet() and self.placa.is_open): #Se ejecuta constantemente la instruccion de leer la señal, con el while
              data = self.placa.readline().decode("utf-8").strip() #Con "data" leemos los datos del placa y con "decode" decodificamos
              if(len(data)>1): #Verificamos que se haya recibido el dato
                  self.datos_recibidos=data #Se lo asignamos a la variable data
                  self.recibida.set() #Activa la bandera al recibir una trama
      except TypeError:
          pass

  def iniciar_hilo(self): #Método para iniciar el hilo
      self.hilo = Thread(target=self.leer_datos) #Creamos el objeto hilo, donde en "target recibe el metodo que se va a ejecutar"
      self.hilo.setDaemon(1)
      self.señal.set()
      self.hilo.start()

  def stop_hilo(self): #Método para detener el hilo
      if(self.hilo is not None): #Se verifica que no sea none
          self.señal.clear() #Se elimina la señal
          self.hilo.join()
          self.hilo = None

  def desconectar(self): #Método para desconectar
      self.placa.close() #Se cierra la conexion con el placa
      self.stop_hilo() #Finaliza el hilo