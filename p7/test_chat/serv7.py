import socket, os, sys, signal, select, hashlib, json

class Servidor():

    def __init__(self):
        self.s = None
        self.clientes = []
        self.usuarios_conectados = []
        self.dict_sock_usuario = {}
        self.clientes_dentro_conexion = []
        self.clientes_sin_autentificacion = []

    def main(self):

        puerto = int(sys.argv[1])
        s = self.s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.bind(('localhost', puerto))
        s.listen(2)
        
        clientes = self.clientes
        usuarios_conectados = self.usuarios_conectados
        dict_sock_usuario = self.dict_sock_usuario
        
        while True:
            try:
                todos = [s]+ clientes
                lectura, _, _ = select.select(todos.copy(), [], [])    # Se espera a que haya una nueva conexión
                if s in lectura:    # Si el socket está en la lista de lectura, es porque hay una nueva conexión  
                    ns, _ = s.accept()
                    clientes.append(ns) # Se añade el nuevo socket a la lista de clientes
                else:
                    self.atender_cliente(lectura, dict_sock_usuario)
            except KeyboardInterrupt:
                
                os.write(2, b'El servidor se cierra\n')
                s.close()
                for sock in clientes:
                    sock.close()
                sys.exit(0)
            

            

    def login_usuario(self, nombre_usuario, ns):
        usuarios_conectados = self.usuarios_conectados
        clientes = self.clientes
        dict_sock_usuario = self.dict_sock_usuario

        # Comprobamos si el nombre de usuario ya existe
        esta_usuario_conectado = self.comprobar_usuarios_conectados(nombre_usuario)     
        
        if esta_usuario_conectado == True:
            ns.send(b'rechazado')
            clientes.remove(ns)
            ns.close()
        else:                   
            ns.send(b'unico')
            dict_sock_usuario[ns] = nombre_usuario


    def login_usuario_2(self, ns):
        usuarios_conectados = self.usuarios_conectados
        clientes = self.clientes
        dict_sock_usuario = self.dict_sock_usuario
        clientes_dentro_conexion = self.clientes_dentro_conexion

        nombre_usuario = dict_sock_usuario[ns]
        contraseña = ns.recv(1024)  # Recibimos la contraseña del cliente    
        passKey = self.gestionar_usuario(nombre_usuario, contraseña)
        
        if passKey == b'ok': 
            usuarios_conectados.append(nombre_usuario)
            ns.send(b'correcto')
            for cliente in clientes_dentro_conexion:
                if cliente != ns:
                    mensaje = 'El usuario ' + nombre_usuario + ' se ha conectado'
                    cliente.send(mensaje.encode())
        else:
            ns.send(b'incorrecto')
            clientes.remove(ns)
            #Borrar de diccionario
            ns.close()

    def comprobar_usuarios_conectados(self, nombre_usuario):
        if nombre_usuario in self.usuarios_conectados: True

    def comprobar_contraseña_es_correcta(self, nombre_usuario, contraseña):
        contra_encriptada = self.encriptar(contraseña)   # Encriptamos la contraseña
        if self.obtener_contraseña(nombre_usuario) == contra_encriptada :
            return b'ok' 
            
        else:
            return b'incorrecto'
        
    def gestionar_usuario(self, nombre_usuario, contraseña): #nombre fatal
        users = self.obtener_usuarios()  # Devuelve usuarios del archivo json
        if nombre_usuario in users: # Si el usuario ya está registrado
            #Mira si usuario coincide con contraseña_encriptada
            return self.comprobar_contraseña_es_correcta(nombre_usuario, contraseña)
        else:   # Si el usuario no está registrado, lo añadimos
            self.añadir_usuario_no_registrado(nombre_usuario, contraseña)
            return b'ok'
    # Funcion que obtiene los usuarios registrados   
            
    def obtener_usuarios(self):    
        with open('usuarios.json', 'r') as f:
            users = json.load(f)    # Cargamos los usuarios del archivo json en un diccionario
        return users

    # Funcion que obtiene la contraseña de un usuario
    def obtener_contraseña(self, nombre_usuario):
        with open('usuarios.json', 'r') as f:
            data = json.load(f)

        contraseña = data.get(nombre_usuario, None) # Obtiene el valor (la contraseña) asociado a la clave (el nombre de usuario
        return contraseña

    # Funcion que añade un usuario no registrado   
    def añadir_usuario_no_registrado(self, nombre_usuario, contraseña):
        contra_encriptada = self.encriptar(contraseña)   # Encriptamos la contraseña
        #self.crear_json_si_no_existe()

        try: 
            with open('usuarios.json', 'r') as f:
                users = json.load(f)
        except:
            users = {}
        users[nombre_usuario] = contra_encriptada  # Añadimos el nuevo usuario con su contraseña al diccionario
        with open('usuarios.json', 'w') as f:
            json.dump(users, f) # Guardamos el diccionario en el archivo json

    def encriptar(self, contraseña):
        hash_obj = hashlib.sha256()
        hash_obj.update(contraseña)
        hash_contraseña = hash_obj.hexdigest()
        return hash_contraseña
    

    def crear_json_si_no_existe(self):
        if not os.path.exists('usuarios.json'):
            # Si no existe, crear un diccionario vacío
            users = {}
            # Guardar el diccionario en un nuevo archivo json
            with open('usuarios.json', 'w') as f:
                json.dump(users, f)

    def atender_cliente(self, ns, diccionario):
        clientes = self.clientes
        usuarios_conectados = self.usuarios_conectados
        clientes_dentro_conexion = self.clientes_dentro_conexion
        clientes_sin_autentificacion = self.clientes_sin_autentificacion

        if ns:  # Si ns no está vacío, es porque hay un mensaje de un cliente
            if ns[0] in clientes_dentro_conexion:
                
                mensaje_del_cliente = ns[0].recv(1024).decode()
                if mensaje_del_cliente == 'exit':
                    nombre_usuario = diccionario[ns[0]]
                    usuarios_conectados.remove(nombre_usuario)
                    clientes_dentro_conexion.remove(ns[0])
                    mensaje_salida = 'El usuario ' + nombre_usuario + ' ha salido'
                    clientes.remove(ns[0])
                    #clientes_dentro_conexion.remove(ns[0])
                    for cliente in clientes_dentro_conexion:
                        cliente.send(mensaje_salida.encode()) 
                    #usuarios.remove(nombre_usuario)
                    ns[0].close()
                    
                else:
                    nombre_usuario = diccionario[ns[0]]
                    mensaje = nombre_usuario + ' : ' + mensaje_del_cliente

                    # Envio por broadcast del mensaje_del_cliente a TODOS los clientes conectados
                    for cliente in clientes_dentro_conexion:
                        if cliente != ns[0]:
                            cliente.send(mensaje.encode())
            elif ns[0] in clientes_sin_autentificacion:
                clientes_sin_autentificacion.remove(ns[0])
                self.login_usuario_2(ns[0])
                clientes_dentro_conexion.append(ns[0])
            
            else:
                nombre_usuario = ns[0].recv(1024).decode()
                self.login_usuario(nombre_usuario, ns[0])
                clientes_sin_autentificacion.append(ns[0])

            

 
    
if __name__ == '__main__':
    servidor = Servidor()
    servidor.crear_json_si_no_existe()
    servidor.main()