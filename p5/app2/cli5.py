import os, sys, socket

def main():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    s.bind(('localhost', 5000))

   
    s.sendto(b'Hora', ('localhost', 5001))
    
    respuesta, direccion = s.recvfrom(1024)

    os.write(1, (respuesta + b'\n'))

if __name__ == '__main__':
    main()
