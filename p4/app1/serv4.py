import os, sys, socket, signal

def main():
    
    ruta = "/tmp/socketP4"
    
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

    if os.path.exists(ruta):
        os.remove(ruta)
        
    s.bind(ruta)
    
    s.listen(2) # Cola baja. Si se llena manda un NACK

    signal.signal(signal.SIGINT, cerrar_servidor)
    
    while True:
        ns, direccion_cliente = s.accept()
        # Direccion cliente es vacía ahora porque es de la misma maquina
        
        os.write(2, b'Conexion aceptada\n')

        atender_cliente(ns)

        #s.close()
        # El servidor no se puede caer cuando un cliente haga un cierre borde

def atender_cliente(ns):
    pid = os.fork()
    if pid == 0:
        ruta_fichero = ns.recv(1024)
        #Cerrar Lectura
        with open(ruta_fichero, 'rb') as archivo: #rb como parametro para que pueda leer binarios
            while True:
                fragmento =  archivo.read(1024)
                if not fragmento:
                    break
                ns.send(fragmento)

        cierre = ns.recv(1024)
        os.write(2, cierre)
        #Solo seria escritura
        if cierre == b"":
            ns.close()
        
        pid_hijo = os.getpid()
        os.kill(pid_hijo, signal.SIGKILL)
    
def cerrar_servidor(signum, frame):
    os.write(2, b'El servidor se cierra\n')
    sys.exit(0)


if __name__ == '__main__':
    main()