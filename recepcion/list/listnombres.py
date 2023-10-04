from recepcion.nodos.nodosnombres import nodonombres
import os

class listnombres:
    def __init__(self):
        self.primero=None
        self.contador_Drones=0
    
    def Incertar_dato(self,Nombres):
        if self.primero is None:
            
            self.primero =nodonombres(Nombres=Nombres)
            self.contador_Drones+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual.siguiente.anterior=actual
            actual = actual.siguiente

        nuevo_nodo = nodonombres(Nombres=Nombres)
        nuevo_nodo.anterior = actual    
        actual.siguiente= nuevo_nodo
        self.contador_Drones+=1

    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente
    def eliminar(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None      