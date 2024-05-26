import os, sys, socket, locale, time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    s.bind(('localhost', 5001))

    while True:
        petición, direccion_cli = s.recvfrom(1024)
        mensaje = b'Recibo:' + petición + b'from:' + direccion_cli[0].encode() + b':' + str(direccion_cli[1]).encode()
        os.write(2, mensaje)
        
        if petición == b'Hora':
            hora = obtener_hora()
            s.sendto(hora.encode(), direccion_cli)     

def obtener_hora():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    return time.strftime("%A %d de %B del %Y %H:%M:%S")

if __name__ == '__main__':
    main()