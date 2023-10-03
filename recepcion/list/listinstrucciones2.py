from recepcion.nodos.nodosinstrucciones2 import nodosinstrucciones2
import xml.etree.ElementTree as ET
import os

class listinstrucciones2:
    def __init__(self):
        self.primero=None
        self.contador_Drones=0
    
    def Incertar_dato(self,instrucciones2):
        if self.primero is None:
            
            self.primero =nodosinstrucciones2(instrucciones2=instrucciones2)
            self.contador_Drones+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= nodosinstrucciones2(instrucciones2=instrucciones2)
        self.contador_Drones+=1

    def recorrer_e_imprimir_lista(self):
        print("")
        print("")
        print("")
        print("******************************************************************")       
        actual=self.primero
        i=0
        while actual != None:
            
            print("Tiempo",actual.instrucciones2.tiempo)
            actual.instrucciones2.lista_acciones.recorrer_e_imprimir_lista()
            actual= actual.siguiente
        print("******************************************************************")
        print("")
        print("")
        print("")    
    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente
    