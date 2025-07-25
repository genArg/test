from tkinter import IntVar, Tk, Frame, Button, Label, ttk, PhotoImage, StringVar, Entry
import serial, serial.tools.list_ports #Nos permite reconocer los puertos disponibles
import time
import grafica_terminal
import webbrowser
import threading
from actualizar_json import convertir_vector

# Configuración de la pantalla
pantalla_ancho = 742 #1366
pantalla_alto = 535 #768

#colores 
color_fondo = '#e8f5e9'
color_fondo_azul = '#00001c'
color_boton = '#546981'
fondo_etiqueta = '#1a2d45'
color_letra = '#FBFBFB'
color_test = '#000000'
color_test_2 = '#FFFFFF'
color_test_3 = '#FF0000'
color_test_4 = '#00FF00'
color_fondo_titulo_1 = '#cedee1'
color_fondo_titulo_2 = '#ce9ee1'
color_rojo = '#FF0000'
color_naranja = '#FFA500'
color_negro = '#000000'
color_blanco = '#FFFFFF'
color_verde = '#00FF00'
color_gris = '#505050'
# velocidad de la comunicacion serial e8f5e9
velocidad = 115200
# comando para filtrar mensajes
comando = "Tx"
# tiempo de refresco de pozos en minutos
tiempo_refresco_pozos = 60

n = 3 # Número de segundos para cambiar el bit_n_segundo

### Define la una clase que se usara en el script
class Grafica(Frame):

   ## esta definicion se ejecuta una sola vez al inicio
   def __init__(self,master, *args):
      super().__init__(master, *args)
      ## en esta seccion se definen clases que se van a utilizar en el resto del codigo  
# ✅ añade variable grafica
      self.imagen = PhotoImage(file="img2.png") # añade una imagen
      #self.imagen_2 = PhotoImage(file="img1.png") # añade una imagen
      # 
      self.puerto_usado = "none_2"
      # Define el una variable para actualizar los botones medido en segundos
      self.tiempo_muerto_1 = 0
      #Variable para establecer el tiempo de refresco de los pozos
      self.tiempo_refresco = IntVar()

      ## bit de tiempo
      self.bit_un_segundo = 0
      self.bit_n_segundo = 0
      self.contador_n_segundo = 0

      # vector de estados de los pozos
      self.estados_pozos = [tiempo_refresco_pozos] * 60
      self.contador_pozos = 0
      self.mensajes_pozos = ["sin conectar"] * 60

      self.lista_pozos = []  # Lista para almacenar los pozos

      #self.datos_placa.recibida.clear() #Se limpia el evento del hilo principal por primera vez
      self.widgets()    ## Se llama al metodo que confugura la interface grafica


    
    ##
   def widgets(self):

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
      self.frame_a.grid_columnconfigure(0, weight=1)
      self.frame_a.grid_columnconfigure(1, weight=1)
      self.frame_a.grid_columnconfigure(2, weight=1)

      Label(self.frame_a, image=self.imagen, bd=0).grid(row=0, column=1)
      #Label(self.frame_a, image=self.imagen_2).grid(row=0, column=1, padx=5)

      #self.tag_1 = Label(self.frame_c, text="----", font=('Arial', 12, 'bold'), bg=color_fondo)
      #self.tag_1.grid(row=0, column=0, padx=5, pady=5)
      #self.bt_conectar = Button(self.frame_c, text='ejecutar', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.localizar)
      ##self.bt_conectar.grid(row=3, column=0, pady=5)



      ## extrae informacion de puertos
      try:
         port = [port.device for port in serial.tools.list_ports.comports()]
         self.combobox_port = ttk.Combobox(self.frame_b, values=port, justify='center', width=12, font='Arial')
         self.combobox_port.grid(row=0, column=0, padx=5, pady=5)
         self.combobox_port.current(0)
      except:
         print("No se encontraron puertos disponibles.")
         pass

      # Crea un boton para conectar al módem GSM
      self.bt_conectar = Button(self.frame_b, text='Conectar', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.ConectarPlaca)
      self.bt_conectar.grid(row=0, column=1, pady=5)

      self.lb_indicador_conexion = Label(self.frame_b, text="●", font=('Arial', 25, 'bold'), fg=color_gris, bg=color_fondo)
      self.lb_indicador_conexion.grid(row=0, column=2, padx=5, pady=5)

      # Crea un una caja para establecer el tiempo de refresco de los pozos
      self.tiempo_refresco.set(tiempo_refresco_pozos)  # Valor entero por defecto
      self.box_tiempo_refresco=Entry(self.frame_b, textvariable=self.tiempo_refresco, font=('Arial', 12, 'bold'), width=5)
      self.box_tiempo_refresco.grid(row=1, column=0, padx=1, pady=5)

      # Crea un boton para guardar el valor del tiempo de refresco
      self.bt_guardar = Button(self.frame_b, text='Actualizar', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.refrescar_pozos_accion)
      self.bt_guardar.grid(row=1, column=1, pady=5)
      # crea el boton localizacion
      self.bt_conectar = Button(self.frame_b, text='Localizar', font=('Arial', 12, 'bold'),width=12, bg=color_boton, fg=color_letra, command=self.localizar)
      self.bt_conectar.grid(row=2, column=0, pady=5)

      self.Iniciar_Temporizadores()  ## Crea los temporizadores para el control de tiempo



   def CrearHilo(self):
      
      hilo_principal = threading.Thread(target=self.HiloPrincipal, daemon=True)
      hilo_principal.start() #Inicia el hilo principal

   def CrearHilo_2(self):
      """Crea un hilo para manejar la lógica de actualización de estados."""
      hilo_actualizacion = threading.Thread(target=self.actualizar_estados, daemon=True)
      hilo_actualizacion.start()

   def ConectarPlaca(self):
      hilo_conexion = threading.Thread(target=self.conectar_serial, daemon=True)
      hilo_conexion.start()

   def Iniciar_Temporizadores(self):
      hilo_temporizador = threading.Thread(target=self.temporizadores, daemon=True)
      hilo_temporizador.start()

   ## define un metodo que ejecuta un temporizador cada n segundos
   def temporizadores(self):
      print("Iniciando temporizadores...")
      global n
      self.contador_n_segundo = 0
      while True:
         time.sleep(0.5)
         self.bit_un_segundo = not self.bit_un_segundo
         self.contador_n_segundo += 1
         self.contador_pozos += 1
         if self.contador_pozos == 10:
            self.contador_pozos = 0
            self.refrescar_pozos()  # Llama a la función para refrescar los pozos cada 60 segundos
            print(self.estados_pozos)            
         if self.contador_n_segundo == n:
            self.bit_n_segundo = not self.bit_n_segundo
            self.contador_n_segundo = 0
         self.tiempo_muerto_1 += 1
         if self.tiempo_muerto_1 > 9:
            self.tiempo_muerto_1 = 0

         
   ## define un metodo que se ejecuta en un hilo principal
   def HiloPrincipal(self):

      while (self.gsm.is_open):
         respuesta_interna = self.leer_mensajes()
         if respuesta_interna == True:
            self.borrar_mensajes()
         time.sleep(5)  # Espera 5 segundos antes de volver a leer los mensajes
      self.gsm.close()  # Cierra el puerto serial cuando se detiene el hilo

   ## metodo para conectarse al modulo gsm
   def conectar_serial(self):
        """Conecta al puerto serial y configura el módem GSM."""
        try:
            # Configura el puerto y la velocidad
            self.gsm = serial.Serial(self.combobox_port.get(), int(velocidad), timeout=1)
            time.sleep(1)  # Espera un poco para que el módem arranque
            self.puerto_usado = self.combobox_port.get()

            # Configura el modo texto para SMS
            print("Configurando modo texto...")
            self.enviar_comando('AT+CMGF=1', 0)

            # Selecciona la SIM como almacenamiento
            print("Usando la memoria de la SIM...")
            self.enviar_comando('AT+CPMS="SM"', 0)

            # Comprueba la conexión enviando un comando AT
            self.enviar_comando('AT', 0)
            print(self.respuesta)
            print("Conexión exitosa al módem GSM.")

            self.lb_indicador_conexion.config(fg=color_verde)
            self.refrescar_pozos_accion()

            ## Crea un hilo para majar la parte logica del almacenamiento de los datos
            self.CrearHilo() # Lectura de mensajes en un hilo separado
            self.CrearHilo_2() # Actualización de estados en la interfaz gráfica

        except Exception as e:
            print(f"Error al conectar: {e}")
            self.lb_indicador_conexion.config(fg=color_rojo)
            self.combobox_port.set('')  # Limpia la selección si no hay puertos
            port = [port.device for port in serial.tools.list_ports.comports()]
            self.combobox_port.configure(values=port) # = ttk.Combobox(self.frame_a, values=port, justify='center', width=12, font='Arial')
            

      ## Envia un comando al módem GSM y espera una respuesta
   def enviar_comando(self, comando, espera=1):
        self.gsm.write((comando + '\r').encode())
        time.sleep(espera)
        self.respuesta = self.gsm.readlines()
        return [linea.decode(errors='ignore').strip() for linea in self.respuesta]
   
   def leer_mensajes(self):
      # Lee todos los SMS almacenados
      retorno = False
      respuesta_interna = "none_1"
      print("Leyendo SMS...")
      try:
         respuesta_interna = self.enviar_comando('AT+CMGL="ALL"', espera=2)  # Lee todos los mensajes de la SIM
         print(respuesta_interna)
         print(len(respuesta_interna))
      except Exception as e:
         print(f"Error al leer mensajes: {e}")
      if len(respuesta_interna) > 4:
         retorno = self.logica_filtro_mensaje(respuesta_interna)  # Llama a la función para procesar los mensajes
      return retorno

   ## Borra los mensajes de la SIM
   def borrar_mensajes(self):
      try:
         # Borra todos los mensajes de la SIM
         print("Borrando todos los SMS...")
         self.enviar_comando('AT+CMGDA="DEL ALL"', espera=2)  # Borra todos los mensajes
      except Exception as e:
         print(f"Error al borrar mensajes: {e}")

   ## define un metodo que se ejecuta al recibir un mensaje
   def logica_filtro_mensaje(self, mensaje):
      
      retorno = False
      # Muestra los mensajes
      indice=0
      for linea in mensaje:
         indice += 1
         if linea.startswith(comando):
            dato = linea.split(".")
            self.lista_pozos.append([dato[1], dato[4]])  # Agrega el pozo a la lista
            self.estados_pozos[int(dato[1])-1] = 0 - 1 - int(dato[4])
