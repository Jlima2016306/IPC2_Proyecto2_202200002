from drones.nodos.nodosDrones import nodosDrones
import xml.etree.ElementTree as ET
import os

class listDrones:
    def __init__(self):
        self.primero=None
        self.contador_Drones=0
    
    def Incertar_dato(self, Drones):
        nuevo_nodo = nodosDrones(Drones=Drones)
        actual = self.primero
        while actual != None :
            if Drones.nombre == actual.Drones.nombre:
                print ("Ya existe")
                return 
            actual = actual.siguiente        
        if self.primero is None:
            self.primero = nuevo_nodo
            self.contador_Drones += 1
            return
        
        if Drones.nombre < self.primero.Drones.nombre:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
            self.contador_Drones += 1
            return
        
        actual = self.primero
        while actual.siguiente and Drones.nombre >= actual.siguiente.Drones.nombre:
            actual = actual.siguiente
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.contador_Drones += 1

    def recorrer_e_imprimir_lista(self):
        print("Total de senales almacenadas:",self.contador_Drones)
        print("")
        print("")
        print("")
        print("******************************************************************")       
        actual=self.primero
        i=0
        while actual != None:
            
            print("Nombre",actual.Drones.nombre)
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