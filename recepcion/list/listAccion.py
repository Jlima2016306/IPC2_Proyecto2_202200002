from recepcion.nodos.nodosAccion import nodosAccion
import xml.etree.ElementTree as ET
import os
from recepcion.clase.Accion import Accion
from recepcion.clase.nombres import Nombres
from recepcion.list.listnombres import listnombres
class listAccion:
    def __init__(self):
        self.primero=None
        self.contador_Drones=0
    
    def Incertar_dato(self,Accion):
        if self.primero is None:
            
            self.primero =nodosAccion(Accion=Accion)
            self.contador_Drones+=1
            return
        actual = self.primero
        while actual.siguiente:
            actual.siguiente.anterior=actual
            actual = actual.siguiente

        nuevo_nodo = nodosAccion(Accion=Accion)
        nuevo_nodo.anterior = actual    
        actual.siguiente= nuevo_nodo
        self.contador_Drones+=1

    def recorrer_e_imprimir_lista(self):

        print("---------------------------------------------")
        actual=self.primero
        i=0
        while actual != None:
            
            print("Nombre:",actual.Accion.dron+"  Accion:"+actual.Accion.accion+"  tiempo:"+ str(actual.Accion.posicion))
            actual= actual.siguiente
        print("---------------------------------------------")

    def recorrer_e_imprimir_listaTipo_2(self):

        print("---------------------------------------------")
        nombreImpresos = listnombres()
        actual=self.primero
        i=1
        numero=0
        llave=True
        
        while actual!= None:
            llave=True
            for casa in nombreImpresos:
                if(casa.Nombres.nombres == actual.Accion.dron):
                     llave = False
                     break
                else:
                     llave = True


            if(llave):
                                nuevo = Nombres(actual.Accion.dron)
                                nombreImpresos.Incertar_dato(nuevo)
                                
    
            actual = actual.siguiente   

        txt = "N/"

        for casa in nombreImpresos:
                print("Dron:",casa.Nombres.nombres)
                octo = self.primero
                while octo!=None:
                         if(octo.Accion.dron == casa.Nombres.nombres):
                            print("    Accion:",octo.Accion.accion,"Tiempo:",octo.Accion.posicion)
                         octo = octo.siguiente
                txt = txt+"/"+casa.Nombres.nombres
        print(txt)
        actual=self.primero
        i=1
        numero=0
        while actual!= None:
            
            if(actual.Accion.posicion>numero):
                        numero = actual.Accion.posicion
            actual = actual.siguiente            
        h =0
        for i in range(numero):
            h+=1
            text=str(h)+" / "
            
            for casa in nombreImpresos:
                actual =self.primero
                while actual!=None:  
                        if(h==actual.Accion.posicion and actual.Accion.dron == casa.Nombres.nombres ):
                            text=text+" / "+actual.Accion.accion
                        actual=actual.siguiente       

            print(text)



        print("---------------------------------------------")        

    def devolverNumeroMax(self):
        actual=self.primero
        i=1
        numero=0
        while actual!= None:
            
            if(actual.Accion.posicion>numero):
                        numero = actual.Accion.posicion
            actual = actual.siguiente   

        return numero            

    def devolverNombres(self):
        nombreImpresos = listnombres()
        actual=self.primero
        i=1
        numero=0
        llave=True
        
        while actual!= None:
            llave=True
            for casa in nombreImpresos:
                if(casa.Nombres.nombres == actual.Accion.dron):
                     llave = False
                     break
                else:
                     llave = True


            if(llave):
                                nuevo = Nombres(actual.Accion.dron)
                                nombreImpresos.Incertar_dato(nuevo)
    
            actual = actual.siguiente   



        txt = "N/"
        for casa in nombreImpresos:
                txt = txt+"/"+casa.Nombres.nombres
        print(txt)
        return nombreImpresos

    def buscarDronUltimo(self):
        actual = self.primero
        ultimo_dron = None
        anterio = None
        while actual != None:
            anterio = actual
            actual= actual.siguiente
        actual = anterio
        n=0
        while actual != None:
            ultimo_dron = actual
            if(anterio != None and ultimo_dron.anterior != None):
                if anterio.Accion.dron == ultimo_dron.anterior.Accion.dron :
             
                            
                        anterio.Accion.posicion = ultimo_dron.anterior.Accion.posicion #quiero hheredar la posicion del pennultimoo al ultimo
                        return anterio
            actual = actual.anterior  # Retrocede al nodo anterior


        return anterio
    

    def devolverUltimo(sefl):

        actual = sefl.primero
        ultimo_dron = None

        while actual != None:
            ultimo_dron = actual
            actual= actual.siguiente        
        return ultimo_dron

    def afirmativoEstaFuncionNosDaraElganeTODOoNADAAAAAAAAAAA(self,dron):

        actual = self.primero
        ultimo_dron = None
        captador = None
        while actual != None:
            ultimo_dron = actual
            if(ultimo_dron.Accion.dron ==dron):
                captador = ultimo_dron.Accion
            actual= actual.siguiente 
        if(captador == None):
            captador=Accion(dron,"prender Luz",1)


        if(ultimo_dron):    
            actual = ultimo_dron
            

            while actual!= None:
                if(captador.dron != actual.Accion.dron and actual.Accion.accion == "prender Luz" and captador.posicion+1 == actual.Accion.posicion):
                    return "esperar"

                actual = actual.anterior
        
            if(ultimo_dron.Accion.accion == "prender Luz" and ultimo_dron.Accion.posicion == 1 and ultimo_dron.anterior==None): 
                return "esperar"

        return "prender Luz"
    
        
    def CualEsTuTiempoBro(self,dron):
        actual = self.primero
        ultimo_dron = None        
        while actual != None:
            ultimo_dron = actual
            actual= actual.siguiente
        if(ultimo_dron):    
            actual = ultimo_dron

            while actual!= None:
                if(actual.Accion.dron == dron ):
                    return actual.Accion.posicion
                actual = actual.anterior
        

        return 0                
    
    def devolverSubir(self):
        actual = self.primero
        ultimo_dron = None

        while actual != None:
            ultimo_dron = actual
            actual= actual.siguiente 

        ultimo_dron.Accion.accion ="Subir"
        ultimo_dron.Accion.posicion =ultimo_dron.Accion.posicion + 1
        return ultimo_dron        

    def devolverbajar(self):
        actual = self.primero
        ultimo_dron = None

        while actual != None:
            ultimo_dron = actual
            actual= actual.siguiente 

        ultimo_dron.Accion.accion ="Bajar"
        ultimo_dron.Accion.posicion =ultimo_dron.Accion.posicion - 1
        return ultimo_dron       

    def devolverLuz(self):
        actual = self.primero
        ultimo_dron = None

        while actual != None:
            ultimo_dron = actual
            actual= actual.siguiente 

        ultimo_dron.Accion.accion ="prender Luz"
        return ultimo_dron  
         
    def devolverEsperar(self):
        actual = self.primero
        ultimo_dron = None

        while actual != None:
            ultimo_dron = actual
            actual= actual.siguiente 

        ultimo_dron.Accion.accion ="esperar"
        return ultimo_dron    
    def alarma(self):
        actual = self.primero
        ultimo_dron = None

        while actual != None:
            if actual.Accion.accion =="prender Luz":
                print ("the time is here")
            ultimo_dron = actual
            actual= actual.siguiente 

        return ultimo_dron       
    def __iter__(self):
        # Devuelve un iterador que recorre la lista
        current = self.primero
        while current:
            yield current
            current = current.siguiente
    def obtener_tamano(self):
        actual = self.primero
        tamano = 0
        
        while actual is not None:
            tamano += 1
            actual = actual.siguiente

        return tamano            