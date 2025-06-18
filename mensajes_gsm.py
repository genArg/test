import serial
import time

# Cambia por el puerto correspondiente a tu sistema
puerto = 'COM11'  # o 'COM3' en Windows
velocidad = 9600

# Inicia la comunicación serial
gsm = serial.Serial(puerto, velocidad, timeout=1)
time.sleep(1)  # Espera un poco para que el módem arranque

def enviar_comando(comando, espera=1):
    gsm.write((comando + '\r').encode())
    time.sleep(espera)
    respuesta = gsm.readlines()
    return [linea.decode(errors='ignore').strip() for linea in respuesta]

# Pone el modo texto
print("Configurando modo texto...")
#print(enviar_comando('AT+CMGF=1'))

# Selecciona la SIM como almacenamiento
print("Usando la memoria de la SIM...")
#print(enviar_comando('AT+CPMS="SM"'))

enviar_comando('AT+CMGD=2', espera=2) # Borra el segundo mensaje (índice 1) de la SIM

if False:
    # Borra todos los mensajes de la SIM
    print("Borrando todos los SMS...")
    respuesta = enviar_comando('AT+CMGDA="DEL ALL"', espera=2) # Borra todos los mensajes

# Lee todos los SMS almacenados
print("Leyendo SMS...")
respuesta = enviar_comando('AT+CMGL="ALL"', espera=2) # Lee todos los mensajes de la SIM

# Muestra los mensajes
for linea in respuesta:
    print(linea)
#print(respuesta)
gsm.close()
