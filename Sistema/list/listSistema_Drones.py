from Sistema.nodos.nodosSistema_Drones import nodosSistema_Drones
import xml.etree.ElementTree as ET
import os

class listSistema_Drones:
    def __init__(self):
        self.primero=None
        self.contador=0
    
    def Incertar_dato(self,Sistema_Drones):
        if self.primero is None:
            
            self.primero =nodosSistema_Drones(Sistema_Drones=Sistema_Drones)
            self.contador+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente= nodosSistema_Drones(Sistema_Drones=Sistema_Drones)
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
            print("Nombre de sistema:",actual.Sistema_Drones.nombre)
            print("alturaMax:",actual.Sistema_Drones.alturaMax)
            print("cantidad_drones:",actual.Sistema_Drones.cantidad_drones)
            print("+++++++++++++++++++++++++++++++++++")
            actual.Sistema_Drones.listContenido.recorrer_e_imprimir_lista()
            actual= actual.siguiente
        print("******************************************************************")
        print("")
        print("")
        print("")    

    def localizarSistema(self,nombre):
        actual=self.primero
        while actual != None:
            print(actual.Sistema_Drones.nombre + "ddddd" + nombre)
            if(actual.Sistema_Drones.nombre == nombre):
                print("eeee")
                return actual

                break
            actual=actual.siguiente

        return None

    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente