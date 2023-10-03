from Sistema.nodos.nodosAlturas import nodosAlturas
import xml.etree.ElementTree as ET
import os

class listAlturas:
    def __init__(self):
        self.primero=None
        self.contador=0
    
    def Incertar_dato(self,Alturas):
        if self.primero is None:
            
            self.primero =nodosAlturas(Alturas=Alturas)
            self.contador+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= nodosAlturas(Alturas=Alturas)
        self.contador+=1

    def recorrer_e_imprimir_lista(self):
        print("******************************************************************")       
        actual=self.primero
        i=0
        while actual != None:
            
            print("Metros:",actual.Alturas.metros)
            print("Letra:",actual.Alturas.letra)
            actual= actual.siguiente
            print("---")
        print("******************************************************************")
    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente