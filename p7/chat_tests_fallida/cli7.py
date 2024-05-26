import socket, os, sys, signal, getpass
#nombre_usuario = sys.argv[1]
class Cliente():
    #def __init__(self):
       #self.nombre_usuario = sys.argv[1]  

    def main(self, nombre_usuario):

        s = self.crear_y_conectar_socket()
        confirmacion_usuario = self.enviar_nombre_usuario(s, nombre_usuario)
        
        if confirmacion_usuario != b'unico':
            os.write(2, b'Nombre de usuario ya existe\n')
            s.close()
            sys.exit(0)
        
        contraseña = getpass.getpass('Ingrese su contraseña: ')
        
        confirmacion_contraseña = self.enviar_contraseña(s, contraseña)
            
        if confirmacion_contraseña == b'correcto':
            self.comunicacion_servidor(s)
        else:
            texto = "La contraseña no es correcta\n"
            os.write(2, texto.encode())
            s.close()
            sys.exit(0)   
    
    def crear_y_conectar_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.connect(('localhost', 5000))
        return s
    
    def enviar_nombre_usuario(self, s, nombre_usuario):
        s.send(nombre_usuario.encode('utf-8')) 
        confirmacion_usuario = s.recv(1024)
        return confirmacion_usuario

    def enviar_contraseña(self, s, contraseña):
        s.send(contraseña.encode())
        confirmacion_contraseña = s.recv(1024)
        return confirmacion_contraseña

    def comunicacion_servidor(self,s):
        pid = os.fork()  
        if pid == 0:
            while True:
                respuesta = s.recv(1024).decode()
                if respuesta == '':
                    s.close()
                    os.kill(os.getppid(), signal.SIGTERM)
                    sys.exit(0)
                respuesta = respuesta + '\n'
                os.write(1, respuesta.encode())
                        
        else:
            while True:
                mensaje_a_enviar = input()
                s.send(mensaje_a_enviar.encode())
                if mensaje_a_enviar == 'exit':
                    #cerrar también con ctrl+c 
                    s.close()
                    os.kill(pid, signal.SIGTERM)
                    break

