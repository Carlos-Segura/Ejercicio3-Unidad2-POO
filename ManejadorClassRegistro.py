from ClassRegistroMeteorologico import Registro

class ManejadorRegistro():
    
    def __init__(self):
        lista = []
        
    def completarLista(self, lista):
        archi = open("Clima.csv","r")
        lector = csv.reader(archi,delimiter=",")
        lista1 = list(lector)
        archi.close()
        for i in lista1:
            lista2 = []
            for j in i:
                registro = (j[0], j[1], j[2])
                lista2.append(j[0], j[1], j[2])
                self.__lista.append(lista2)
