class bolos:

    def calculadora(self, bolas):
        if not self.formatoCorrecto(bolas):
            raise Exception("El formato de las bolas no es correcto")
        elif  self.tamañoCorrecto(bolas) == "False": raise Exception("El tamaño de la lista no es correcto")
        elif(not self.contienePleno(bolas) and not self.contieneSpare(bolas)):
            #Caso normal, ni plenos ni spares
            p = sum(bolas)
            return p
        elif(self.contienePleno(bolas)):
            #and not self.contieneSpare(bolas)
            #if(bolas[bolas.index(10) + 1] != 0):
            #    raise Exception("La bola siguiente a un pleno no puede ser distinta de 0")
            #bolas = self.aumentarPuntuacionPleno(bolas)
            #print(bolas)
            #Añade un 0 despues del 10
            #posicionPleno = bolas.index(10)
            #puntuacionPlenoSumar = bolas[posicionPleno + 1] + bolas[posicionPleno + 2]
            m = sum(self.listaSumarASpar(bolas))
            if self.tamañoCorrecto(bolas) == "no bonus":
                p = sum(self.listaSumarAPleno(bolas)) + sum(bolas) + m
            elif self.tamañoCorrecto(bolas)== "pleno final" : 
                p = (sum(self.listaSumarAPleno(bolas)) + sum(bolas) - bolas[-1] -bolas[-2]) + m 
            elif self.tamañoCorrecto(bolas)== "2 bonus":
                p = (sum(self.listaSumarAPleno(bolas)) + sum(bolas) - bolas[-1] - bolas[-2]) + m
            elif self.tamañoCorrecto(bolas) == "spar final":
                p = p = (sum(self.listaSumarAPleno(bolas)) + sum(bolas) - bolas[-1]) + m
                
        
        elif self.contieneSpare(bolas) and not self.contienePleno(bolas):
            p = sum(bolas[0:20]) + sum(self.listaSumarASpar(bolas))
        return p 
        
    def listaSumarASpar(self, bolas):
        bolas0 = []
        for a in bolas:
            bolas0.append(a)

        bolasN = self.aumentarPuntuacionPleno(bolas0)
        n = 0
        m = []
        for a in bolasN:
            if (n % 2 == 0) and (n+2 <= len(bolasN)) and (bolasN[n]+bolasN[n+1] == 10) and (bolasN[n] != 10) and (bolasN[n+1] != 10) :
                m.append(bolasN[n+2])
            n = n+1
        return m

    def formatoCorrecto(self, bolas):
        if isinstance(bolas, list) == False:
            return False
        for a in bolas:
            if (type(a) != int) or (a < 0) or (a > 10):
                return False
        return True
    
    def listaSumarAPleno(self, bolas):
        m = []
        n = 0
        for a in bolas:
            if (a == 10 and (n +3 <= len(bolas))):
                #si no hay 2 bolas despues del pleno, es un pleno final con bonus por lo que no hay que buscar una puntuación que sumarle
                #Como añade el segundo bonus, se lo podemos quitar al total arriba
                m.append(bolas[n+1])
                m.append(bolas[n+2])
            n = n + 1
        return m
    
    
    def aumentarPuntuacionPleno(self, bolas):
        n = 0
        for a in bolas:
            if (a == 10):
                bolas.insert(n + 1, 0)
            n = n + 1
        return bolas
    
#    def tamañoCorrecto(self, bolas):
#        tamaño = 20
#        for a in bolas:
#            if(a == 10):  
#                tamaño = tamaño - 1

        #if bolas[-3]== 10: tamaño = tamaño +2
#        return tamaño == len(bolas)

    def tamañoCorrecto(self, bolas):
        m = []
        for a in bolas:
            m.append(a)
        #Si utilizaba la lista bolas me la modificaba, y solo queria la modificación para el calculo de dimensión 
        #PREGUNTAR
        bolasA = self.aumentarPuntuacionPleno(m)
        if len(bolasA) == 20:
            return "no bonus"
        elif (len(bolasA) == 22 and bolasA[-3] == 0):
            return "pleno final"
        elif (len(bolasA) == 24 or len(bolasA) == 23 and (bolasA[-1] == 0) or bolasA[-2] == 0):
            return "2 bonus"
        elif (len(bolasA) == 21 and (bolas[-3]+ bolasA[-2] ==10)):
            return "spar final"
        else:
            return "False"
            

            
                   

    def contienePleno(self, bolas):
        a = 10 in bolas
        return a        

    def contieneSpare(self, bolas):
        n = 0
        for a in bolas:
            if (n % 2 == 0) and (n+2 <= len(bolas)) and (bolas[n]+bolas[n+1] == 10):
                return True
            n = n+1
        
            
    
    