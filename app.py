import tkinter as tk
from subprocess import check_output
from tkinter import filedialog, messagebox

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from typing import List, Any
import xml.etree.ElementTree as ET
import json
import traceback
import os
#clases
from drones.clase.Drones import Drones
from graphviz import Digraph
import xml.dom.minidom as minidom

from Sistema.clase.Alturas import Alturas
from Sistema.clase.Contenido import Contenido
from Sistema.clase.ListaSistema_Drones import ListaSistema_Drones
from Sistema.clase.Sistema_Drones import Sistema_Drones

from mensajes.clase.Mensaje import Mensaje
from mensajes.clase.Instrucciones import Instrucciones

from recepcion.clase.Accion import Accion
from recepcion.clase.nombres import Nombres
from recepcion.clase.instrucciones2 import instrucciones2
from recepcion.clase.mensajeRec import mensajeRec

import os
from drones.list.listDrones import listDrones

from Sistema.list.listAlturas import listAlturas
from Sistema.list.listContenido import listContenido
from Sistema.list.listListaSistema_Drones import listListaSistema_Drones
from Sistema.list.listSistema_Drones import listSistema_Drones

from mensajes.list.listMensaje import listMensaje
from mensajes.list.listInstrucciones import listInstrucciones

from recepcion.list.listAccion import listAccion
from recepcion.list.listnombres import listnombres
from recepcion.list.listinstrucciones2 import listinstrucciones2
from recepcion.list.listmensajeRec import listmensajeRec

