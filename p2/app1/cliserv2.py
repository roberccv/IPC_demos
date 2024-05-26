import os, sys

def main():
    rd_s, wd_c = os.pipe()    # Pipe hijo escribe - padre lee
    rd_c, wd_s = os.pipe()    # Pipe padre escribe - hijo lee

    rs, wc = os.fdopen(rd_s, 'r'), os.fdopen(wd_c, 'w')
    rc, ws = os.fdopen(rd_c, 'rb'), os.fdopen(wd_s, 'wb')
    ruta = sys.argv[1]

    pid = os.fork() 
    
    if pid == 0:    # Estamos en el cliente
            frase_debug1 = b'Proceso cli2 creado con PID: ' + str(os.getpid()).encode() + b'\n'
            #os.write() espera una cadena de bytes por lo que se debe codificar la cadena, para ello usamos .encode() y la b delante que indica cadena bytes
            os.write(2, frase_debug1)
            
            rs.close()  # Cierro la tubería de lectura del servidor
            ws.close()  # Cierro la tubería de escritura del servidor
            wc.write(ruta)  # Escribimos la ruta en la tubería cliente -> servidor
            wc.close() # Cierro la tubería de escritura del cliente

            solucion = rc.read()    # Leemos la solución desde la tubería servidor -> cliente
            #preguntar pq no sobreesvribe y si esta escuchando todo el rato
            os.write(1, solucion)  # Escribimos la solución en la salida estándar
            rc.close()
            
    else:   # Estamos en el servidor
            
            frase_debug2 = b'Proceso serv2 creado con PID: ' + str(os.getpid()).encode() + b'\n'
            os.write(2, frase_debug2)

            rc.close() # Cierro la tubería de lectura del cliente
            wc.close ()  # Cierro la tubería de escritura del cliente
            nueva_ruta = rs.readline()    # Leemos la ruta desde la tubería cliente -> servidor
            rs.close()
            with open(nueva_ruta, 'rb') as archivo: #rb como parametro para que pueda leer binarios
                 while True:
                    fragmento =  archivo.read(4096)
                    if not fragmento:
                         break
                    ws.write(fragmento) # Escribimos en la tubería servidor -> cliente fragmento a fragmento (por el tamaño del buffer)
                    
            ws.close() 
     
if __name__ == '__main__':
    main()