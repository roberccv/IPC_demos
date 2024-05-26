class Partida:
    def __init__(self) -> None:
        self.resultados_lanzamientos = []
        self.rondas = []
    
    def crear_partida(self):
        for _ in range(0, 10):
            self.rondas.append([0, 0])

    def jugar_ronda(self, primer_lanzamiento, segundo_lanzamiento):
        if primer_lanzamiento + segundo_lanzamiento > 10:
            raise ValueError("No se pueden tirar más de 10 bolos en una ronda")
        self.rondas.append([primer_lanzamiento, segundo_lanzamiento])
    
    def _calcular_puntos_despues_strike(self, indice_ronda):
        siguientes_bolas = self.rondas[indice_ronda + 1]
        return sum(siguientes_bolas)    
    
    def obtener_puntuacion(self):
        puntuacion_total = 0
        for i, ronda in enumerate(self.rondas):
            puntuacion_total = puntuacion_total + sum(ronda)
            if ronda[0] == 10 and i < 9:
                puntuacion_total = puntuacion_total + self._calcular_puntos_despues_strike(i)
        return puntuacion_total