# ✅ gurada la hora y fecha en el boton del pozo            
            try:
               self.mensajes_pozos[int(dato[1])-1] = mensaje[indice-2]
            except IndexError:
               print(f"no se almaceno el estado.")
               continue

            retorno = True
      
      return retorno

            

   def actualizar_estados(self):
      """Actualiza los estados de los elementos en la interfaz gráfica."""
      while self.gsm.is_open :
         time.sleep(5)  # Espera 5 segundos antes de actualizar los estados
         #if self.tiempo_muerto_1 == 0 or self.tiempo_muerto_1 ==5:
         for indice in range(len(self.estados_pozos)):
            (i,j) = self.logica_separacion_argunmentos(indice + 1)
            if self.estados_pozos[indice] == (-2):
               self.boton[int(i)][int(j)].config(bg=color_verde)
               self.estados_pozos[indice] = self.tiempo_refresco.get()
# ✅ Actualiza texto del botón de forma segura
               mensaje = self.mensajes_pozos[indice]
               self.boton[int(i)][int(j)].config(text=f'Pozo {i + j*20} - {mensaje}')
            if self.estados_pozos[indice] == (-1):
               self.boton[int(i)][int(j)].config(bg=color_rojo)
               #self.estados_pozos[indice] = self.tiempo_refresco.get()
