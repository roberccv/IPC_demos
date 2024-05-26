import socket, os, sys, signal
from multiprocessing import Manager
s = None
#clientes = []

def finalizar(signal, frame):
    global s
    os.write(2, b'El servidor se cierra\n')
    s.close()
    sys.exit(0)

def main():

    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.bind(('localhost', 5001))

    s.listen(2)
    with Manager() as manager:
        clientes = manager.list()
        usuarios = manager.list()
        while True: 
            ns, dir_cliente = s.accept()
            clientes.append(ns)

            atender_cliente(ns, clientes, usuarios)

            signal.signal(signal.SIGINT, finalizar)
        


def atender_cliente(ns, clientes, usuarios):
    pid = os.fork()
    if pid == 0:
        nombre_usuario = ns.recv(1024).decode()
        if nombre_usuario in usuarios:
            ns.send(b'rechazado')
            ns.close()
            sys.exit(0)
        
        usuarios.append(nombre_usuario)
        ns.send(b'aceptado')

        while True:
            mensaje_del_cliente = ns.recv(1024).decode()
            if mensaje_del_cliente == 'exit':
                clientes.remove(ns)
                ns.close()
                break

            mensaje = nombre_usuario + ' : ' + mensaje_del_cliente

            for cliente in clientes:
                cliente.send(mensaje.encode())  
            #Broadcast

    
if __name__ == '__main__':
    main()