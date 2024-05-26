import os, sys, socket, time

ruta = sys.argv[1]

def main():
    
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
    
    s.connect("/tmp/socketP4")
    s.send(ruta.encode())

    #s.shutdown(socket.SHUT_WR)
    while True:
        respuesta = s.recv(1024)
        if len(respuesta) < 1024:
            os.write(1, respuesta)
            break
        else:
            os.write(1,respuesta)

    #s.shutdown(socket.SHUT_RD)
    s.shutdown(socket.SHUT_RDWR)
    #s.close()    

if __name__ == '__main__':
    main()