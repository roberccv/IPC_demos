import socket, os, sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    ruta = sys.argv[1]
    s.connect(('localhost', 5000))
    
    s.send(ruta.encode())
    s.shutdown(socket.SHUT_WR)
    os.write(2,b'Cliente cierra escritura')

    #s.shutdown(socket.SHUT_WR)
    while True:
        respuesta = s.recv(1024)
        if len(respuesta) < 1024:
            os.write(1, respuesta)
            break
        else:
            os.write(1,respuesta)
    
    os.write(2,b'Cliente cierra lectura')
    s.close()
    

    
if __name__ == '__main__':
    main()
    