class TextEditorApp:
    def __init__(self, root):
        self.listaTEMPDrones = listDrones()
        self.listaSupremaDelmensaje = listmensajeRec()
        self.listAccionTemp = listAccion()
        self.listListaSistema_DronesTemp = listListaSistema_Drones()
        self.listSistema_DronesTemp = listSistema_Drones()

        self.mensaJeTemp = listMensaje()
        self.emitiendoLuz= 0

        self.men =""
        #borrrar
        self.root = root
        self.root.title("Editor de Texto")

        self.line_number_bar = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        self.text_widget = ScrolledText(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')
        self.wadm = None


        self.current_line = 1

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_Init = tk.Menu(self.menu_bar, tearoff=0)
        self.file_Dron = tk.Menu(self.menu_bar, tearoff=0)
        self.file_Men = tk.Menu(self.menu_bar, tearoff=0)

        
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Inicializar", command=self.inicializa)

        self.menu_bar.add_cascade(label="Gestionar Drones", menu=self.file_Dron)
        self.menu_bar.add_cascade(label="Mensajes", menu=self.file_Men)
        self.menu_bar.add_cascade(label="Graficar Sistema de Drones", command=self.invocarMM)
        self.menu_bar.add_cascade(label="Ayuda", command=self.datosStudiantes)


        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Generar XML", command=self.xmlSale)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        self.file_Dron.add_command(label="Ver Drones", command=self.mostrar_tablaDron)
        self.file_Dron.add_command(label="Agregar", command=self.agregar_DronActivacionSecretaMortalAlienigena)
        
        self.file_Men.add_command(label="Ver Mensajes", command=self.mostrar_tablaMensaje)

    def open_file(self):
        
        file_path = filedialog.askopenfilename(filetypes=[("Archivos xml", "*.xml")])
        self.wadm = file_path
        print(self.wadm)
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                tree = ET.parse(file_path)
                raiz=tree.getroot()
                self.cargarDron(raiz)
                self.cargarSistema(raiz)
                self.cargarMensaje(raiz)
                
                self.operar()
                #self.data = content


    def cargarDron(self,raiz):  
        #Dron cargado y listo para matarhg
            for dronesRecibidos_temporal in raiz.findall("listaDrones"):
                for dron in dronesRecibidos_temporal.findall("dron"):
                    nombre = dron.text

                    nuevo= Drones(nombre)
                    self.listaTEMPDrones.Incertar_dato(nuevo)
                    print("Matrices ok!")

            self.listaTEMPDrones.recorrer_e_imprimir_lista()


    def cargarMensaje(self,raiz):  
        #Dron cargado y listo para matarhg
            for mensajesRecibidosTemp in raiz.findall("listaMensajes"):
                for dron in mensajesRecibidosTemp.findall("Mensaje"):
                    nombre = dron.get("nombre")
                    SD = dron.find("sistemaDrones").text
                    temporal = listInstrucciones()
                    for instrucciones in dron.findall(".//instruccion"):
                         dronname = instrucciones.get("dron")
                         altura = instrucciones.text
                         new = Instrucciones(dronname,altura)
                         temporal.Incertar_dato(new)
                    nuevo= Mensaje(nombre,SD,temporal)
                    self.mensaJeTemp.Incertar_dato(nuevo)
                    print("Matrices ok!")

            self.mensaJeTemp.recorrer_e_imprimir_lista()

    def cargarSistema(self,raiz):  
        #Dron cargado y listo para matar
            for listaSistemasDrones_temporal in raiz.findall("listaSistemasDrones"):

                for sistemaDrones in listaSistemasDrones_temporal.findall("sistemaDrones"):
                    nombre = sistemaDrones.get("nombre")
                    for alt in sistemaDrones.findall("alturaMaxima"):
                         alturaMax = alt.text
                    for cantidadDrones in sistemaDrones.findall("cantidadDrones"):
                         cantDrones = cantidadDrones.text
                    
                    listContenidoTemp = listContenido()                    
                    print("Matrices ok!")

                    for contenido in sistemaDrones.findall("contenido"):
                         
                            for dron in contenido.findall("dron"):
                              dronCont = dron.text
                              print(dronCont)  
                            llave = False
                            for dronesExistente in self.listaTEMPDrones:
                                 if(dronCont == dronesExistente.Drones.nombre):
                                      llave = True
                                      break
                            if(llave == True):          
                                listAlturasTemp = listAlturas()

                                for altura in contenido.findall(".//altura"):    
                                    letraValor = altura.text
                                    metroValor = altura.get("valor")

                                    nuevoAlturas = Alturas(metroValor,letraValor)
                                    listAlturasTemp.Incertar_dato(nuevoAlturas)
                                    print(altura.text)

                                    print("Matrices ok!")

                                nuevoCont = Contenido(dronCont,listAlturasTemp)

                                listContenidoTemp.Incertar_dato(nuevoCont)
                            else:
                                 print("El dron: ",dronCont," no existe en el listado de drones")

                    
                    nuevoSD= Sistema_Drones(nombre,alturaMax,cantDrones,listContenidoTemp)
                    self.listSistema_DronesTemp.Incertar_dato(nuevoSD)
                    
            self.listSistema_DronesTemp.recorrer_e_imprimir_lista()



    def operar(self):
        #borrar
        milista =[]
        

        tiempo=0

        lista_sistemas_drones = listSistema_Drones()
        lista_mensajes = listMensaje()

        for sistema_drones in self.listSistema_DronesTemp:

            for mensaje in self.mensaJeTemp:
                self.listaSupremaDelmensaje 
                if(sistema_drones.Sistema_Drones.nombre==mensaje.Mensaje.sistemaDrones):
                    Aguacate=""
                    tiempo=0
                    self.listAccionTemp = listAccion()
                    listaParaSeñoras = listAccion()
                    listaCantidadMovimientos= listAccion()
                    
                         
                    for cifrado in mensaje.Mensaje.listInstrucciones:
                        NuevoMov = Accion(cifrado.Instrucciones.dron,"esperar",1)

                        listaCantidadMovimientos.Incertar_dato(NuevoMov)                

                        for drones in sistema_drones.Sistema_Drones.listContenido:
                            MovActual= listaCantidadMovimientos.buscarDronUltimo().Accion
                            

                            if(drones.Contenido.dron == cifrado.Instrucciones.dron):

                                for alturas in drones.Contenido.listAlturas:
                                    if(cifrado.Instrucciones.altura==alturas.Alturas.metros):
                                        while MovActual.posicion != int(alturas.Alturas.metros):
                                             
                                             if(MovActual.posicion > int(alturas.Alturas.metros)):
                                                  new = listaCantidadMovimientos.devolverbajar()
                                                  time = listaParaSeñoras.CualEsTuTiempoBro(new.Accion.dron)
                                                  tiempo+=1                                 
                                                  nubo = Accion(new.Accion.dron,new.Accion.accion,time+1)
                                                  listaParaSeñoras.Incertar_dato(nubo)

                                                  print(str(new.Accion.accion))

                                             if(MovActual.posicion<int(alturas.Alturas.metros)):
                                                  new = listaCantidadMovimientos.devolverSubir()
                                                  time = listaParaSeñoras.CualEsTuTiempoBro(new.Accion.dron)

                                                  tiempo+=1
                                                  nubo = Accion(new.Accion.dron,new.Accion.accion,time+1)
                                                  listaParaSeñoras.Incertar_dato(nubo)                                                  
                                                  
                                                  print(str(new.Accion.accion))


                                    
                                        if(MovActual.posicion==int(alturas.Alturas.metros)):
                                                  
                                                  def recursiva(tiempo):
                                                    print("haberquesale:",MovActual.dron)
                                                    aquiYahora= listaParaSeñoras.afirmativoEstaFuncionNosDaraElganeTODOoNADAAAAAAAAAAA(MovActual.dron)
                                                    if(aquiYahora=="esperar"):
                                                        new = listaCantidadMovimientos.devolverEsperar()  
                                                        time = listaParaSeñoras.CualEsTuTiempoBro(new.Accion.dron)

                                                        tiempo+=1 
                                                        nubo = Accion(new.Accion.dron,"esperar",time+1)
                                                        listaParaSeñoras.Incertar_dato(nubo)  
                                                        recursiva(tiempo)   
                                                    else:
                                                        new = listaCantidadMovimientos.devolverLuz()  
                                                        print("t:",new.Accion.posicion)
                                                        time = listaParaSeñoras.CualEsTuTiempoBro(new.Accion.dron)
                                                        tiempo+=1 
                                                        nubo = Accion(new.Accion.dron,new.Accion.accion,time+1)
                                                        listaParaSeñoras.Incertar_dato(nubo)
                                                        nonlocal Aguacate  
                                                        Aguacate=Aguacate+alturas.Alturas.letra                                                                                                      
                                                    print(str(new.Accion.accion))      
                                                  recursiva(tiempo)                                            






                                        



                    n=listaParaSeñoras.devolverNumeroMax()
                    lista = listaParaSeñoras.devolverNombres()
                    i=0
                    text=str(i)+" / "
                    llave ="ingrese"
                    for nombres in lista:

                            for comid in listaParaSeñoras:
                                    if(comid.Accion.dron == nombres.Nombres.nombres ):
                                        llave = "ingrese"
                                        final = comid.Accion.posicion
                            numeroZota =0  
                            e = 1          
                            h=0
                            if(final != n):          
                                numeroZota= n-final   

                                for e in range(numeroZota):
                                    h+=1
                                    nub= Accion(nombres.Nombres.nombres,"esperar",final+h)   
                                    listaParaSeñoras.Incertar_dato(nub)

                    h =0
                    listaParaInstruccion = listinstrucciones2()
                    for i in range(n):
                        h+=1
                        text=str(h)+" / "
                        listaParaHijosdeLaLuna =  listAccion()
                        for casa in lista:
                            for comid in listaParaSeñoras:
                                    if(h==comid.Accion.posicion and comid.Accion.dron == casa.Nombres.nombres ):
                                        listaParaHijosdeLaLuna.Incertar_dato(Accion(comid.Accion.dron,comid.Accion.accion,comid.Accion.posicion))
                                        text=text+" / "+comid.Accion.accion

                        print("++++++++++++++++++++++++++++++++++++++++++++")
                        nov = instrucciones2(h,listaParaHijosdeLaLuna)
                        listaParaInstruccion.Incertar_dato(nov)

                    listaParaInstruccion.recorrer_e_imprimir_lista()
                    listaParaSeñoras  .recorrer_e_imprimir_listaTipo_2()    
                    nobobobo = mensajeRec(mensaje.Mensaje.nombre,mensaje.Mensaje.sistemaDrones,n,Aguacate,listaParaInstruccion) 
                    self.listaSupremaDelmensaje .Incertar_dato(nobobobo)
                    self.listaSupremaDelmensaje .recorrer_e_imprimir_lista()
                    print(f"Encontre igualdad, iniciando proceso de combocatoria celestial: {Aguacate} y tiempo :{n}")




    ####### windos
    def mostrar_tablaMensaje(self):


        ventana = tk.Tk()
        ventana.title("Tabla de Mensajes")

        # Crear un Treeview
        tree = ttk.Treeview(ventana)

        # Configurar las columnas en el Treeview
        tree["columns"] = ("Nombre", "SistemaDrones")
        tree.heading("#1", text="Nombre")
        tree.heading("#2", text="SistemaDrones")

        tree.column("#1", width=100)
        tree.column("#2", width=100)
        # Agregar datos a la tabla
        def hacer_algo(nombre):
            print("Nombre:",nombre)
            self.listaSupremaDelmensaje
            texto =""
            for ListadoDeMensajes in self.listaSupremaDelmensaje:
                 if(ListadoDeMensajes.mensajeRec.nombre == nombre):
                        

                    texto="Nombre:"+nombre+"\n"
                    texto=texto+"Sistema de drones:"+ListadoDeMensajes.mensajeRec.sitema_drones+"\n"
                    texto= texto+"Tiempo Optimo:"+str(ListadoDeMensajes.mensajeRec.tiempo)+"\n"
                    texto= texto+"Mensaje:"+ListadoDeMensajes.mensajeRec.mensaje+"\n"
                    texto= texto+"Acciones:\n"
                    texto= texto+"--------------------------------------------------------------\n"
                    texto= texto+"--------------------------------------------------------------\n"                    
                    for instruc in ListadoDeMensajes.mensajeRec.lista_instrucciones2:
                         texto= texto+"\n"
                         texto= texto+"Segundo:"+str(instruc.instrucciones2.tiempo)+"\n"
                         texto= texto+"++++++++++++++++++++++++++++++++++++++++++++\n"
                         for acciones in instruc.instrucciones2.lista_acciones:
                            texto= texto+"Dron:"+acciones.Accion.dron+"  Accion:"+acciones.Accion.accion+"  segundo:"+str(acciones.Accion.posicion)+"\n"    
            ventana_emergente = tk.Toplevel(root)
            ventana_emergente.title("Ventana Emergente")
            etiqueta = tk.Label(ventana_emergente, text=texto)
            etiqueta.pack()
            boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
            boton_cerrar.pack()

        def hacer_algo2(nombre):
            print("Nombre:",nombre)

            self.Graficar_Mensaje(nombre)



        def obtener_elemento_seleccionado():
            


        # nUEVO
            item = tree.selection()
            if item:
                nombre = tree.item(item, "values")[0]
                hacer_algo(nombre)
            else:
                print("Ningún elemento seleccionado")

        for mensaje in self.mensaJeTemp:
            print(mensaje.Mensaje.nombre)
            valores = [mensaje.Mensaje.nombre, mensaje.Mensaje.sistemaDrones]
            tree.insert("", "end", values=valores)

        def obtener_elemento_seleccionado2():
            


        # Acción al hacer clic en una celda de la columna 3
            item = tree.selection()
            if item:
                nombre = tree.item(item, "values")[0]
                hacer_algo2(nombre)
            else:
                print("Ningún elemento seleccionado")


        # Empacar el Treeview

        tree.pack()
        boton = tk.Button(ventana, text="Obtener Elemento Seleccionado", command=obtener_elemento_seleccionado)
        boton2 = tk.Button(ventana, text="Graficar", command=obtener_elemento_seleccionado2)

        boton.pack()
        boton2.pack()
        ventana.mainloop()


    def mostrar_tablaDron(self):


        ventana = tk.Tk()
        ventana.title("Tabla de Mensajes")

        # Crear un Treeview
        tree = ttk.Treeview(ventana)

        # Configurar las columnas en el Treeview
        tree["columns"] = ("Nombre", "SistemaDrones")
        tree.heading("#1", text="dron")

        tree.column("#1", width=100)

        for mensaje in self.listaTEMPDrones:
            valores = [mensaje.Drones.nombre]
            tree.insert("", "end", values=valores)



        # Empacar el Treeview

        tree.pack()

        ventana.mainloop()
        # Ejemplo de una lista de objetos Mensaje
        lista_mensajes = [
            Mensaje("Mensaje1", "SistemaDrones1"),
            Mensaje("Mensaje2", "SistemaDrones2"),
            Mensaje("Mensaje3", "SistemaDrones3"),
            # Puedes agregar más objetos Mensaje aquí
        ]

        # Llamar a la función para mostrar la tabla


    def agregar_DronActivacionSecretaMortalAlienigena(self):
        def crear_mensaje():
            nombre = nombre_entry.get()  # Obtener el valor ingresado en el campo de nombre
            Nuevo = Drones(nombre)
            self.listaTEMPDrones.Incertar_dato(Nuevo)
        # Crear una ventana principal
        ventana_principal = tk.Tk()
        ventana_principal.title("Crear Mensaje")

        # Crear un campo de entrada para el nombre
        nombre_label = tk.Label(ventana_principal, text="Nombre:")
        nombre_label.pack()

        nombre_entry = tk.Entry(ventana_principal)
        nombre_entry.pack()

        # Crear un botón para crear el mensaje
        crear_boton = tk.Button(ventana_principal, text="Crear", command=crear_mensaje)
        crear_boton.pack()

        ventana_principal.mainloop()      
    def gh(self):
        try:
            operar_().clear()

            intrucciones = intruccion(self.data)
            respuestas_Operaciones = operar_()

            contenido = "digraph G {\n\n"                         
            r = open("Operaciones.dot", "w", encoding="utf-8")
            contenido += str(Graphviz(respuestas_Operaciones))
            contenido += '\n}'

            r.write(contenido)
            r.close()

            print("...............................................................")
            print("            ** COMANDOS DE GRAPHVIZ **               ")
            print("")
            print(contenido)
            print("...............................................................")
            print("")
            print("FIN.....")

            os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
            os.system('dot -Tpng Operaciones.dot -o grafo.png')
            print("terminado")

        except Exception as e:
            messagebox.showinfo("Se produjo un error: ",str(e))
            messagebox.showinfo("Mensaje", f"Error al generar el archivo de salida, Verificar el Archivo de entrada.")
        else:
            messagebox.showinfo("Mensaje", "Grafica generada con exito")
            respuestas_Operaciones.clear()
            intrucciones.clear()

    def Graphviz2(self):
            colorNodo = ""
            fuenteNodo = ""
            formaNodo = ""
            try:
                print('---------------------------------------------')
                for respuesta in self.listSistema_DronesTemp:
                        temporal = str(respuesta.texto.operar(None)).lower()
                        print(respuesta.texto.operar(None))
                        print(respuesta.ejecutarT())
                        Titulo = respuesta.Sistema_Drones.nombre

                        temporal = "yellow"
                        colorNodo = temporal



                        temporal = "black"

                        fuenteNodo = temporal


                        temporal = "circle"
                        formaNodo = temporal




                temporal = ''
                CnumIzquierdo = 0
                CnumDerecho = 0
                Crespuesta = 0
                Ctotal = 0

                text = ""
                text += f"\tnode [shape={formaNodo}]\n"

                text += f"\tnodo0 [label = \"Sistema de Drones\"]\n"
                text += f"\tnodo0" + "[" + f"fontcolor = {fuenteNodo}" + "]\n"

                for respuesta in self.listSistema_DronesTemp:
                    CnumIzquierdo += 1
                    CnumDerecho += 1
                    Crespuesta += 1
                    Ctotal += 1

                    
                    text += f"\tnodo{self.generate_unique_node_id()} [label = \"{Titulo}\", style = filled, fillcolor = {colorNodo}, fontcolor = {fuenteNodo}, shape = {formaNodo}]\n"
                    
                    if parent:
                        text += f"\t{nodo.id} -> {parent}\n"

                    # Llamar a la función recursivamente para los hijos
                    for hijo in nodo.hijos:
                        text += self.Graphviz(hijo, parent=nodo.id)

                    parent = None    
                return text
            except Exception as e:
                messagebox.showinfo("Se produjo un error: ",str(e)+str(traceback.extract_tb(e.__traceback__))  )
                messagebox.showinfo("Mensaje", "Error en los comandos de Graphviz")

    def miasma():
        for i, sistemaD in enumerate(sistemaD_lista):
    # Agregar el nodo SistemaD al grafo
            dot.node(f'SistemaD{i}', shape='box', label='SistemaD')

    # Recorrer la lista de hijos de SistemaD y agregar los nodos de Drones
        for j, drone in enumerate(sistemaD.lista_hijos):
            dot.node(f'Drone{i}_{j}', shape='ellipse', label=f'Dron: {drone.nombre}')
            dot.edge(f'SistemaD{i}', f'Drone{i}_{j}')

# Guardar el grafo como archivo
        dot.render('grafico_sistemaD', format='png')                               


    def inicializa(self):
        self.listaTEMPDrones.eliminar()
        self.listaSupremaDelmensaje.eliminar()
        self.listSistema_DronesTemp.eliminar()
        self.mensaJeTemp.eliminar()
        messagebox.showinfo("Eliminado", "App inicializado exitosamente.")

    def datosStudiantes(self):

            texto =""
            texto += "Julio Samuel Isaac Lima Donis \n"
            texto += "202200002 \n"
            texto += "Introducción a la Programación y Computación 2 sección D \n"
            texto += "Ingenieria en Ciencias y Sistemas \n"
            texto += "4to semestre \n"
            texto += "Documentacion Link : https://github.com/Jlima2016306/IPC2_Proyecto2_202200002/blob/main/Documentaci%C3%B3n.pdf \n"
            ventana_emergente = tk.Toplevel(root)
            ventana_emergente.title("Ayuda")
            etiqueta = tk.Label(ventana_emergente, text=texto)
            etiqueta.pack()
            boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
            boton_cerrar.pack()


    

    def generar_grafo_sistemaD(self,dot, sistemaD, parent=None):
        # Agregar el nodo actual al gráfico DOT
        node_label = f'{sistemaD.Sistema_Drones.nombre}'
        dot.node(node_label, shape='box')  # Usamos 'box' para el nodo SistemaD
        
        # Agregar relación con el nodo padre (si lo hay)
        if parent:
            dot.edge(parent, node_label)
        
        # Recorrer la lista de hijos y generar el gráfico para cada uno
        for hijo in sistemaD.Sistema_Drones.listContenido:
            #if isinstance(hijo, Sistema_Drones):
            #    self.generar_grafo_sistemaD(dot, hijo, node_label)
            #elif isinstance(hijo, Contenido):
                name = hijo.Contenido.dron
                print(name)
                dron_label = f'{sistemaD.Sistema_Drones.nombre}_{hijo.Contenido.dron}'
                dot.node(f'{sistemaD.Sistema_Drones.nombre}_{hijo.Contenido.dron}', shape='ellipse')  # Usamos 'ellipse' para los nodos Drones
                dot.edge(node_label, f'{sistemaD.Sistema_Drones.nombre}_{hijo.Contenido.dron}')

                sub_parent = dron_label  # Nodo padre para la escalera de hijos
                i=0
                for nieto in hijo.Contenido.listAlturas:
                    dot.edge(sub_parent, f'{sistemaD.Sistema_Drones.nombre}_{hijo.Contenido.dron}_{nieto.Alturas.letra,"=",nieto.Alturas.metros}')
                    sub_parent =  f'{sistemaD.Sistema_Drones.nombre}_{hijo.Contenido.dron}_{nieto.Alturas.letra,"=",nieto.Alturas.metros}' # El siguiente nodo será el padre de los siguientes hijos
                    i+=1

    def invocarMM(self):
    # Crear una estructura de datos de ejemplo

        # Crear un objeto Digraph de Graphviz
        dot = Digraph(comment='Grafo de SistemaD', format='png')

        # Generar el gráfico DOT
        for Sistem in self.listSistema_DronesTemp:

            self.generar_grafo_sistemaD(dot, Sistem)
        

        # Renderizar el gráfico en un archivo PNG
        dot.render('sistemaD', format='png')
        messagebox.showinfo("Guardado", "Archivo de Sistema de drones guardado exitosamente.")

    def Graficar_Mensaje(self, nombre):
            dot = Digraph(comment="Tabla de Instrucciones")

            # Lista de instrucciones y acciones de ejemplo
            for ListadoDeMensajes in self.listaSupremaDelmensaje:
                 if(ListadoDeMensajes.mensajeRec.nombre == nombre):
                        for instruc in ListadoDeMensajes.mensajeRec.lista_instrucciones2:
                            node_label = f"{0}\n"

                            for acciones in instruc.instrucciones2.lista_acciones:    
                                
                                node_label += "\n"+acciones.Accion.dron + "\n"          
                            dot.node(node_label, shape="rectangle", fontsize="10")   
                            break                         
                        for instruc in ListadoDeMensajes.mensajeRec.lista_instrucciones2:
                            node_label = f"{instruc.instrucciones2.tiempo}\n"

                            for acciones in instruc.instrucciones2.lista_acciones:    
                                
                                node_label += "\n"+acciones.Accion.accion + "\n"          
                            dot.node(node_label, shape="rectangle", fontsize="10")    


            # Guardar el código DOT en un archivo
            dot_file = "tabla_de_instrucciones.dot"
            dot.save(dot_file)
            dot.render("tabla_de_instrucciones", format="png", cleanup=True)
            messagebox.showinfo("Guardado", "Archivo PNG de grafica guardado exitosamente.")

    def xmlSale(self):
            # Crear el elemento raíz
            respuesta = ET.Element("respuesta")

            # Crear el elemento listaMensajes


            # Puedes agregar más tiempos, acciones de dron y mensajes si es necesario

            # Crear un objeto ElementTree para escribir en un archivo
            lista_mensajes = ET.SubElement(respuesta, "listaMensajes")
            # Guardar el XML en un archivo
       
            for ListadoDeMensajes in self.listaSupremaDelmensaje:
                

                # Crear un mensaje
                mensaje = ET.SubElement(lista_mensajes, "mensaje", nombre=ListadoDeMensajes.mensajeRec.nombre)

                # Agregar elementos dentro del mensaje
                sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
                sistema_drones.text = ListadoDeMensajes.mensajeRec.sitema_drones

                tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
                tiempo_optimo.text = str(ListadoDeMensajes.mensajeRec.tiempo)

                mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
                mensaje_recibido.text = ListadoDeMensajes.mensajeRec.mensaje

                instrucciones = ET.SubElement(mensaje, "instrucciones")

                # Agregar tiempo y acciones dentro de instrucciones


                for instruc in ListadoDeMensajes.mensajeRec.lista_instrucciones2:
                    tiempo = ET.SubElement(instrucciones, "tiempo", valor=str(instruc.instrucciones2.tiempo))
                    acciones = ET.SubElement(tiempo, "acciones")

                    for acciones2 in instruc.instrucciones2.lista_acciones: 
                                

                                dron = ET.SubElement(acciones, "dron", nombre=acciones2.Accion.dron)
                                dron.text = acciones2.Accion.accion
            tree = ET.ElementTree(respuesta)
            xmlstr = minidom.parseString(ET.tostring(respuesta)).toprettyxml(indent="    ")  # Especifica el número de espacios para la indentación

            with open("archivo.xml", "w", encoding="utf-8") as xml_file:
                xml_file.write(xmlstr)  
                messagebox.showinfo("Guardado", "Archivo XML guardado exitosamente.")              
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()