# ✅ Actualiza texto del botón de forma segura
               mensaje = self.mensajes_pozos[indice]
               self.boton[int(i)][int(j)].config(text=f'Pozo {i + j*20} - {mensaje}')
            if self.estados_pozos[indice] == 0:
               self.boton[int(i)][int(j)].config(bg=color_naranja)
         try:      
            convertir_vector(self.estados_pozos)
         except IndexError:
               print(f"Error: No se pudo enviar el vector de estados.")
               continue
         '''if True:

            # Aquí puedes actualizar las etiquetas o botones según el estado de los pozos
            if self.lista_pozos:
               for pozo in self.lista_pozos:
                  print(self.lista_pozos)
                  i = int(pozo[0])
                  estado = int(pozo[1])
                  j=0
                  (i,j) = self.logica_separacion_argunmentos(i)
                  if estado == 0: 
                     try:
                        self.boton[int(i)][int(j)].config(bg=color_rojo)
                     except IndexError:
                        print(f"Error: Índice fuera de rango para el pozo {i},{j}. Verifica los datos recibidos.")
                        continue
                  elif estado == 1:
                     try:
                        self.boton[int(i)][int(j)].config(bg=color_verde)
                     except IndexError:
                        print(f"Error: Índice fuera de rango para el pozo {i},{j}. Verifica los datos recibidos.")
                        continue
         
         if (self.tiempo_muerto_1 % 3) == 0:
            puertos_disponibles = [p.device for p in serial.tools.list_ports.comports()]
            if self.puerto_usado in puertos_disponibles:
               self.lb_indicador_conexion.config(fg=color_verde)
            else:
               self.gsm.close()
               self.lb_indicador_conexion.config(fg=color_rojo)'''

   


   ## define un metodo para establece la localizacion mediante google maps
   def localizar(self):
      print("Localizando...")
      #self.tag_1.config(text="Localizando...")
      # URL de Google Maps
      url = 'https://maps.app.goo.gl/XuEL6btjdLmpPGTL9'
      # Abre la URL en el navegador predeterminado
      webbrowser.open(url)
      pass

   ## define un metodo que se ejecuta al pulsar el boton
   def pozo_accion(self, i, j):
       print(f"Hola desde el pozo {i},{j}")
       pass
   
   ## metodo para refrescar los pozos
   def refrescar_pozos(self):
      #resta uno a todos los estados de los pozos
      i = 0
      j = 0
      for i in range(len(self.estados_pozos)):
         if self.estados_pozos[i] > 0:
            self.estados_pozos[i] -= 1
         elif self.estados_pozos[i] == 0:
            try:
               None
              # (i,j) = self.logica_separacion_argunmentos(i+1)
              # self.boton[int(i)][int(j)].config(bg=color_naranja)
            except IndexError:
               print(f"Error: Índice fuera de rango para el pozo {i},{j}. Verifica los datos recibidos.")
               continue

   ## define un metodo que se ejecuta al pulsar el boton de refrescar pozos
   def refrescar_pozos_accion(self):
      print("Refrescando pozos...")
      global tiempo_refresco_pozos
      tiempo_refresco_pozos = self.tiempo_refresco.get()  # Obtiene el valor del tiempo de refresco
      actualizar = [self.tiempo_refresco.get()] * 60  # Crea una lista con el nuevo tiempo de refresco
      self.estados_pozos = actualizar  # Actualiza los estados de los pozos
      pass


   def logica_separacion_argunmentos(self, i):
      j = 1
      try:
         if i == 20 or i == 40 or i == 60:
            j = (i // 20) - 1
            i = 20
         elif i > 0 and i < 60:
            j = 0
            j = i // 20  # Ajusta el índice para la columna
            i = i - j * 20  # Ajusta el índice para la fila
      except ZeroDivisionError:
         print("Error: División por cero al calcular los índices.")
         return (0, 0)
      return (i, j)  # Devuelve los índices ajustados
                     



### Inicia el bucle principal
if __name__ == "__main__":
   terminal = Tk()
   terminal.state('zoomed')  # Maximiza la ventana en Windows
   terminal.geometry(f"{pantalla_ancho}x{pantalla_alto}")#('1366x768')    #('742x535')
   terminal.config(bg='#010808', bd=4)
   terminal.wm_title('Central de pozos - Proyecto SAT')
   terminal.minsize(width=700, height=400)  # Corregido el nombre de 'minisize' a 'minsize'
   terminal.call('wm', 'iconphoto', terminal._w, PhotoImage(file='img1.png'))
   # Usa archivo .ico para que se vea en la barra de tareas de Windows
   #terminal.iconbitmap("icono.ico")

   
   app = Grafica(terminal)  ## crea un elemento de una clase, en esta se establece el bucle que se va seguir
   app.mainloop()    ## ejecuta la funcion de principal de la clase