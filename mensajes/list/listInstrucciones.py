from mensajes.nodos.nodosInstrucciones import nodosInstrucciones
import xml.etree.ElementTree as ET
import os

class listInstrucciones:
    def __init__(self):
        self.primero=None
        self.contador=0
    
    def Incertar_dato(self,Instrucciones):
        if self.primero is None:
            
            self.primero =nodosInstrucciones(Instrucciones=Instrucciones)
            self.contador+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= nodosInstrucciones(Instrucciones=Instrucciones)
        self.contador+=1

    def recorrer_e_imprimir_lista(self):
        print("---------------------------------------------------")       
        actual=self.primero
        i=0
        while actual != None:
            print("dron:",actual.Instrucciones.dron)
            print("altura:",actual.Instrucciones.altura)
            actual= actual.siguiente
        print("---------------------------------------------------")

    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente 