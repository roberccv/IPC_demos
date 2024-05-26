import os, sys, time, locale

a = sys.argv[1]
def main():

    if not os.path.exists("/tmp/fifo_10_serv"):
        os.mkfifo("/tmp/fifo_10_serv")

         
    while True:

        fifo_lectura = os.open("/tmp/fifo_10_serv", os.O_RDONLY)
        mensaje = b''
        while not mensaje.endswith(b'\n'):  # Delimitador de lectura hasta el salto de línea
            mensaje += os.read(fifo_lectura, 1)
        #print(mensaje)
        os.close(fifo_lectura)
        if mensaje == b'hora\n':
            if a == 'si':
                time.sleep(1)
                os.write(2, b'Servidor recibe solicitud de hora\n')
            fifo_escritura = os.open("/tmp/fifo_10_cli", os.O_WRONLY)
            if a == 'si':
                time.sleep(1)
                os.write(2, b'Servidor enviando hora al cliente\n')
            os.write(fifo_escritura, b'fecha: ' + obtener_hora().encode())
            os.close(fifo_escritura)
        

def obtener_hora():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    return time.strftime("%A %d de %B del %Y %H:%M:%S")



if __name__ == "__main__" :
    main()