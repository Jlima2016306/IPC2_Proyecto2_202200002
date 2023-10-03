from Sistema.nodos.nodosListaSistema_Drones import nodosListaSistema_Drones
import xml.etree.ElementTree as ET
import os

class listListaSistema_Drones:
    def __init__(self):
        self.primero=None
        self.contador=0
    
    def Incertar_dato(self,ListaSistema_Drones):
        if self.primero is None:
            
            self.primero =nodosListaSistema_Drones(ListaSistema_Drones=ListaSistema_Drones)
            self.contador+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= nodosListaSistema_Drones(ListaSistema_Drones=ListaSistema_Drones)
        self.contador+=1

    def recorrer_e_imprimir_lista(self):
        print("Total de datos almacenadas:",self.contador)
        print("")
        print("")
        print("")
        print("******************************************************************")       
        actual=self.primero
        i=0
        while actual != None:
            
            print("Nombre",actual.ListaSistema_Drones.nombre)
            actual.ListaSistema_Drones.listListaSistemaDrones.recorrer_e_imprimir_lista()
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