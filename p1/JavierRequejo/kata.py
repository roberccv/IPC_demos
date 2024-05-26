class Partida:

    def puntuacion(tiros):
        score = 0
        for i, tiro in enumerate(tiros):
            if tiro[1] == "/":
                score += 10 
                if i + 1 < len(tiros):
                    score += tiros[i + 1][0]
            elif tiro[0] == "X":
                score += 10
            else:
                score += sum(tiro)
        return score