import os
import setproctitle

class cliserv2:

    def crear_procesos(self):
        pid = os.fork()
        if pid == 0:
            setproctitle.setproctitle('cli2')
            print('Proceso cli2 creado con PID:', os.getpid())
        else:
            setproctitle.setproctitle('serv2')
            print('Proceso serv2 creado con PID:', os.getpid())