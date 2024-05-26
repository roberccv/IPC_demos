import socket, os, sys, signal

nombre_usuario = sys.argv[1]
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect(('localhost', 5001))
    s.send(nombre_usuario.encode('utf-8')) 

    confirmacion = s.recv(1024)
    if confirmacion == b'aceptado':  
        pid = os.fork()  
        if pid == 0:
            while True:
                respuesta = s.recv(1024).decode()
                respuesta = respuesta + '\n'
                os.write(1, respuesta.encode())
        else:
            while True:
                mensaje_a_enviar = input()
                s.send(mensaje_a_enviar.encode())
                if mensaje_a_enviar == 'exit':
                    os.kill(pid, signal.SIGTERM)
                    break
    else: 
        os.write(2, b'Nombre de usuario ya existe\n')
        s.close()
        sys.exit(0)
            


if __name__ == '__main__':
    main()