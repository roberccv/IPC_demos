import socket, os, sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    
    s.connect(('localhost', 5000))

    s.send(b'Hora \n')
    s.shutdown(socket.SHUT_WR)
    os.write(2,b'Cliente cierra escritura')

    hora = s.recv(1024)
    #s.shutdown(socket.SHUT_RD)
    s.close()
    os.write(2,b'Cliente cierra lectura')

    os.write(1, hora)


if __name__ == '__main__':
    main()
    