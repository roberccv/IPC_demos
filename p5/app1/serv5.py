import os, sys, socket, locale, time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    s.bind(('localhost', 5001))

    while True:
        ruta, direccion_cli = s.recvfrom(1024)

        os.write(2, b'Envio del fichero')
        with open(ruta, 'rb') as archivo: 
            while True:
                fragmento =  archivo.read(1024)
                if not fragmento:
                    break
                s.sendto(fragmento, direccion_cli)

if __name__ == '__main__':
    main()

