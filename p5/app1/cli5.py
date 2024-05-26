import os, sys, socket

ruta = sys.argv[1]

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    s.bind(('localhost', 5000))


    s.sendto(ruta.encode(), ('localhost', 5001))

    while True:
        respuesta, direccion = s.recvfrom(1024)
        if len(respuesta) < 1024:
            os.write(1, respuesta)
            break
        else:
            os.write(1,respuesta)
    

if __name__ == '__main__':
    main()
           
