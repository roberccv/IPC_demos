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
        
        gestion_hijo(ns)
        
        signal.signal(signal.SIGINT, finalizar)

def gestion_hijo(ns):
    pid = os.fork()
    if pid == 0:
        ruta = ns.recv(1024)
        os.write(2,b'SErvidor cierra lectura')
        ns.shutdown(socket.SHUT_RD)
        with open(ruta, 'rb') as archivo:
            while True:
                fragmento =  archivo.read(1024)
                if not fragmento:
                    break
                ns.send(fragmento)
            
            
        ns.shutdown(socket.SHUT_WR)
        os.write(2,b'Servidor cierra escritura')


if __name__ == '__main__':
    main()