class Partida:
    
    def __init__(self):
        self.rondas = []
    
    def crear_partida(self, rondas):
        if len(rondas) != 10:
            raise ValueError("Una partida tiene exactamente 10 rondas")
        for i in range(len(rondas)):
            ronda = rondas[i]
            for lanzamiento in ronda:
                if not isinstance(lanzamiento, int):
                    raise ValueError("Este lanzamiento no es un numero entero")            
            if(sum(ronda) > 10) and i != 9:
                raise ValueError("En una ronda no pueden tirarse mas de 10 bolos")
            if len(ronda) == 1 and ronda[0] != 10:
                raise ValueError("No puede haber lanzamientos vacios que no sean strikes")
            self.rondas.append(ronda)

    def obtener_puntuacion(self):
        rondas = self.rondas
        puntuacion = 0
        for i in range(len(rondas)):
            print(puntuacion, "antes de la ronda", i)
            ronda = rondas[i]
            puntuacion = sum(ronda) + puntuacion
            print(puntuacion)
            if ronda[0] == 10 and i != 9 and i != 8:  # CASO DEL STRIKE
                print("strike en ronda normal")
                siguiente_ronda = rondas[i + 1]               
                if siguiente_ronda[0] == 10 and i != 8:
                    puntuacion = puntuacion + 10 
                puntuacion = sum(siguiente_ronda) + puntuacion
            elif ronda[0] == 10 and i != 9 and i == 8:  # CASO DEL STRIKE EN LA PENULTIMA RONDA
                siguiente_ronda = rondas[i + 1] 
                if sum(siguiente_ronda) >= 10:
                    puntuacion = puntuacion - siguiente_ronda[2]              
                if (siguiente_ronda[0] == 10 and siguiente_ronda[1] == 10):
                    print("entra")
                    #puntuacion = puntuacion - 10 
                print("entra")
                puntuacion = sum(siguiente_ronda) + puntuacion
            elif ronda[0] == 10 and i == 9 and ronda[1] != 10: # CASO DEL STRIKE EN LA ULTIMA RONDA
                print("strike en la ultima ronda")
                puntuacion = ronda[1] + ronda[2] + puntuacion 
            elif ronda[0] == 10 and i == 9 and ronda[1] == 10 and ronda[2] == 10:
                print("doble strike en la ultima ronda")              
            elif ronda[0] != 10 and sum(ronda) >= 10:   # CASO DEL SPARE
                print(puntuacion)
                print("spare en ronda normal")
                if (i != 9):    # CASO DEL SPARE EN RONDAS NORMALES
                    siguiente_ronda = rondas[i + 1]
                    for j in range(len(ronda)):
                        if j == 0: 
                        # Se suma el primer lanzamiento de la siguiente tirada
                            puntuacion = siguiente_ronda[0] + puntuacion
                if i == 9:   # CASO DEL SPARE EN LA ULTIMA RONDA
                    print("spare en ronda ultima")
                    print(ronda[2])
                    print(puntuacion)
                    puntuacion = ronda[2] + puntuacion
                    ronda_previa = rondas[i - 1]
                    if sum(ronda_previa) >= 10:
                        puntuacion = puntuacion - ronda[2]
        return puntuacion
    
