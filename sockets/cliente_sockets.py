import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crear objeto - direccion IP y puerto
s.bind(('localhost', 12345))    #Twopla- Asociar la direccion y puerto - configuracion  en el mismo computador la direccion o local host 127.0.0.1
s.listen() #escuchar conexiones de clientes entrantes

while True:
    try: #captura error
         print('Waiting...')
         client, address = s.accept() #se queda aca hasta que halla conexion / se conecte un cliente
         print('Client Connected') #solo se ejecuta esta linea cuando se conecta un cliente

    except KeyboardInterrupt: #detiene el proceso - igual a ctrl c que interrumpe
         break
    
print('End server')


x ="1"
s ="2"