import socket, os, sys, signal, select, hashlib, json

s = None
clientes = []
usuarios_conectados = []
dict_sock_usuario = {}

def finalizar(signal, frame):
    global s
    os.write(2, b'El servidor se cierra\n')
    s.close()
    sys.exit(0)

def main():

    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.bind(('localhost', 5000))
    s.listen(2)
    
    global clientes
    global usuarios_conectados
    global dict_sock_usuario

    if not os.path.exists('usuarios.json'):
        # Si no existe, crear un diccionario vacío
        users = {}
        # Guardar el diccionario en un nuevo archivo json
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
    
    while True:
        s_copia = [s]
        lectura, _, _ = select.select(s_copia, [], [], 0.05)    # Se espera a que haya una nueva conexión
        if s in lectura:    # Si el socket está en la lista de lectura, es porque hay una nueva conexión  
            ns, _ = s.accept()
            clientes.append(ns) # Se añade el nuevo socket a la lista de clientes
            nombre_usuario = ns.recv(1024).decode()
            login_usuario(nombre_usuario, ns)
            print('Usuarios conectados: ' + str(usuarios_conectados))
        clientes_copia = clientes.copy()
        clientes_listos, _, _ = select.select(clientes_copia, [], [], 0.05)  # Se espera a que haya un mensaje de un cliente
        atender_cliente(clientes_listos, dict_sock_usuario)

        signal.signal(signal.SIGINT, finalizar)

def login_usuario(nombre_usuario, ns):
    global usuarios_conectados
    global clientes
    global dict_sock_usuario

    # Comprobamos si el nombre de usuario ya existe 
    print(usuarios_conectados)   
    if nombre_usuario in usuarios_conectados:
        print('mierda')
        ns.send(b'rechazado')
        clientes.remove(ns)
        ns.close()
    else:                   
        ns.send(b'unico')
        contraseña = ns.recv(1024)  # Recibimos la contraseña del cliente
        contra_encriptada = encriptar(contraseña)   # Encriptamos la contraseña
        
        users = obtener_usuarios()  # Registramos en un diccionario los usuarios registrados
        
        if nombre_usuario in users: # Si el usuario ya está registrado
            #Mira si usuario coincide con contraseña_encriptada
            if obtener_contraseña(nombre_usuario) == contra_encriptada : 
                passKey = b'ok'
            else:
                passKey = b'incorrecto'
        else:   # Si el usuario no está registrado, lo añadimos
            añadir_usuario_no_registrado(nombre_usuario, contra_encriptada)
            passKey = b'ok'
        
        if passKey == b'ok': 
            dict_sock_usuario[ns] = nombre_usuario
            usuarios_conectados.append(nombre_usuario)
            print('El usuario ' + nombre_usuario + ' se ha añadido')
            print(usuarios_conectados)
            ns.send(b'correcto')
            for cliente in clientes:
                try:
                    if cliente != ns:
                        mensaje = 'El usuario ' + nombre_usuario + ' se ha conectado'
                        cliente.send(mensaje.encode())
                except BrokenPipeError:
                    print('Error con el socket' + nombre_usuario)
                    clientes.remove(cliente)
                    usuarios_conectados.remove(nombre_usuario)
                    del dict_sock_usuario[cliente]
                    cliente.close()
        else:
            ns.send(b'incorrecto')
            clientes.remove(ns)
            ns.close()
            

# Funcion que obtiene los usuarios registrados           
def obtener_usuarios():    
    with open('usuarios.json', 'r') as f:
        users = json.load(f)    # Cargamos los usuarios del archivo json en un diccionario
    return users

# Funcion que obtiene la contraseña de un usuario
def obtener_contraseña(nombre_usuario):
    with open('usuarios.json', 'r') as f:
        data = json.load(f)

    contraseña = data.get(nombre_usuario, None) # Obtiene el valor (la contraseña) asociado a la clave (el nombre de usuario
    return contraseña

# Funcion que añade un usuario no registrado   
def añadir_usuario_no_registrado(nombre_usuario, contraseña):
    with open('usuarios.json', 'r') as f:
        users = json.load(f)
    users[nombre_usuario] = contraseña  # Añadimos el nuevo usuario con su contraseña al diccionario
    with open('usuarios.json', 'w') as f:
        json.dump(users, f) # Guardamos el diccionario en el archivo json

def encriptar(contraseña):
    hash_obj = hashlib.sha256()
    hash_obj.update(contraseña)
    hash_contraseña = hash_obj.hexdigest()
    return hash_contraseña

def atender_cliente(ns, diccionario):
    global clientes
    global usuarios_conectados

    if ns:  # Si ns no está vacío, es porque hay un mensaje de un cliente
        mensaje_del_cliente = ns[0].recv(1024).decode()
        if mensaje_del_cliente == 'exit':
            nombre_usuario = diccionario[ns[0]]
            usuarios_conectados.remove(nombre_usuario)
            mensaje_salida = 'El usuario ' + nombre_usuario + ' ha salido'
            clientes.remove(ns[0])
            for cliente in clientes:
                cliente.send(mensaje_salida.encode()) 
            #usuarios.remove(nombre_usuario)
            ns[0].close()
            
        else:
            nombre_usuario = diccionario[ns[0]]
            mensaje = nombre_usuario + ' : ' + mensaje_del_cliente

            # Envio por broadcast del mensaje_del_cliente a TODOS los clientes conectados
            for cliente in clientes:
                try:
                    if cliente != ns[0]:
                        cliente.send(mensaje.encode())  
                except BrokenPipeError:
                    print('Error con el socket' + nombre_usuario)
                    clientes.remove(cliente)
                    #usuarios_conectados.remove(nombre_usuario)
                    del diccionario[cliente]
                    cliente.close()

    
if __name__ == '__main__':
    main()