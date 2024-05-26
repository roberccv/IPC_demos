import os, sys, time

a = sys.argv[1]
def main():
    if not os.path.exists("/tmp/fifo_10_cli"):
        os.mkfifo("/tmp/fifo_10_cli")

    m = 0
    while m < 4:    # El bucle sirve para que el cliente haga varias peticiones
        fifo_escritura= os.open("/tmp/fifo_10_serv", os.O_WRONLY)
        if a == 'si':
            #Probar print lento 
            time.sleep(1)
            os.write(2, b'Cliente enviando solicitud de hora\n')
        

        os.write(fifo_escritura, b'hora\n')
            #No lo esta interpretando como 20 peticiones sino como um horahorahorahorahorahora pq es un chorro de bytes
            #por lo que se peta.

        os.close(fifo_escritura)

        fifo_lectura= os.open("/tmp/fifo_10_cli", os.O_RDONLY)
        respuesta = os.read(fifo_lectura, 100) + b'\n'
        if a == 'si':
            time.sleep(1)
            os.write(2, b'Cliente recibe respuesta del servidor\n')
            
        os.write(1, respuesta)

        os.close(fifo_lectura)

        m += 1

if __name__ == "__main__" :
    main()