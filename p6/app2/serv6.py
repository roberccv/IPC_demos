import socket, os, sys, locale, time, signal

s = None
def finalizar(signal, frame):
    global s
    os.write(2, b'El servidor se cierra\n')
    s.close()
    sys.exit(0)


def main():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    
    s.bind(('localhost', 5000))

    s.listen(2)

    while True:
        ns, dir_cliente = s.accept()
        print(dir_cliente)

        ns.recv(1024)
        ns.shutdown(socket.SHUT_RD)
        os.write(2,b'SErvidor cierra lectura')
        os.write(2, b'Peticion recibida por el cliente')

        hora = obtener_hora()
        ns.send(hora.encode())
        ns.shutdown(socket.SHUT_WR)
        os.write(2,b'Servidor cierra escritura')
        signal.signal(signal.SIGINT, finalizar)


def obtener_hora():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    return time.strftime("%A %d de %B del %Y %H:%M:%S")

if __name__ == '__main__':
    main()