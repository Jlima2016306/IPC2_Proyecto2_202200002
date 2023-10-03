from Sistema.nodos.nodosContenido import nodosContenido
import xml.etree.ElementTree as ET
import os

class listContenido:
    def __init__(self):
        self.primero=None
        self.contador=0
    
    def Incertar_dato(self,Contenido):
        if self.primero is None:
            
            self.primero =nodosContenido(Contenido=Contenido)
            self.contador+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= nodosContenido(Contenido=Contenido)
        self.contador+=1

    def recorrer_e_imprimir_lista(self):

        print("===========================================================================================")
        actual=self.primero
        i=0
        while actual != None:
            
            print("Nombre",actual.Contenido.dron)
            actual.Contenido.listAlturas.recorrer_e_imprimir_lista()
            actual= actual.siguiente
            print("-------------------")
        print("===========================================================================================")
    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente