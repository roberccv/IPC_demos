class Romanos:
  
    def convertir(self, numero_arabigo):
        if not isinstance(numero_arabigo, int):
            raise ValueError("El número debe ser un entero")
        if numero_arabigo <= 0:
            raise ValueError("El número debe ser mayor a 0")
        numero_romano = ""
        for i in range(numero_arabigo):
            numero_romano = numero_romano + "I"
        for i in range(numero_arabigo // 5):
            numero_romano = numero_romano.replace("IIIII", "V")
        for i in range(numero_arabigo // 10):
            numero_romano = numero_romano.replace("VV", "X")
        for i in range(numero_arabigo // 50):
            numero_romano = numero_romano.replace("XXXXX", "L")
        for i in range(numero_arabigo // 100):
            numero_romano = numero_romano.replace("LL", "C")
        for i in range(numero_arabigo // 500):
            numero_romano = numero_romano.replace("CCCCC", "D")
        for i in range(numero_arabigo // 1000):
            numero_romano = numero_romano.replace("DD", "M")
        
        if numero_romano.find("VIIII") != -1:
            numero_romano = numero_romano.replace("VIIII", "IX")      
        if numero_romano.find("IIII") != -1:
            numero_romano = numero_romano.replace("IIII", "IV")
        if numero_romano.find("XXXX") != -1:
            numero_romano = numero_romano.replace("XXXX", "XL")
        if numero_romano.find("LXL") != -1:
            numero_romano = numero_romano.replace("LXL", "XC")
        if numero_romano.find("CCCC") != -1:
            numero_romano = numero_romano.replace("CCCC", "CD")
        if numero_romano.find("DCD") != -1:
            numero_romano = numero_romano.replace("DCD", "CM")
            
        return numero_romano
     