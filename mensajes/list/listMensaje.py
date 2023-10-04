from mensajes.nodos.nodosMensaje import nodosMensaje
import xml.etree.ElementTree as ET
import os
from Sistema.list.listSistema_Drones import listSistema_Drones
class listMensaje:
    def __init__(self):
        self.primero=None
        self.contador=0
        self.temporalSD = listSistema_Drones()
    


    def Incertar_dato(self, Mensaje):
        nuevo_nodo = nodosMensaje(Mensaje=Mensaje)
        actual = self.primero
        while actual != None :
            if Mensaje.nombre == actual.Mensaje.nombre:
                print ("Ya existe")
                return 
            actual = actual.siguiente           
        if self.primero is None:
            self.primero = nuevo_nodo
            self.contador += 1
            return
        
        if Mensaje.nombre < self.primero.Mensaje.nombre:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
            self.contador += 1
            return
        
        actual = self.primero
        while actual.siguiente and Mensaje.nombre >= actual.siguiente.Mensaje.nombre:
            actual = actual.siguiente
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self.contador += 1


    def recorrer_e_imprimir_lista(self):
        print("Total de datos almacenadas:",self.contador)
        print("")
        print("")
        print("")
        print("******************************************************************")       
        actual=self.primero
        i=0
        while actual != None:
            print("Nombre de sistema:",actual.Mensaje.nombre)
            print("sistemaDrones:",actual.Mensaje.sistemaDrones)
            print("+++++++++++++++++++++++++++++++++++")
            actual.Mensaje.listInstrucciones.recorrer_e_imprimir_lista()
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
    def eliminar(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None              