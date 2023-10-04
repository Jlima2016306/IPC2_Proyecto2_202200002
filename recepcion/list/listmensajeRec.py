from recepcion.nodos.nodosmensajeRec import nodosmensajeRec
import xml.etree.ElementTree as ET
import os

class listmensajeRec:
    def __init__(self):
        self.primero=None
        self.contador_Drones=0
    

    def Incertar_dato(self, mensajeRec):
        nuevo_nodo = nodosmensajeRec(mensajeRec=mensajeRec)
        actual = self.primero
        while actual != None :
            if mensajeRec.nombre == actual.mensajeRec.nombre:
                print ("Ya existe")
                return 
            actual = actual.siguiente        
        if self.primero is None:
            self.primero = nuevo_nodo
            self.contador_Drones += 1
            return
        
        if mensajeRec.nombre < self.primero.mensajeRec.nombre:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
            self.contador_Drones += 1
            return
        
        actual = self.primero
        while actual.siguiente and mensajeRec.nombre >= actual.siguiente.mensajeRec.nombre:
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
            
            print("Nombre",actual.mensajeRec.nombre)
            print("Sistema de drones",actual.mensajeRec.sitema_drones)
            print("Tiempo Optimo",actual.mensajeRec.tiempo)
            print("mensaje",actual.mensajeRec.mensaje)
            actual.mensajeRec.lista_instrucciones2.recorrer_e_imprimir_lista()

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