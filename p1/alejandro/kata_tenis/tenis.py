class Tenis:

    def __init__(self):
        self.jugador1 = 0
        self.jugador2 = 0
    
    def obtener_resultado(self):
        marcador = ''
        puntos_jugador1 = self.jugador1
        puntos_jugador2 = self.jugador2
        son_validos = self.comprobar_validez_puntos(puntos_jugador1, puntos_jugador2)
        if son_validos == False:
            raise ValueError('Los puntos no son validos')
        es_ventaja = self.comprobar_ventaja(puntos_jugador1, puntos_jugador2)
        es_partido_ganado = self.comprobar_partido_ganado(puntos_jugador1, puntos_jugador2)
        if es_partido_ganado == True:
            if puntos_jugador1 > puntos_jugador2:
                marcador = 'Game jugador 1'
            else:
                marcador = 'Game jugador 2'
        elif puntos_jugador1 == puntos_jugador2 and puntos_jugador1 >= 3:
            marcador = 'Deuce'
        elif es_ventaja == True:
            if puntos_jugador1 > puntos_jugador2:
                marcador = 'Advantage jugador 1'
            else:
                marcador = 'Advantage jugador 2'
        else:
            marcador = self.transformar_puntos(puntos_jugador1) + '-' + self.transformar_puntos(puntos_jugador2)
        return marcador
    
    def comprobar_validez_puntos(self, puntos_jugador1, puntos_jugador2):
        if not isinstance(puntos_jugador1, int) or not isinstance(puntos_jugador2, int):
            return False
        if puntos_jugador1 < 0 or puntos_jugador2 < 0:
            return False
        if puntos_jugador1 - puntos_jugador2 > 2 or puntos_jugador2 - puntos_jugador1 > 2:
            if puntos_jugador1 > 4 or puntos_jugador2 > 4:
                return False
        
        return True
    
    def comprobar_ventaja(self, puntos_jugador1, puntos_jugador2):
        if puntos_jugador1 >= 3 and puntos_jugador2 >= 3:
            if puntos_jugador1 - puntos_jugador2 == 1 or puntos_jugador2 - puntos_jugador1 == 1:
                return True
        return False

    def comprobar_partido_ganado(self, puntos_jugador1, puntos_jugador2):
        if puntos_jugador1 >= 4 and puntos_jugador1 - puntos_jugador2 >= 2:
            return True
        elif puntos_jugador2 >= 4 and puntos_jugador2 - puntos_jugador1 >= 2:
            return True
        return False
    
    def transformar_puntos(self, puntos):
        if puntos == 0:
            return 'Love'
        elif puntos == 1:
            return 'Fifteen'
        elif puntos == 2:
            return 'Thirty'
        elif puntos == 3:
            return 'Forty'
