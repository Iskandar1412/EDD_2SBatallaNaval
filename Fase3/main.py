#Fase 2 y Fase 3 fueron hechos en UBUNTU

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random
import json #Servira Para tambien Fase 3
from turtle import width
from PIL import Image, ImageTk
from tkinter import filedialog
from datetime import date, datetime
import sys, os
from eth_account import Account
import secrets
from web3 import Web3, EthereumTesterProvider #Nuevo De FASE 3 -- pip install web3
#from PIL import ImageTk, Image
#ESTRUCTURA DE LA MATRIZ DISPERSA :v
from Structures.Dispersa.Matrix import Matriz_Dispesa
from Structures.Barcos.Barcos import Barcos_List
from Structures.Merkle.Merkle import Merkle #FASE3
from Structures.HashTable.Hash2 import Hashi #FASE3
from Structures.BlockChain.Block import BlockChain #FASE3
from Structures.UsuarioAdministrador.admin import ListaUsuarioAdministrador
UsuarioAdministrador = ListaUsuarioAdministrador()
PortavionesPJ1 = Barcos_List()
SubmarinosPJ1 = Barcos_List()
DestructoresPJ1 = Barcos_List()
BuquesPJ1 = Barcos_List()
PortavionesPJ2 = Barcos_List()
SubmarinosPJ2 = Barcos_List()
DestructoresPJ2 = Barcos_List()
BuquesPJ2 = Barcos_List()
TableroPJ1 = Matriz_Dispesa()
TableroPJ2 = Matriz_Dispesa()
MiniTablerodePJ2 = Matriz_Dispesa()
MiniTablerodePJ1 = Matriz_Dispesa()
TablaHash = Hashi()     #FASE 3
MerkleTree = Merkle()   #FASE 3
Bloques = BlockChain()  #FASE 3
#from Structures.AVL.AVLTree import DobleLUSR
from Structures.ListL.ListadeListas import ListaListas
from Structures.ListaUsuarios.Usuarios import Lista_Usuario
from Structures.DoubleLinked.DobleART import DobleLART
from Structures.Cola.cola import Cola
from Structures.Pila.Pila import ListaPila
#PARA INTERACTUAR CON LA ARBOL AVL DobleLUSR
#PARA INTERACTUAR CON LISTA DE LISTAS ListadeListas.h / ListaListas
ListaArticulosPrim = DobleLART()
ListaLArticulos = ListaListas()
ColaTutorial = Cola()
ListaPila = ListaPila()

#ESTRUCTURA QUE GUARDARA AL USUARIO INGRESADO
#USUARIO A CREAR
#ListaUsuariosDB = DobleLUSR()
ListaUsuariosDB = Lista_Usuario()
UsuarioAdministrador.add('EDD', 'edd123', 22, 13500)
#ListaUsuariosDB.add(5, 'sdf', 'asdf', 45, 45)
#ListaUsuariosDB.Display()
                    #ID Nick   Pass     Edad Mon
#ListaUsuariosDB.add(1, "EDD", "edd123", 22, 8888)
#ListaUsuariosDB.add(1,"EDD", "edd123", 22, 8888)
#print(UsuarioAdministrador.cabeza.strCeros)
#UsuarioAdministrador.InicioAdmin("EDD", "edd123")
#daata = "{\\n\tFROM:0x428154679734asf46sddb2s113250b,\\n\tSKINS:[\\n\t\t{\\n\t\t\tSKIN:123,\\n\t\t\tVALUE:456\\n\t\t}\\n]"
#Bloques.insertar(daata, "0ds1f2s5d46f8s7964fffsxc12", 4, "0000")
#Bloques.insertar(daata, "0ds1f2s5d46f8s7964fffsxc468", 4, "0000")
#Bloques.insertar(daata, "0fds4f64a6s8ff21a01011103asdf5", 4, "0000")
#Bloques.insertar(daata, "0ds1f2s5d46f8s7964fffsx46fds", 4, "0000")
#Bloques.graphosBlock()

#Conexiones Web3
#infura_url = "https://mainnet.infura.io/v3/d399ce764cc54414a51edccd8c85e891"
#abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
#addres = '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07'
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
#priv = secrets.token_hex(32)
#priv_key = "0x" + priv
#acct = Account.from_key(priv_key)
#account = acct.address
#print(account, priv_key)
#contract = web3.eth.contract(address=addres, abi=abi)
#print('Connected:',web3.isConnected())
#web3.eth.defaultAccount = web3.eth.accounts[0]
#private_key = '89693160dcf6a90739e56ad70c7d505bb8c9d5dd7197c2cdeae06d8443d80594'
#print(web3.eth.accounts[5])
#bcb4ea03eb7a2f5cbfad56a01d9b94b6ae5d9eb22477a73f57715b4a1fe3681d
#e945ab502a55e0ebcd1cd481d2402bfa1a3f1b8c9d104b6225c109af185f39fa
#tx = {
#    'to': accoutn,#al usuario en donde ira pagado
#    'skin': idskin,
#    'value': web3.toWei(1, 'ether'),
#    'gas': 2000000,
#    'gasPrice': web3.toWei('50', 'gwei')
#}
#
#signedTx = web3.eth.account.signTransaction(tx, private_key)
#tx_hash = web
#print(web3.eth.defaultAccount)

#web3 = Web3(Web3.HTTPProvider(infura_url))
#print('Conected:', web3.isConnected())
#print('Blocks:',web3.eth.blockNumber)
#abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
#addres = '0xd26114cd6EE289AccF82350c8d8487fedB8A0C07'

#print(contract)
#supply
#totalSupply = contract.functions.totalSupply().call()
#print(totalSupply)
#print(web3.fromWei(totalSupply, 'ether'))
#print(contract.functions.name().call())
#print(contract.functions.symbol().call())
#balance = contract.functions.balanceOf('0x23735750a6ed0119e778d9bb969137df8cc8c3d1').call()
#print(web3.fromWei(balance, 'ether'))



#-----------------------------Clase Usuario Administrador-----------------------------
#-----------------------------Clase Usuario Administrador-----------------------------
#-----------------------------Clase Usuario Administrador-----------------------------
#-----------------------------Clase Usuario Administrador-----------------------------

class Administrador(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.restante = 0
        self.widgetsAdmin()
    
    def aHoras(self, segundos):
        segundos = segundos % (24 * 3600)
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
        return "%02d:%02d:%02d" % (horas, minutos, segundos)
    
    def aSegundos(self, hora):
        h, m, s = hora.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    
    def cuenta(self, restante = None):
        if restante != None:
            self.restante = restante
        if self.restante <= 0:
            Mensajefinal = '00:00:00'
            self.LabelCuenta.configure(text=Mensajefinal)
            #print("FINALIZADO")
        else:
            horaActual = self.aHoras(self.restante)
            self.LabelCuenta.configure(text=horaActual)
            self.restante = self.restante - 1
            self.after(1000, self.cuenta)
    
    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) ==0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
         
    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
    
    def refrescarTiempo(self):
        time = self.aSegundos("{0}:{1}:{2}".format(self.CajaHoras.get(), UsuarioAdministrador.cabeza.tiempomin, UsuarioAdministrador.cabeza.tiemposeg))
        self.LabelCuenta['text'] = self.aHoras(time)
    
    def AceptarTiempo(self):
        UsuarioAdministrador.cabeza.tiempomin = self.CajaMinutos.get()#no esta originalmente
        UsuarioAdministrador.cabeza.tiemposeg = self.CajaSegundos.get()#no esta originalmente
        total = self.aSegundos("{0}:{1}:{2}".format(self.CajaHoras.get(), UsuarioAdministrador.cabeza.tiempomin, UsuarioAdministrador.cabeza.tiemposeg))
        self.LabelCuenta['text'] = self.aHoras(total)#no esta originalmente
        #if total > 0:
        #    self.cuenta(total)
    
    def AceptarCeros(self):
        if self.entradaCeros.get().isdigit() == True:
            UsuarioAdministrador.cabeza.cantidadceros = int(self.entradaCeros.get())
            UsuarioAdministrador.cabeza.strCeros = str(self.entradastrCeros.get())
            #print(UsuarioAdministrador.cabeza.cantidadceros)
    
    def salir(self):
        self.master.destroy()
        self.master.quit()
    
    def CrearBloque(self):
        MerkleTree.add("1")
        MerkleTree.auth()
        rootMerk = MerkleTree.tophash.hash
        cantidadceros = UsuarioAdministrador.cabeza.cantidadceros
        strCeros = UsuarioAdministrador.cabeza.strCeros
        Bloques.insertar("", rootMerk, cantidadceros, strCeros, "{\n},\n")
        MerkleTree.eliminar()
        print('Bloque Generado Exitosamente')
    
    def regresar(self):
        self.master.withdraw()
        print('Saliendo del Admin')
        self.Ventana_principal = Toplevel()
        self.Ventana_principal.config(bg='#1D1A1A')
        self.Ventana_principal.title("Proyecto Fase 3 - 201906051 (Inicio)")
        ruta = 'Images/IMGF.png'
        program_directory=sys.path[0]
        self.Ventana_principal.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
        x_wi = 350
        y_he = 500
        xpos = y_he
        ypos = (ventana.winfo_screenheight() // 2) - (y_he // 2) -25
        post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
        self.Ventana_principal.geometry(post)
        self.Ventana_principal.resizable(0,0)
        self.Ventana_principal.protocol("WM_DELETE_WINDOW", self.salir)
        app = Inicio(self.Ventana_principal)
        app.mainloop()
        
    def widgetsAdmin(self):
        #Controles Tiempo
        self.ControlesTiempo = Frame(self.master, bg="red", height=30)
        self.ControlesTiempo.place(x=70, y=10)
        #Minutos
        self.LabelTiempoHor = Label(self.ControlesTiempo, text=' H ', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 10, 'bold'))
        self.LabelTiempoHor.pack(side=LEFT)
        self.CajaHoras = Spinbox(self.ControlesTiempo, from_= 00, to = 23, font=('Comic Sans MS', 10),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", width=5)
        self.CajaHoras.pack(side=LEFT)
        #Minutos
        self.LabelTiempoMin = Label(self.ControlesTiempo, text=' M ', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 10, 'bold'))
        self.LabelTiempoMin.pack(side=LEFT)
        self.CajaMinutos = Spinbox(self.ControlesTiempo, from_= 00, to = 59, font=('Comic Sans MS', 10),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", width=5)
        self.CajaMinutos.pack(side=LEFT)
        #Segundos
        self.LabelTiempoSeg = Label(self.ControlesTiempo, text=' S ', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 10, 'bold'))
        self.LabelTiempoSeg.pack(side=LEFT)
        self.CajaSegundos = Spinbox(self.ControlesTiempo, from_= 00, to = 59, font=('Comic Sans MS', 10),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", width=5)
        self.CajaSegundos.pack(side=LEFT)
        #Cuenta
        self.LabelCuenta = Label(self.master, text='00:00:00', font=('Courier New',50, 'bold'), bg='#1D1A1A')
        self.LabelCuenta.place(x=15, y=70)
        self.botondesbloquear = Button(self.master, text= 'Aceptar',activebackground='#1D1A1A', command=lambda:self.AceptarTiempo(),activeforeground='white',  bg='white', font=('Arial', 10,'bold'))
        self.botondesbloquear.place(x=140, y=180)
        self.refrescarTiempo()
        #self.AceptarTiempo()
        #Cantidad de Ceros
        self.LabelCantidad0 = Label(self.master, text='Cantidad Ceros', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 12, 'bold'))
        self.LabelCantidad0.place(x=40, y=250)
        self.entradaCeros = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
        self.entradaCeros.insert(0, 'Ceros ' + str(UsuarioAdministrador.cabeza.cantidadceros))
        self.entradaCeros.bind("<FocusIn>", lambda args: self.entry_in(self.entradaCeros))
        self.entradaCeros.bind("<FocusOut>", lambda args: self.entry_out(self.entradaCeros, 'Cantidad 0 : ' + str(UsuarioAdministrador.cabeza.cantidadceros)))
        self.entradaCeros.place(x=220, y=247)
        self.LabelstrCantidad0 = Label(self.master, text='Cantidad Ceros', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 12, 'bold'))
        self.LabelstrCantidad0.place(x=40, y=250)
        self.entradastrCeros = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
        self.entradastrCeros.insert(0, 'Ceros ' + UsuarioAdministrador.cabeza.strCeros)
        self.entradastrCeros.bind("<FocusIn>", lambda args: self.entry_in(self.entradastrCeros))
        self.entradastrCeros.bind("<FocusOut>", lambda args: self.entry_out(self.entradastrCeros, 'Cantidad 0 : ' + UsuarioAdministrador.cabeza.strCeros))
        self.entradastrCeros.place(x=220, y=287)
        
        self.ButtonOK = Button(self.master, text= 'OK',activebackground='#1D1A1A', command=lambda:self.AceptarCeros(),activeforeground='white',  bg='white', font=('Arial', 10,'bold'))
        self.ButtonOK.place(x=240, y=327)
        #Boton salida
        self.ruta_boton_salida = 'Images/off.png'
        self.program_directory = sys.path[0]
        self.imagen_boton_salida = PhotoImage(file=os.path.join(self.program_directory, self.ruta_boton_salida)).subsample(10)
        boton_salida = Button(self.master, image=self.imagen_boton_salida, text='Cerrar Sesion', compound=LEFT, bg='#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A', command=lambda:self.regresar(), width=140)
        boton_salida.place(x=95, y=430)
        boton_GeneracionBloque = Button(self.master, text='Crear Bloque', bg='#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A', command=lambda:self.CrearBloque())
        boton_GeneracionBloque.place(x=95, y=390)

#-----------------------------Clase Usuario Administrador-----------------------------
#-----------------------------Clase Usuario Administrador-----------------------------
#-----------------------------Clase Usuario Administrador-----------------------------
#-----------------------------Clase Usuario Administrador-----------------------------

#-----------------------------Clase Registrar Usuario-----------------------------
#-----------------------------Clase Registrar Usuario-----------------------------
#-----------------------------Clase Registrar Usuario-----------------------------
#-----------------------------Clase Registrar Usuario-----------------------------

class Registro(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.user_marcar = "Ingresar Usuario"
        self.contra_marcar = "Ingresar Password"
        self.id_marcar = "Ingresar ID"
        self.edad_marcar = "Ingresar Edad"
        self.money_marcar = "Ingresar Cant. Monedas"
        self.widgets_register()
        
    #----------------------------------Entradas-------------------------------------
    #----------------------------------Entradas-------------------------------------
    #----------------------------------Entradas-------------------------------------
    #----------------------------------Entradas-------------------------------------
    
    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) ==0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
        if self.entry3.get() != 'Ingresar Password':
            self.entry3['show'] = ""
        if self.entry3.get() != 'Ingresar ID':
            self.entry3['show'] = "*"
        if self.entry3.get() != 'Ingresar Edad':
            self.entry3['show'] = "*"
        if self.entry3.get() != 'Ingresar Cant. Monedas':
            self.entry3['show'] = "*"
        if self.entry3.get() != 'Ingresar Usuario':
            self.entry3['show'] = "*"
            
    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
        if self.entry3.get() != 'Ingresar Password':
            self.entry3['show'] = "*"
        if self.entry3.get() == 'Ingresar Password':
            self.entry3['show'] = ""
    
    #----------------------------------Entradas-------------------------------------
    #----------------------------------Entradas-------------------------------------
    #----------------------------------Entradas-------------------------------------
    #----------------------------------Entradas-------------------------------------
    
    #------------------------Verificación USR (Registrar)---------------------------
    #------------------------Verificación USR (Registrar)---------------------------
    #------------------------Verificación USR (Registrar)---------------------------
    #------------------------Verificación USR (Registrar)---------------------------
    
    def verificacion_users(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        self.indica3['text'] = ''
        self.indica4['text'] = ''
        self.indica5['text'] = ''
        id_entry = self.entry1.get()
        users_entry = self.entry2.get()
        password_entry = self.entry3.get()
        edad_entry = self.entry4.get()
        moneda_entry = self.entry5.get()
        if id_entry != None and users_entry != None and password_entry != None and edad_entry != None and moneda_entry != None:
            if id_entry.isdigit() == True and users_entry.isalnum() == True and password_entry.isalnum() == True and edad_entry.isdigit() == True and moneda_entry.isdigit() == True:
                id_aceptada = int(id_entry)
                user_aceptado = str(users_entry)
                pass_aceptado = str(password_entry)
                edad_aceptada = int(edad_entry)
                moneda_aceptada = int(moneda_entry)
                ListaUsuariosDB.add(id_aceptada, user_aceptado, pass_aceptado, edad_aceptada, moneda_aceptada)
                print('Usuario Creado con Exito')
                #ListaUsuariosDB.Display()
                self.Regresar()
            if id_entry.isdigit() == False:
                self.indica1['text'] = 'ID NO VALIDO'
            if users_entry.isalnum() == False:
                self.indica2['text'] = 'USUARIO NO VALIDO'
            if password_entry.isalnum() == False:
                self.indica3['text'] = 'PASSWORD NO VALIDA'
            if edad_entry.isdigit() == False:
                self.indica4['text'] = 'EDAD NO VALIDA'
            if moneda_entry.isdigit() == False:
                self.indica5['text'] = 'CANTIDAD NO VALIDA'
    
    #------------------------Verificación USR (Registrar)---------------------------
    #------------------------Verificación USR (Registrar)---------------------------
    #------------------------Verificación USR (Registrar)---------------------------
    #------------------------Verificación USR (Registrar)---------------------------
    
    #----------------------------Widgets Usuario Crear-------------------------------
    #----------------------------Widgets Usuario Crear-------------------------------
    #----------------------------Widgets Usuario Crear-------------------------------
    #----------------------------Widgets Usuario Crear-------------------------------
    
    def widgets_register(self):
        self.ruta = 'k1.png'
        self.program_directory = sys.path[0]
        self.logo = PhotoImage(file=os.path.join(self.program_directory, self.ruta))
        self.logo2 = self.logo.subsample(3)
        #self.imagen = Image.open(self.ruta)
        Label(self.master, image = self.logo2, bg='#1D1A1A',height=150, width=200).pack()
        #ID ID ID ID ID ID ID ID ID ID ID ID ID ID 
        Label(self.master, text='ID', bg='#1D1A1D', fg='white', font= ('Lucida Sans', 16, 'bold'), height=1).place(x=70, y=170)
        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry1.insert(0, self.id_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.id_marcar))
        self.entry1.place(x=5, y=199)
        self.indica1 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica1.place(x=45, y=230)
        #Usuario a Crear
        Label(self.master, text= 'Usuario', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'), height=1).place(x=35, y=260)
        self.entry2 = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry2.insert(0, self.user_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.user_marcar))
        self.entry2.place(x=5, y=289)
        self.indica2 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica2.place(x=27, y=320)
        #Contrasenia y entrada
        Label(self.master, text= 'Contraseña', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'), height=1).place(x=195,y=260)
        self.entry3 = Entry(self.master,font=('Comic Sans MS', 12),justify = 'center',  fg='grey', highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry3.insert(0, self.contra_marcar)
        self.entry3.bind("<FocusIn>", lambda args: self.entry_in(self.entry3))
        self.entry3.bind("<FocusOut>", lambda args: self.entry_out(self.entry3, self.contra_marcar))
        self.entry3.place(x=190,y=289)
        self.indica3 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica3.place(x=205, y=320)
        #Crear Edad
        Label(self.master, text= 'Edad', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'), height=1).place(x=237, y=170)
        self.entry4 = Entry(self.master,font=('Comic Sans MS', 12),justify = 'center',  fg='grey', highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry4.insert(0, self.edad_marcar)
        self.entry4.bind("<FocusIn>", lambda args: self.entry_in(self.entry4))
        self.entry4.bind("<FocusOut>", lambda args: self.entry_out(self.entry4, self.edad_marcar))
        self.entry4.place(x=190, y=199)
        self.indica4 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica4.place(x=220, y=230)
        #Monedas
        Label(self.master, text= 'Monedas', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'), height=1).place(x=30, y=350)
        self.entry5 = Entry(self.master,font=('Comic Sans MS', 12),justify = 'center',  fg='grey', highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry5.insert(0, self.money_marcar)
        self.entry5.bind("<FocusIn>", lambda args: self.entry_in(self.entry5))
        self.entry5.bind("<FocusOut>", lambda args: self.entry_out(self.entry5, self.money_marcar))
        self.entry5.place(x=5, y=379)
        self.indica5 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica5.place(x=20, y=410)
        Button(self.master, text= 'Crear Usuario',  command = self.verificacion_users,activebackground='#1D1A1A',activeforeground='white',  bg='white', font=('Arial', 12,'bold')).place(x=200,y=379)
        bot_reg = Button(self.master, text= 'Regresar', bg='#1D1A1A',activebackground='white',activeforeground='#1D1A1A', bd=0, fg = 'white', font=('Arial', 10,'bold'),command= self.Regresar)
        bot_reg.place(x=5,y=465)
    
    #----------------------------Widgets Usuario Crear-------------------------------
    #----------------------------Widgets Usuario Crear-------------------------------
    #----------------------------Widgets Usuario Crear-------------------------------
    #----------------------------Widgets Usuario Crear-------------------------------
    
    #----------------------------Regresar Menu Principal-------------------------------
    #----------------------------Regresar Menu Principal-------------------------------
    #----------------------------Regresar Menu Principal-------------------------------
    #----------------------------Regresar Menu Principal-------------------------------
    
    def Regresar(self):
        self.master.withdraw()
        self.Ventana_Pric = Toplevel()
        self.Ventana_Pric.config(bg='#1D1A1A')
        self.Ventana_Pric.title("Proyecto Fase 3 - 201906051 (Inicio)")
        ruta = 'Images/IMGF.png'
        program_directory=sys.path[0]
        self.Ventana_Pric.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
        x_wi = 350
        y_he = 500
        xpos = y_he
        ypos = (self.Ventana_Pric.winfo_screenheight() // 2) - (y_he // 2) -25
        #ventana.geometry('350x500+500+50')
        post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
        #print(post)
        self.Ventana_Pric.geometry(post)
        #ventana.overrideredirect(1)
        self.Ventana_Pric.resizable(0,0)
        app = Inicio(self.Ventana_Pric)
        app.mainloop()
    
    #----------------------------Regresar Menu Principal-------------------------------
    #----------------------------Regresar Menu Principal-------------------------------
    #----------------------------Regresar Menu Principal-------------------------------
    #----------------------------Regresar Menu Principal-------------------------------

#-----------------------------Clase Registrar Usuario-----------------------------
#-----------------------------Clase Registrar Usuario-----------------------------
#-----------------------------Clase Registrar Usuario-----------------------------

#-------------CLASE PARA MOSTRAR EL CARRITO DE COMPRAS-------------
#-------------CLASE PARA MOSTRAR EL CARRITO DE COMPRAS-------------
#-------------CLASE PARA MOSTRAR EL CARRITO DE COMPRAS-------------
                   
class CarroVer(Toplevel):
    def __init__(self, callback = None):
        super().__init__()
        self.callback = callback
        self.config(bg="#1D1A1A")
        self.geometry('700x500+300+100')
        self.resizable(0,0)
        cantidad = 0
        self.title('Listado de Compras' )
        self.labelNomPro = Label(self, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 22, 'bold'))
        self.labelNomPro.place(x=170, y=10)
        self.widgets()
        
    def mostrarDatos(self):
        self.preciototal = 0
        self.IDUsuario = ListaUsuariosDB.usuario_act.id
        Listado = ListaUsuariosDB.usuario_act.carrito.cabeza
        NumeroRep = ListaUsuariosDB.usuario_act.cantidad_comprada
        
        #print(NumeroRep)
        if Listado == None:
            return
        else:
            self.preciototal = 0
            registro = self.tabla.get_children()
            for registro in registro:
                self.tabla.delete(registro)
            while Listado != None:
                contador = 1
                
                #print(Listado.id, Listado.nombre, Listado.precio)
                self.tabla.insert('', 'end', text=str(Listado.id), values=(str(Listado.id + self.IDUsuario),Listado.nombre,str(Listado.cantidad),str(Listado.precio)))
                self.preciototal += (Listado.precio * Listado.cantidad)
                Listado = Listado.siguiente
                contador += 1
        self.labelNomPro['text'] = 'Precio Total: ' + str(self.preciototal)
    
    def eliminar(self):
        id_producto = self.entradaEntryDel.get()
        IDUsuario = ListaUsuariosDB.usuario_act.id
        ListaUsuariosDB.eliminarprodDelCarro(int(id_producto))
        self.mostrarDatos()
    
    def cancelandoCompra(self):
        cancelando = "CANCELADO"
        self.callback(cancelando)
        #ListaUsuariosDB.LimpiarCarro()
        self.destroy()
        
    def ComprandoVoy(self):
        UsuarioKey = ListaUsuariosDB.usuario_act.LlaveWallet
        UsuarioAddress = ListaUsuariosDB.usuario_act.WalletUSR
        #print(self.USRWalHex.get())
        #print(self.USRKeyHex.get())
        if str(self.USRWalHex.get()) == UsuarioAddress and str(self.USRKeyHex.get()) == UsuarioKey:
            #print('C')
            comprando = "COMPRA"
            self.callback(self.preciototal)
            self.destroy()
        else:
            print('Clave de Usuario o Llave no Valida\nNo se puede realizar compra')
        #print()
    
    def GenerarHash(self):
        CarroCompras = ListaUsuariosDB.usuario_act.carrito.cabeza
        if CarroCompras == None:
            return
        else:
            while CarroCompras != None:
                TablaHash.insert((CarroCompras.id + self.IDUsuario), CarroCompras.nombre)
                CarroCompras = CarroCompras.siguiente
            TablaHash.grapho()
            TablaHash.limpiar()
    
    def widgets(self):
        self.LabelUsrHex = Label(self, text='Address', bg="#1D1A1A", fg='white')
        self.LabelUsrHex.place(x=570, y=109)
        self.USRWalHex = Entry(self)
        self.USRWalHex.place(x=520, y=139)
        self.LabelUsrHex = Label(self, text='Key', bg="#1D1A1A", fg='white')
        self.LabelUsrHex.place(x=585, y=169)
        self.USRKeyHex = Entry(self)
        self.USRKeyHex.place(x=520, y=199)
        
        
        self.bus = Frame(self ,width=500, height= 395,bg="white")
        self.bus.place(x=5, y=100)
        
        coluns = ('a0', 'a1', 'a2', 'a3')
        self.tabla = ttk.Treeview(self.bus, columns=coluns, show='headings', height=18)
        self.tabla.column("#1", anchor=CENTER, stretch=NO, width=100)
        self.tabla.column("#2", stretch=NO, width=200)
        self.tabla.column("#3", anchor=CENTER,stretch=NO, width=100)
        self.tabla.column("#4", anchor=CENTER,stretch=NO, width=100)
        self.tabla.grid(row=3, column=0, columnspan=4)
        self.tabla.heading('a0', text="ID", anchor=CENTER)
        self.tabla.heading('a1', text="NOMBRE", anchor=CENTER)
        self.tabla.heading('a2', text="CANTIDAD", anchor=CENTER)
        self.tabla.heading('a3', text="PRECIO", anchor=CENTER)
        self.mostrarDatos()
        
        self.LabelIdDel = Label(self, text='ID Eliminar', bg="#1D1A1A", fg='white')
        self.LabelIdDel.place(x=565, y=269)
        self.entradaEntryDel = Entry(self)
        self.entradaEntryDel.place(x=520, y=299)
        self.botonenvio = Button(self, text='Eliminar', command=lambda:self.eliminar(),activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white')
        self.botonenvio.place(x=565, y=330)
        self.BotonComprar = Button(self, text= 'Comprar', command=lambda:self.ComprandoVoy(), activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 9,'bold'))
        self.BotonComprar.place(x=520, y=400)
        self.BotonCancelarCompra = Button(self, text= 'Cancelar', command=lambda:self.cancelandoCompra(),activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 9,'bold'))
        self.BotonCancelarCompra.place(x=610, y=400)
        self.BotonHashMostrar = Button(self, text= 'Crear Tabla', command=lambda:self.GenerarHash(), activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 9,'bold'))
        self.BotonHashMostrar.place(x=560, y=450)
        
#-------------CLASE PARA MOSTRAR EL CARRITO DE COMPRAS-------------
#-------------CLASE PARA MOSTRAR EL CARRITO DE COMPRAS-------------
#-------------CLASE PARA MOSTRAR EL CARRITO DE COMPRAS-------------

#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------

class VentanaProducto(Toplevel):
    def __init__(self, id, precio, nombre, src, categoria, monedausuario, callback=None):
        super().__init__()
        self.callback = callback
        self.config(bg="#1D1A1A")
        self.geometry('500x500+500+100')
        self.resizable(0,0)
        self.title('Articulo: ' + nombre  + ' \-°-/ Categoria: ' + categoria)
        self.labelNomPro = Label(self, text='Articulo: '+nombre, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 22, 'bold'))
        self.labelNomPro.place(x=140, y=10)
        self.monedasusuario = monedausuario
        self.precioproducto = precio
        self.labelmonedasusuario = Label(self, text='Tokens Usuario: ' + str(monedausuario), bg="#1D1A1A", fg='white')
        self.labelmonedasusuario.place(x=320, y=250)
        #imagen
        self.rutaimagenprod = src
        self.program_directory = sys.path[0]
        self.Imagen = PhotoImage(file=os.path.join(self.program_directory, self.rutaimagenprod))
        self.logo = self.Imagen.subsample(2)
        self.img = Label(self, image=self.logo, bg='#1D1A1A',height=150, width=240)
        self.img.place(x=140, y=80)
        self.preciolab = Label(self, text='Costo: ' + str(precio)+ ' Tokens', bg='#1D1A1A', fg='white')
        self.preciolab.place(x=50, y=250)
        self.entradacosto = Entry(self)
        self.entradacosto.place(x=250, y=299)
        self.labelcosto = Label(self, text='Cantidad a comprar', bg="#1D1A1A", fg='white')
        self.labelcosto.place(x=100, y=300)
        self.botonenvio = Button(self, text='Añadir', command=self.Compra)
        self.botonenvio.place(x=240, y=440)

    def Compra(self):
        cantidades = self.entradacosto.get()
        #print(cantidades)
        if cantidades != None:
            if cantidades.isdigit() == True:
                cantidadaceptada = int(cantidades)
                self.total = cantidadaceptada * int(self.precioproducto)
                #print(self.total)
                self.reducido = self.monedasusuario - self.total
                if self.reducido > 0:
                    self.callback(cantidades)
                    self.destroy()
                else:
                    print('Tokens Insuficientes')        
                
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------

#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------

class Secundaria(Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.usuarioeliminado = False
        self.NoImagenMostrada = ListaUsuariosDB.obtenercantidadjugadas()
        self.DataArchivo = data
        self.UsuarioNombre = ListaUsuariosDB.nombreUsuario()
        self.UsuarioID = ListaUsuariosDB.idUsuario()
        self.UsuarioMoned = ListaUsuariosDB.monedasUsuario()
        self.UsuarioPass = ListaUsuariosDB.passUsuario()
        self.UsuarioPassEncrypt = ListaUsuariosDB.passEncrypt()
        self.UsuarioEdad = ListaUsuariosDB.edadUsuario()
        self.PartidasJugadas = ListaUsuariosDB.obtenercantidadjugadas()
        
        #self.m = None
        self.coordenadas_usadas = []
        self.jugadaNo = None
        self.m = 0
        self.numeroPortaviones = 0
        self.numeroSubmarinos = 0
        self.numeroDestructores = 0
        self.numeroBuques = 0
        
        self.contadorPortavionesPJ1 = 1
        self.contadorSubmarinosPJ1 = 1
        self.contadorDestructoresPJ1 = 1
        self.contadorBuquesPJ1 = 1
        
        self.contadorPortavionesPJ2 = 1
        self.contadorSubmarinosPJ2 = 1
        self.contadorDestructoresPJ2 = 1
        self.contadorBuquesPJ2 = 1
        
        self.numeroPortaPJ1 = 0
        self.numeroSubmaPJ1 = 0
        self.numeroDestrPJ1 = 0
        self.numeroBuquePJ1 = 0
        
        self.numeroPortaPJ2 = 0
        self.numeroSubmaPJ2 = 0
        self.numeroDestrPJ2 = 0
        self.numeroBuquePJ2 = 0
        
        self.valori = 1
        
        self.MovimientosNPC = []
        
        self.secioniniciada = False
        
        self.CantidadComprasUsuario = ""
        self.CantidadComprasUsuario_sinArreglar = ""
        
        self.CasillasTab1 = []
        self.CasillasTab2 = []
        
        self.PosicionesPJ1 = []
        self.PosicionesPJ2 = []
        
        self.sicompro = False
        self.cancelocompra = False
        
        self.PJ1Port = []
        self.PJ1Subm = []
        self.PJ1Dest = []
        self.PJ1Buqu = []
        
        self.PJ2Port = []
        self.PJ2Subm = []
        self.PJ2Dest = []
        self.PJ2Buqu = []
        
        self.JugadorVsJugador = False
        self.JugadorVsNPC = False
        self.TurnoNonPlayerComputer = False
        
        self.contadorCompras = 0
        
        self.totalcompra = 0
        
        self.restante = 0
        
        self.widgets_sec()
        
    #-----------------------Salida del Usuario-----------------------
    #-----------------------Salida del Usuario-----------------------
    #-----------------------Salida del Usuario-----------------------
    
    def regresar(self):
        if self.usuarioeliminado == False:
            if self.m != 0:
                TableroPJ1.EliminarTodo()
                TableroPJ2.EliminarTodo()
                TableroPJ1.eliminarTabGanador()
                TableroPJ2.eliminarTabGanador()
                MiniTablerodePJ1.EliminarTodo()
                MiniTablerodePJ2.EliminarTodo()
                MiniTablerodePJ1.eliminarTabGanador()
                MiniTablerodePJ2.eliminarTabGanador()
            Bloques.toJson()
            Bloques.graphosBlock()
            PortavionesPJ1.eliminarTodosBarcos()
            PortavionesPJ2.eliminarTodosBarcos()
            SubmarinosPJ1.eliminarTodosBarcos()
            SubmarinosPJ2.eliminarTodosBarcos()
            DestructoresPJ1.eliminarTodosBarcos()
            DestructoresPJ2.eliminarTodosBarcos()
            BuquesPJ1.eliminarTodosBarcos()
            BuquesPJ2.eliminarTodosBarcos()
            ListaUsuariosDB.salirjugador2()
            self.restante = 0
            self.secioniniciada = False
            self.master.withdraw()
            print('Cerrando Secion')
            self.Ventana_principal = Toplevel()
            self.Ventana_principal.config(bg='#1D1A1A')
            self.Ventana_principal.title("Proyecto Fase 3 - 201906051 (Inicio)")
            ruta = 'Images/IMGF.png'
            program_directory=sys.path[0]
            self.Ventana_principal.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
            x_wi = 350
            y_he = 500
            xpos = y_he
            ypos = (ventana.winfo_screenheight() // 2) - (y_he // 2) -25
            post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
            self.Ventana_principal.geometry(post)
            self.Ventana_principal.resizable(0,0)
            app = Inicio(self.Ventana_principal)
            app.mainloop()
        else: 
            self.usuarioeliminado = False
            #ListaUsuariosDB.Display()
            if self.m != 0:  
                TableroPJ1.EliminarTodo()
                TableroPJ2.EliminarTodo()
                TableroPJ1.eliminarTabGanador()
                TableroPJ2.eliminarTabGanador()
                MiniTablerodePJ1.EliminarTodo()
                MiniTablerodePJ2.EliminarTodo()
                MiniTablerodePJ1.eliminarTabGanador()
                MiniTablerodePJ2.eliminarTabGanador()
            Bloques.toJson()
            Bloques.graphosBlock()
            
            PortavionesPJ1.eliminarTodosBarcos()
            PortavionesPJ2.eliminarTodosBarcos()
            SubmarinosPJ1.eliminarTodosBarcos()
            SubmarinosPJ2.eliminarTodosBarcos()
            DestructoresPJ1.eliminarTodosBarcos()
            DestructoresPJ2.eliminarTodosBarcos()
            BuquesPJ1.eliminarTodosBarcos()
            BuquesPJ2.eliminarTodosBarcos()
            ListaUsuariosDB.cerrarSecion()
            ListaUsuariosDB.cerrarSecion()
            self.secioniniciada = False
            ListaUsuariosDB.usuario_act = None
            ListaUsuariosDB.salirjugador2()
            self.restante = 0
            #messagebox.showinfo(message='Saliendo del Usuario\nSe estan generando los bloques (Puede demorar un tiempo)')
            self.master.withdraw()
            self.secioniniciada = False
            self.restante = 0
            print('Usuario Eliminado - Cerrando Secion')
            self.Ventana_principal = Toplevel()
            self.Ventana_principal.config(bg='#1D1A1A')
            self.Ventana_principal.title("Proyecto Fase 3 - 201906051 (Inicio)")
            ruta = 'Images/IMGF.png'
            program_directory=sys.path[0]
            self.Ventana_principal.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
            x_wi = 350
            y_he = 500
            xpos = y_he
            ypos = (ventana.winfo_screenheight() // 2) - (y_he // 2) -25
            post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
            self.Ventana_principal.geometry(post)
            self.Ventana_principal.resizable(0,0)
            app = Inicio(self.Ventana_principal)
            app.mainloop()
            
    #-----------------------Salida del Usuario-----------------------
    #-----------------------Salida del Usuario-----------------------
    #-----------------------Salida del Usuario-----------------------
    
    #----------------------------Entradas----------------------------
    #----------------------------Entradas----------------------------
    #----------------------------Entradas----------------------------
    
    def entry_out2(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
        if self.entradaIDProd.get() != 'Ingresar Producto':
            self.entradaIDProd['show'] = ""
            
    def entry_in_XY(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
    
    def entry_out_XY(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
            
    def entry_in2(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
            
    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) ==0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
            
        if self.entradaID.get() != 'Ingresar ID':
            self.entradaID['show'] = ""
        if self.entradaEdad.get() != 'Ingresar Edad':
            self.entradaEdad['show'] = ""
        if self.entradaNom.get() != 'Ingresar Usuario':
            self.entradaNom['show'] = ""
        if self.entradaPass.get() != 'Ingresar Password':
            self.entradaPass['show'] = ""
        if self.entradaMon.get() != 'Ingresar Cant. Monedas':
            self.entradaMon['show'] = ""
        if self.entradaIDProd.get() != 'Ingresar ID':
            self.entradaIDProd['show'] = ""
         
    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
        if self.entradaPass.get() == 'Ingresar Password':
            self.entradaPass['show'] = ""
            
    #----------------------------Entradas----------------------------
    #----------------------------Entradas----------------------------
    #----------------------------Entradas----------------------------
    
    #----------------------Desbloqueo o Bloqueo Casillas/Botones----------------------
    #----------------------Desbloqueo o Bloqueo Casillas/Botones----------------------
    #----------------------Desbloqueo o Bloqueo Casillas/Botones----------------------
    
    def DesbloquearCasillas(self):
        self.entradaID.config(state='normal')
        self.entradaEdad.config(state='normal')
        self.entradaNom.config(state='normal')
        self.entradaPass.config(state='normal')
        self.entradaMon.config(state='normal')
        self.botonmodificar.config(state='normal')
        self.botondesbloquear.config(state='disabled')
    
    def BloquearCasillas(self):
        self.entradaID.config(state='disabled')
        self.entradaEdad.config(state='disabled')
        self.entradaNom.config(state='disabled')
        self.entradaPass.config(state='disabled')
        self.entradaMon.config(state='disabled')
        self.botonmodificar.config(state='disabled')
        self.botondesbloquear.config(state='normal')
    
    def DesbloquearPositionOP(self):
        print()
    
    #----------------------Desbloqueo o Bloqueo Casillas/Botones----------------------
    #----------------------Desbloqueo o Bloqueo Casillas/Botones----------------------
    #----------------------Desbloqueo o Bloqueo Casillas/Botones----------------------
    
    #-------------------------Verificación Eliminación Buque-------------------------
    #-------------------------Verificación Eliminación Buque-------------------------
    #-------------------------Verificación Eliminación Buque-------------------------
    
    def RestandoBuquesP2(self):
        #Portaviones
        if self.numeroPortaPJ2 > PortavionesPJ2.Barcos_Vivos:
            conteo = self.numeroPortaPJ2 - PortavionesPJ2.Barcos_Vivos
            self.numeroPortaPJ2 = self.numeroPortaPJ2 - conteo
            print('Portavion PJ2 Caido - Restantes: ', self.numeroPortaPJ2)
            ListaUsuariosDB.GanarPorHundir()
            self.refrescar()
        
        #Submarinos
        if self.numeroSubmaPJ2 > SubmarinosPJ2.Barcos_Vivos:
            conteo = self.numeroSubmaPJ2 - SubmarinosPJ2.Barcos_Vivos
            self.numeroSubmaPJ2 = self.numeroSubmaPJ2 - conteo
            print('Submarino PJ2 Caido - Restantes: ', self.numeroSubmaPJ2)
            ListaUsuariosDB.GanarPorHundir()
            self.refrescar()
        
        #Destructores
        if self.numeroDestrPJ2 > DestructoresPJ2.Barcos_Vivos:
            conteo = self.numeroDestrPJ2 - DestructoresPJ2.Barcos_Vivos
            self.numeroDestrPJ2 = self.numeroDestrPJ2 - conteo
            print('Destructor PJ2 Caido - Restantes: ', self.numeroDestrPJ2)
            ListaUsuariosDB.GanarPorHundir()
            self.refrescar()
        
        #Buques
        if self.numeroBuquePJ2 > BuquesPJ2.Barcos_Vivos:
            conteo = self.numeroBuquePJ2 - BuquesPJ2.Barcos_Vivos
            self.numeroBuquePJ2 = self.numeroBuquePJ2 - conteo
            print('Buque PJ2 Caido - Restantes: ', self.numeroBuquePJ2)
            ListaUsuariosDB.GanarPorHundir()
            self.refrescar()
            
        
    def RestandoBuquesP1(self):
        #Portaviones
        if self.numeroPortaPJ1 > PortavionesPJ1.Barcos_Vivos:
            conteo = self.numeroPortaPJ1 - PortavionesPJ1.Barcos_Vivos
            self.numeroPortaPJ1 = self.numeroPortaPJ1 - conteo
            print('Portavion PJ1 Caido - Restantes: ', self.numeroPortaPJ1)
            ListaUsuariosDB.GanarHundirjugador2()
            self.refrescar()
    
        #Submarinos
        if self.numeroSubmaPJ1 > SubmarinosPJ1.Barcos_Vivos:
            conteo = self.numeroSubmaPJ1 - SubmarinosPJ1.Barcos_Vivos
            self.numeroSubmaPJ1 = self.numeroSubmaPJ1 - conteo
            print('Submarino PJ1 Caido - Restantes: ', self.numeroSubmaPJ1)
            ListaUsuariosDB.GanarHundirjugador2()
            self.refrescar()
        
        #Destructores
        if self.numeroDestrPJ1 > DestructoresPJ1.Barcos_Vivos:
            conteo = self.numeroDestrPJ1 - DestructoresPJ1.Barcos_Vivos
            self.numeroDestrPJ1 = self.numeroDestrPJ1 - conteo
            print('Destructor PJ1 Caido - Restantes: ', self.numeroDestrPJ1)
            ListaUsuariosDB.GanarHundirjugador2()
            self.refrescar()
        
        #Buques
        if self.numeroBuquePJ1 > BuquesPJ1.Barcos_Vivos:
            conteo = self.numeroBuquePJ1 - BuquesPJ1.Barcos_Vivos
            self.numeroBuquePJ1 = self.numeroBuquePJ1 - conteo
            print('Buque PJ1 Caido - Restantes: ', self.numeroBuquePJ1)
            ListaUsuariosDB.GanarHundirjugador2()
            self.refrescar()
            
    #-------------------------Verificación Eliminación Buque-------------------------
    #-------------------------Verificación Eliminación Buque-------------------------
    #-------------------------Verificación Eliminación Buque-------------------------
    
    def EliminarUsuario(self):
        ListaUsuariosDB.eliminarUsuario(self.UsuarioID)
        self.usuarioeliminado = True
        self.regresar()
    
    def Cambiar(self):
        NuevaID = self.entradaID.get()
        NuevoUsuario = self.entradaNom.get()
        NuevaEdad = self.entradaEdad.get()
        NuevaPass = self.entradaPass.get()
        NuevosTokens = self.entradaMon.get()
        if(NuevaID != None and NuevoUsuario != None and NuevaEdad != None and NuevaPass != None and NuevosTokens != None):
            if NuevaID.isdigit() == True and NuevoUsuario.isalnum() == True and NuevaEdad.isdigit() == True and NuevaPass.isalnum() == True and NuevosTokens.isdigit() == True:
                IDAceptada = int(NuevaID)
                UsuarioAceptado = str(NuevoUsuario)
                EdadAceptada = int(NuevaEdad)
                PassAceptada = str(NuevaPass)
                TokenAceptado = int(NuevosTokens)
                ListaUsuariosDB.modificarUsuario(IDAceptada, UsuarioAceptado, PassAceptada, EdadAceptada, TokenAceptado)
                self.BloquearCasillas()
                self.refrescar()
                print('Usuario Modificado Correctamente')
                #self.regresar()
                
    def SeleccionMandar(self):
        ListaUsuariosDB.DisplayCarrito()
        
    def GrafoAdyacencia(self):
        TableroPJ2.graficarTabGanador()
        
    #---------------------------Añadir al Carrito---------------------------
    #---------------------------Añadir al Carrito---------------------------
    #---------------------------Añadir al Carrito---------------------------
    #---------------------------Añadir al Carrito---------------------------
    
    def cantidad(self, cantidad):
        now = datetime.now()
        self.total = cantidad * self.PrecioArticulo
        #print(self.total)
        #print('{}::{}:{}:{}'.format(now.date(), now.hour, now.minute, now.second))
        ahoradate = '{}d{}m{}y'.format(now.day, now.month, now.year)
        ahorahor = '{}h{}m{}s'.format(now.hour, now.minute, now.second)
        ahora = ahoradate + ahorahor
        ListaUsuariosDB.AgregarCompra(int(self.IDArticulo), self.NombreArticulo, self.CategoriaArticulo, int(self.PrecioArticulo), int(cantidad), ahora)
        ListaArticulosPrim.deseleccionarArticulo()
        #print(ListaUsuariosDB.usuario_act.carrito.cabeza.precio)
        #Aqui se quita lo de las monedas para que no reste al usuario si no compra
        #######ES ↓ donde se restan monedas
        #ListaUsuariosDB.RestandoMonedas(int(self.PrecioArticulo), int(cantidad))
        ######Nuevo ↓
        #ListaUsuariosDB.RestandoPerCompra(total)
        ListaUsuariosDB.ModificarMonedas()
        #ListaUsuariosDB.Display()
        self.refrescar()
        self.refrescarCarrito()
    
    def BuscarProducto(self):
        #print(self.UsuarioID)
        ProductoID = self.entradaIDProd.get()
        if ProductoID != None:
            if ProductoID.isdigit() == True:
                ProductoAceptado = int(ProductoID)
                ListaArticulosPrim.BuscarArticulo(ProductoAceptado)
                #self.cantidad = None#
                
                self.IDArticulo = ListaArticulosPrim.IDArticuloSeleccionado()
                self.PrecioArticulo = ListaArticulosPrim.precioArticuloSeleccionado()
                self.NombreArticulo = ListaArticulosPrim.nombreArticuloSeleccionado()
                self.SRCArticulo = ListaArticulosPrim.srcArticuloSeleccionado()
                self.CategoriaArticulo = ListaArticulosPrim.categoriaArticuloSeleccionado()
                self.ventanaProducto = VentanaProducto(self.IDArticulo, self.PrecioArticulo, self.NombreArticulo, self.SRCArticulo, self.CategoriaArticulo, ListaUsuariosDB.monedasUsuario(), callback=self.cantidad)
                #print(self.cantidad)
    
    def obtencion(self, obtencion):
        #print(obtencion)
        if obtencion == 'CANCELADO':
            ListaUsuariosDB.LimpiarCarro()
            print('Compra Cancelada')
            self.cancelocompra = True
            self.refrescarCarrito()
            self.refrescarCarrito()
        if obtencion != "CANCELADO":
            preciocompra = 0
            ListaUsuariosDB.RestandoPerCompra(obtencion)
            #print(obtencion)
            self.sicompro = True
            compradada = ListaUsuariosDB.usuario_act.carrito.cabeza
            if compradada == None:
                return
            else:
                DATA_Wallet = ""
                Data_Wal_sinAjust = ""
                while compradada != None:
                    DATA_Wallet += "{\\nSKIN:"+str(compradada.id)+",\\nVALUE:"+str(compradada.precio)+"},"
                    Data_Wal_sinAjust += "\t{\n\t\t\"SKIN\":" + str(compradada.id) + ",\n\t\t\"VALUE\":" + str(compradada.precio) + "\n\t},\n"
                    compradada = compradada.siguiente
                compradada2 = ListaUsuariosDB.usuario_act.carrito.cabeza
                self.CantidadComprasUsuario += DATA_Wallet
                self.CantidadComprasUsuario_sinArreglar += Data_Wal_sinAjust
                Data_Merkle = ""
                while compradada2.siguiente != None:
                    Data_Merkle += "{}a{}b".format(compradada2.id, compradada2.horafecha)
                    compradada2 = compradada2.siguiente
                Data_Merkle += "{}a{}".format(compradada2.id, compradada2.horafecha)
                #print(DATA_Wallet)
                #print(Data_Merkle)
                MerkleTree.add(Data_Merkle)
                
            ListaUsuariosDB.LimpiarCarro()
            self.refrescarCarrito()
            self.refrescar()
            
    def CarritoVer(self):
        self.ventanaCarro = CarroVer(callback = self.obtencion)
        #print()
    
    #---------------------------Añadir al Carrito---------------------------
    #---------------------------Añadir al Carrito---------------------------
    #---------------------------Añadir al Carrito---------------------------
    
    def refrescarTableroPJ2(self):
        self.rutaTablero2 = 'Images/TabPJ2.png'
        self.logoTablero2 = Image.open(self.rutaTablero2)
        self.resizeTab2 = self.logoTablero2.resize((558,558))
        self.ImageTKTAB2 = ImageTk.PhotoImage(self.resizeTab2)
        self.LabelTablero2['image'] = self.ImageTKTAB2
        
        self.rutaMinTab2 = 'Images/MinTabPJ2.png'
        self.LogoMinTab2 = Image.open(self.rutaMinTab2)
        self.resizeminTabPJ2 = self.LogoMinTab2.resize((300,300))
        self.ImageTKMinTAB2 = ImageTk.PhotoImage(self.resizeminTabPJ2)
        self.LabelMinTab2['image'] = self.ImageTKMinTAB2
    
    def refrescarTableroPJ1(self):
        self.rutaTablero = 'Images/TabPJ1.png'
        self.logoTablero = Image.open(self.rutaTablero)
        self.resizeTab = self.logoTablero.resize((558,558))
        self.ImageTKTAB = ImageTk.PhotoImage(self.resizeTab)
        self.LabelTablero['image'] = self.ImageTKTAB
        
        self.rutaMinTab1 = 'Images/MinTabPJ1.png'
        self.LogoMinTab1 = Image.open(self.rutaMinTab1)
        self.resizeminTabPJ1 = self.LogoMinTab1.resize((300,300))
        self.ImageTKMinTAB1 = ImageTk.PhotoImage(self.resizeminTabPJ1)
        self.LabelMinTab1['image'] = self.ImageTKMinTAB1
        
    def refrescarTablero(self):
        self.rutaTablero = 'Images/TabPJ1.png'
        self.logoTablero = Image.open(self.rutaTablero)
        self.resizeTab = self.logoTablero.resize((558,558))
        self.ImageTKTAB = ImageTk.PhotoImage(self.resizeTab)
        self.LabelTablero['image'] = self.ImageTKTAB
        
        self.rutaTablero2 = 'Images/TabPJ2.png'
        self.logoTablero2 = Image.open(self.rutaTablero2)
        self.resizeTab2 = self.logoTablero2.resize((558,558))
        self.ImageTKTAB2 = ImageTk.PhotoImage(self.resizeTab2)
        self.LabelTablero2['image'] = self.ImageTKTAB2
        
        self.rutaMinTab1 = 'Images/MinTabPJ1.png'
        self.LogoMinTab1 = Image.open(self.rutaMinTab1)
        self.resizeminTabPJ1 = self.LogoMinTab1.resize((300,300))
        self.ImageTKMinTAB1 = ImageTk.PhotoImage(self.resizeminTabPJ1)
        self.LabelMinTab1['image'] = self.ImageTKMinTAB1
        
        self.rutaMinTab2 = 'Images/MinTabPJ2.png'
        self.LogoMinTab2 = Image.open(self.rutaMinTab2)
        self.resizeminTabPJ2 = self.LogoMinTab2.resize((300,300))
        self.ImageTKMinTAB2 = ImageTk.PhotoImage(self.resizeminTabPJ2)
        self.LabelMinTab2['image'] = self.ImageTKMinTAB2
        
    
    def refrescarCarrito(self):
        CarroActual = ListaUsuariosDB.usuario_act.carrito
        compra = 0
        costototal = 0
        if CarroActual.cabeza != None:
            compra = 0
            costototal = 0
            temp = CarroActual.cabeza
            while temp != None:
                costototal += temp.precio * temp.cantidad
                compra += 1
                temp = temp.siguiente
        #print(compra, costototal)
        self.BotonCarritoUsU['text'] = str(compra)
        self.totalcompra = costototal
        self.LabelCarritoUsU['text'] = '$ ' + str(costototal)
    
    def refrescar(self):
        self.nombreLabel['text'] = ListaUsuariosDB.nombreUsuario()
        self.UsuarioNombre = ListaUsuariosDB.nombreUsuario()
        self.UsuarioID = ListaUsuariosDB.idUsuario()
        self.monedasLAbel['text'] = 'Tokens: '+str(ListaUsuariosDB.monedasUsuario())
        self.LabelMoneyPJ1['text'] = 'Tokens: ' + str(ListaUsuariosDB.monedasUsuario())
        #print(ListaUsuariosDB.usuario_act.carrito.cabeza.precio)
        
        if ListaUsuariosDB.usuario_secundario != None:
            self.LabelMoneyPJ2['text'] = 'Tokens: ' + str(ListaUsuariosDB.monedasjugador2())
            self.LabelPJ2NPCorPJ2['text'] = 'Usuario: ' + ListaUsuariosDB.nombrejugador2()
    
    def refrescarBarcosPJ1(self):
        PortavionesPJ1.Barcos_En_Pie()
        SubmarinosPJ1.Barcos_En_Pie()
        DestructoresPJ1.Barcos_En_Pie()
        BuquesPJ1.Barcos_En_Pie()
        self.RestandoBuquesP1()
        PortavionesPJ1.Barcos_Caidos()
        SubmarinosPJ1.Barcos_Caidos()
        DestructoresPJ1.Barcos_Caidos()
        BuquesPJ1.Barcos_Caidos()
        conteoPorta = PortavionesPJ1.Barcos_Hundidos
        conteoSubma = SubmarinosPJ1.Barcos_Hundidos
        conteoDestr = DestructoresPJ1.Barcos_Hundidos
        conteoBuque = BuquesPJ1.Barcos_Hundidos
        #print(conteoBuque)
        self.LabelBarcosInGamePJ1['text'] = 'Portaviones (in Game): \t' + str(PortavionesPJ1.Barcos_Vivos) + '\nSubmarinos (in Game): \t' + str(SubmarinosPJ1.Barcos_Vivos) + '\nDestructores (in Game): \t' + str(DestructoresPJ1.Barcos_Vivos) + '\nBuques (in Game): \t' + str(BuquesPJ1.Barcos_Vivos)
        if PortavionesPJ1.Barcos_Vivos == 0 and SubmarinosPJ1.Barcos_Vivos == 0 and DestructoresPJ1.Barcos_Vivos == 0 and BuquesPJ1.Barcos_Vivos == 0:
            self.LabelGanOPerd['text'] = 'Pierde Jugador 1'
            self.LabelGanOPerd2['text'] = 'Pierde Jugador 1'
            TableroPJ2.graficarTabGanador()
            #self.LabelBarcosInGamePJ2['text'] = 'Portaviones Destruidos: \t' + str(conteoPorta) + '\nSubmarinos Destruidos: \t' + str(conteoSubma) + '\nDestructores Destruidos: \t' + str(conteoDestr) + '\nBuques Destruidos: \t' + str(conteoBuque)
            self.refrescarBarcos()
            self.EntryPosX.config(state='disabled')
            self.EntryPosY.config(state='disabled')
            self.ButonXY.config(state='disabled')
            if self.JugadorVsJugador == True:
                self.EntryPosX2.config(state='disabled')
                self.EntryPosY2.config(state='disabled')
                self.ButonXY2.config(state='disabled')
            
    def refrescarBarcosPJ2(self):
        PortavionesPJ2.Barcos_En_Pie()
        SubmarinosPJ2.Barcos_En_Pie()
        DestructoresPJ2.Barcos_En_Pie()
        BuquesPJ2.Barcos_En_Pie()
        self.RestandoBuquesP2()
        PortavionesPJ2.Barcos_Caidos()
        SubmarinosPJ2.Barcos_Caidos()
        DestructoresPJ2.Barcos_Caidos()
        BuquesPJ2.Barcos_Caidos()
        conteoPorta = PortavionesPJ2.Barcos_Hundidos
        conteoSubma = SubmarinosPJ2.Barcos_Hundidos
        conteoDestr = DestructoresPJ2.Barcos_Hundidos
        conteoBuque = BuquesPJ2.Barcos_Hundidos
        #print(conteoBuque)
        self.LabelBarcosInGamePJ2['text'] = 'Portaviones (in Game): \t' + str(PortavionesPJ2.Barcos_Vivos) + '\nSubmarinos (in Game): \t' + str(SubmarinosPJ2.Barcos_Vivos) + '\nDestructores (in Game): \t' + str(DestructoresPJ2.Barcos_Vivos) + '\nBuques (in Game): \t' + str(BuquesPJ2.Barcos_Vivos)
        if PortavionesPJ2.Barcos_Vivos == 0 and SubmarinosPJ2.Barcos_Vivos == 0 and DestructoresPJ2.Barcos_Vivos == 0 and BuquesPJ2.Barcos_Vivos == 0:
            self.LabelGanOPerd['text'] = 'Gana Jugador 1'
            self.LabelGanOPerd2['text'] = 'Gana Jugador 1'
            TableroPJ1.graficarTabGanador()
            #self.LabelBarcosInGamePJ1['text'] = 'Portaviones Destruidos: \t' + str(conteoPorta) + '\nSubmarinos Destruidos: \t' + str(conteoSubma) + '\nDestructores Destruidos: \t' + str(conteoDestr) + '\nBuques Destruidos: \t' + str(conteoBuque)
            self.refrescarBarcos()
            self.EntryPosX.config(state='disabled')
            self.EntryPosY.config(state='disabled')
            self.ButonXY.config(state='disabled')
            if self.JugadorVsJugador == True:
                self.EntryPosX2.config(state='disabled')
                self.EntryPosY2.config(state='disabled')
                self.ButonXY2.config(state='disabled')
    
    def refrescarBarcos(self):
        PortavionesPJ1.Barcos_En_Pie()
        PortavionesPJ2.Barcos_En_Pie()
        SubmarinosPJ1.Barcos_En_Pie()
        SubmarinosPJ2.Barcos_En_Pie()
        DestructoresPJ1.Barcos_En_Pie()
        DestructoresPJ2.Barcos_En_Pie()
        BuquesPJ1.Barcos_En_Pie()
        BuquesPJ2.Barcos_En_Pie()
        PortavionesPJ1.Barcos_Caidos()
        PortavionesPJ2.Barcos_Caidos()
        SubmarinosPJ1.Barcos_Caidos()
        SubmarinosPJ2.Barcos_Caidos()
        DestructoresPJ1.Barcos_Caidos()
        DestructoresPJ2.Barcos_Caidos()
        BuquesPJ1.Barcos_Caidos()
        BuquesPJ2.Barcos_Caidos()
        conteoPorta2 = PortavionesPJ2.Barcos_Hundidos
        conteoSubma2 = SubmarinosPJ2.Barcos_Hundidos
        conteoDestr2 = DestructoresPJ2.Barcos_Hundidos
        conteoBuque2 = BuquesPJ2.Barcos_Hundidos
        conteoPorta1 = PortavionesPJ1.Barcos_Hundidos
        conteoSubma1 = SubmarinosPJ1.Barcos_Hundidos
        conteoDestr1 = DestructoresPJ1.Barcos_Hundidos
        conteoBuque1 = BuquesPJ1.Barcos_Hundidos
        self.LabelBarcosInGamePJ1['text'] = 'Portaviones (in Game): \t' + str(PortavionesPJ1.Barcos_Vivos) + '\nSubmarinos (in Game): \t' + str(SubmarinosPJ1.Barcos_Vivos) + '\nDestructores (in Game): \t' + str(DestructoresPJ1.Barcos_Vivos) + '\nBuques (in Game): \t' + str(BuquesPJ1.Barcos_Vivos)
        self.LabelBarcosInGamePJ2['text'] = 'Portaviones (in Game): \t' + str(PortavionesPJ2.Barcos_Vivos) + '\nSubmarinos (in Game): \t' + str(SubmarinosPJ2.Barcos_Vivos) + '\nDestructores (in Game): \t' + str(DestructoresPJ2.Barcos_Vivos) + '\nBuques (in Game): \t' + str(BuquesPJ2.Barcos_Vivos)
        
        if PortavionesPJ1.Barcos_Vivos == 0 and SubmarinosPJ1.Barcos_Vivos == 0 and DestructoresPJ1.Barcos_Vivos == 0 and BuquesPJ1.Barcos_Vivos == 0:
            self.LabelBarcosInGamePJ1['text'] = 'Portaviones (Destruidos): \t' + str(conteoPorta2) + '\nSubmarinos (Destruidos): \t' + str(conteoSubma2) + '\nDestructores (Destruidos): \t' + str(conteoDestr2) + '\nBuques (Destruidos): \t' + str(conteoBuque2)
            self.LabelBarcosInGamePJ2['text'] = 'Portaviones (Destruidos): \t' + str(conteoPorta1) + '\nSubmarinos (Destruidos): \t' + str(conteoSubma1) + '\nDestructores (Destruidos): \t' + str(conteoDestr1) + '\nBuques (Destruidos): \t' + str(conteoBuque1)
        
        if PortavionesPJ2.Barcos_Vivos == 0 and SubmarinosPJ2.Barcos_Vivos == 0 and DestructoresPJ2.Barcos_Vivos == 0 and BuquesPJ2.Barcos_Vivos == 0:
            self.LabelBarcosInGamePJ1['text'] = 'Portaviones (Destruidos): \t' + str(conteoPorta2) + '\nSubmarinos (Destruidos): \t' + str(conteoSubma2) + '\nDestructores (Destruidos): \t' + str(conteoDestr2) + '\nBuques (Destruidos): \t' + str(conteoBuque2)
            self.LabelBarcosInGamePJ2['text'] = 'Portaviones (Destruidos): \t' + str(conteoPorta1) + '\nSubmarinos (Destruidos): \t' + str(conteoSubma1) + '\nDestructores (Destruidos): \t' + str(conteoDestr1) + '\nBuques (Destruidos): \t' + str(conteoBuque1)
        
        
    #--------------------------------Agregar Piezas--------------------------------
    #--------------------------------Agregar Piezas--------------------------------
    #--------------------------------Agregar Piezas--------------------------------
    #--------------------------------Agregar Piezas-------------------------------- 
    
        #----------------------------------Tablero PJ1----------------------------------
        #----------------------------------Tablero PJ1----------------------------------
        #----------------------------------Tablero PJ1----------------------------------
        
    def PortavionesCasillasPJ1(self, objeto):
        PortavionesPJ1.agregarBarco('Portaviones')
        if objeto['x'] == self.m:
            for i in self.CasillasTab1:
                if i['x'] - 3 == objeto['x'] - 3 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 3
                    while vari <= self.m:
                        PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                        self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                
        if objeto['x'] == self.m - 1:
            for i in self.CasillasTab1:
                if i['x'] - 2 == objeto['x'] - 2 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 2
                    while vari <= self.m:
                        PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                        self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                    
        if objeto['x'] == self.m - 2:
            for i in self.CasillasTab1:
                if i['x'] - 1 == objeto['x'] - 1 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 1
                    while vari <= self.m:
                        PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                        self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                    
        if objeto['x'] <= self.m - 3:
            for i in self.CasillasTab1:
                if i['x'] == objeto['x'] and i['x'] + 3 == objeto['x'] + 3 and i['y'] == objeto['y']:
                    vari = objeto['x']
                    valor = objeto['x'] + 3
                    while vari <= valor:
                        PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                        self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                elif (i['x'] - 3 == objeto['x'] - 3) > 0 and i['y'] == objeto['y']:
                    if i['x'] -3 == objeto['x'] - 3 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 3
                        valor = objeto['x']
                        while vari <= valor:
                            PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                            TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                            self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                            vari += 1
                    elif i['x'] - 2 == objeto['x'] - 2 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 2
                        valor = objeto['x'] + 1
                        while vari <= valor:
                            PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                            TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                            self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                            vari += 1
                    elif i['x'] - 1 == objeto['x'] - 1 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 1
                        valor = objeto['x'] + 2
                        while vari <= valor:
                            PortavionesPJ1.agregarCoordenadas(self.contadorPortavionesPJ1, objeto['y'], vari)
                            TableroPJ1.modificar(objeto['y'], vari, 'Level4')
                            self.PJ1Port.append({'x':vari, 'y':objeto['y']})
                            vari += 1
        self.contadorPortavionesPJ1 += 1
        self.numeroPortaPJ1 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ1Port):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab1):
                if self.CasillasTab1[valorsecundario]['x'] == self.PJ1Port[valorinicial]['x'] and self.CasillasTab1[valorsecundario]['y'] == self.PJ1Port[valorinicial]['y']:
                    self.CasillasTab1.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
    
    def SubmarinosCasillasPJ1(self, objeto):
        SubmarinosPJ1.agregarBarco('Submarino')
        if objeto['x'] == self.m:
            for i in self.CasillasTab1:
                if i['x'] - 2 == objeto['x'] - 2 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 2
                    while vari <= self.m:
                        SubmarinosPJ1.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level3')
                        self.PJ1Subm.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                
        if objeto['x'] == self.m - 1:
            for i in self.CasillasTab1:
                if i['x'] - 1 == objeto['x'] - 1 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 1
                    while vari <= self.m:
                        SubmarinosPJ1.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level3')
                        self.PJ1Subm.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                        
        if objeto['x'] <= self.m - 2:
            for i in self.CasillasTab1:
                if i['x'] == objeto['x'] and i['x'] + 2 == objeto['x'] + 2 and i['y'] == objeto['y']:
                    vari = objeto['x']
                    valor = objeto['x'] + 2
                    while vari <= valor:
                        SubmarinosPJ1.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level3')
                        self.PJ1Subm.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                elif (i['x'] - 2 == objeto['x'] - 2) > 0 and i['y'] == objeto['y']:
                    if i['x'] - 2 == objeto['x'] - 2 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 2
                        valor = objeto['x']
                        while vari <= valor:
                            SubmarinosPJ1.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                            TableroPJ1.modificar(objeto['y'], vari, 'Level3')
                            self.PJ1Subm.append({'x':vari, 'y':objeto['y']})
                            vari += 1
                    elif i['x'] - 1 == objeto['x'] - 1 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 1
                        valor = objeto['x'] + 1
                        while vari <= valor:
                            SubmarinosPJ1.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                            TableroPJ1.modificar(objeto['y'], vari, 'Level3')
                            self.PJ1Subm.append({'x':vari, 'y':objeto['y']})
                            vari += 1
        self.contadorSubmarinosPJ1 += 1
        self.numeroSubmaPJ1 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ1Subm):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab1):
                if self.CasillasTab1[valorsecundario]['x'] == self.PJ1Subm[valorinicial]['x'] and self.CasillasTab1[valorsecundario]['y'] == self.PJ1Subm[valorinicial]['y']:
                    self.CasillasTab1.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
            
    def DestructoresCasillasPJ1(self, objeto):
        DestructoresPJ1.agregarBarco('Destructor')
        if objeto['x'] == self.m:
            for i in self.CasillasTab1:
                if i['x'] - 1 == objeto['x'] - 1 and i['y'] == objeto['y']:
                    #print(i['x'])
                    vari = objeto['x'] - 1
                    while vari <= self.m:
                        DestructoresPJ1.agregarCoordenadas(self.contadorDestructoresPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level2')
                        self.PJ1Dest.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                        
        if objeto['x'] <= self.m - 1:
            for i in self.CasillasTab1:
                if i['x'] == objeto['x'] and i['x'] + 1 == objeto['x'] + 1 and i['y'] == objeto['y']:
                    vari = objeto['x']
                    valor = objeto['x'] + 1
                    while vari <= valor:
                        DestructoresPJ1.agregarCoordenadas(self.contadorDestructoresPJ1, objeto['y'], vari)
                        TableroPJ1.modificar(objeto['y'], vari, 'Level2')
                        self.PJ1Dest.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                elif (i['x'] - 1 == objeto['x'] - 1) > 0 and i['y'] == objeto['y']:
                    if i['x'] - 1 == objeto['x'] - 1 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 1
                        valor = objeto['x']
                        while vari <= valor:
                            DestructoresPJ1.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                            TableroPJ1.modificar(objeto['y'], vari, 'Level2')
                            self.PJ1Dest.append({'x':vari, 'y':objeto['y']})
                            vari += 1
        self.contadorDestructoresPJ1 += 1
        self.numeroDestrPJ1 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ1Dest):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab1):
                if self.CasillasTab1[valorsecundario]['x'] == self.PJ1Dest[valorinicial]['x'] and self.CasillasTab1[valorsecundario]['y'] == self.PJ1Dest[valorinicial]['y']:
                    self.CasillasTab1.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
            
    def BuquesCasillasPJ1(self, objeto):
        BuquesPJ1.agregarBarco('Buque')
        vari = objeto['x']
        BuquesPJ1.agregarCoordenadas(self.contadorBuquesPJ1, objeto['y'], vari)
        TableroPJ1.modificar(objeto['y'], vari, 'Level1')
        self.PJ1Buqu.append({'x':vari, 'y':objeto['y']})
        self.contadorBuquesPJ1 += 1
        self.numeroBuquePJ1 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ1Buqu):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab1):
                if self.CasillasTab1[valorsecundario]['x'] == self.PJ1Buqu[valorinicial]['x'] and self.CasillasTab1[valorsecundario]['y'] == self.PJ1Buqu[valorinicial]['y']:
                    self.CasillasTab1.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
            
        #----------------------------------Tablero PJ1----------------------------------
        #----------------------------------Tablero PJ1----------------------------------
        #----------------------------------Tablero PJ1----------------------------------
        
        #----------------------------------Tablero PJ2----------------------------------
        #----------------------------------Tablero PJ2----------------------------------
        #----------------------------------Tablero PJ2----------------------------------
        
    def PortavionesCasillasPJ2(self, objeto):
        PortavionesPJ2.agregarBarco('Portaviones')
        if objeto['x'] == self.m:
            for i in self.CasillasTab2:
                if i['x'] - 3 == objeto['x'] - 3 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 3
                    while vari <= self.m:
                        PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                        self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                
        if objeto['x'] == self.m - 1:
            for i in self.CasillasTab2:
                if i['x'] - 2 == objeto['x'] - 2 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 2
                    while vari <= self.m:
                        PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                        self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                    
        if objeto['x'] == self.m - 2:
            for i in self.CasillasTab2:
                if i['x'] - 1 == objeto['x'] - 1 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 1
                    while vari <= self.m:
                        PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                        self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                    
        if objeto['x'] <= self.m - 3:
            for i in self.CasillasTab2:
                if i['x'] == objeto['x'] and i['x'] + 3 == objeto['x'] + 3 and i['y'] == objeto['y']:
                    vari = objeto['x']
                    valor = objeto['x'] + 3
                    while vari <= valor:
                        PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                        self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                elif (i['x'] - 3 == objeto['x'] - 3) > 0 and i['y'] == objeto['y']:
                    if i['x'] -3 == objeto['x'] - 3 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 3
                        valor = objeto['x']
                        while vari <= valor:
                            PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                            TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                            self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                            vari += 1
                    elif i['x'] - 2 == objeto['x'] - 2 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 2
                        valor = objeto['x'] + 1
                        while vari <= valor:
                            PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                            TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                            self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                            vari += 1
                    elif i['x'] - 1 == objeto['x'] - 1 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 1
                        valor = objeto['x'] + 2
                        while vari <= valor:
                            PortavionesPJ2.agregarCoordenadas(self.contadorPortavionesPJ2, objeto['y'], vari)
                            TableroPJ2.modificar(objeto['y'], vari, 'Level4')
                            self.PJ2Port.append({'x':vari, 'y':objeto['y']})
                            vari += 1
        self.contadorPortavionesPJ2 += 1
        self.numeroPortaPJ2 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ2Port):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab2):
                if self.CasillasTab2[valorsecundario]['x'] == self.PJ2Port[valorinicial]['x'] and self.CasillasTab2[valorsecundario]['y'] == self.PJ2Port[valorinicial]['y']:
                    self.CasillasTab2.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
    
    def SubmarinosCasillasPJ2(self, objeto):
        SubmarinosPJ2.agregarBarco('Submarino')
        if objeto['x'] == self.m:
            for i in self.CasillasTab2:
                if i['x'] - 2 == objeto['x'] - 2 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 2
                    while vari <= self.m:
                        SubmarinosPJ2.agregarCoordenadas(self.contadorSubmarinosPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level3')
                        self.PJ2Subm.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                
        if objeto['x'] == self.m - 1:
            for i in self.CasillasTab2:
                if i['x'] - 1 == objeto['x'] - 1 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 1
                    while vari <= self.m:
                        SubmarinosPJ2.agregarCoordenadas(self.contadorSubmarinosPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level3')
                        self.PJ2Subm.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                        
        if objeto['x'] <= self.m - 2:
            for i in self.CasillasTab2:
                if i['x'] == objeto['x'] and i['x'] + 2 == objeto['x'] + 2 and i['y'] == objeto['y']:
                    vari = objeto['x']
                    valor = objeto['x'] + 2
                    while vari <= valor:
                        SubmarinosPJ2.agregarCoordenadas(self.contadorSubmarinosPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level3')
                        self.PJ2Subm.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                elif (i['x'] - 2 == objeto['x'] - 2) > 0 and i['y'] == objeto['y']:
                    if i['x'] - 2 == objeto['x'] - 2 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 2
                        valor = objeto['x']
                        while vari <= valor:
                            SubmarinosPJ2.agregarCoordenadas(self.contadorSubmarinosPJ2, objeto['y'], vari)
                            TableroPJ2.modificar(objeto['y'], vari, 'Level3')
                            self.PJ2Subm.append({'x':vari, 'y':objeto['y']})
                            vari += 1
                    elif i['x'] - 1 == objeto['x'] - 1 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 1
                        valor = objeto['x'] + 1
                        while vari <= valor:
                            SubmarinosPJ2.agregarCoordenadas(self.contadorSubmarinosPJ2, objeto['y'], vari)
                            TableroPJ2.modificar(objeto['y'], vari, 'Level3')
                            self.PJ2Subm.append({'x':vari, 'y':objeto['y']})
                            vari += 1
        self.contadorSubmarinosPJ2 += 1
        self.numeroSubmaPJ2 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ2Subm):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab2):
                if self.CasillasTab2[valorsecundario]['x'] == self.PJ2Subm[valorinicial]['x'] and self.CasillasTab2[valorsecundario]['y'] == self.PJ2Subm[valorinicial]['y']:
                    self.CasillasTab2.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
            
    def DestructoresCasillasPJ2(self, objeto):
        DestructoresPJ2.agregarBarco('Destructor')
        
        if objeto['x'] == self.m:
            for i in self.CasillasTab2:
                if i['x'] - 1 == objeto['x'] - 1 and i['y'] == objeto['y']:
                    vari = objeto['x'] - 1
                    while vari <= self.m:
                        DestructoresPJ2.agregarCoordenadas(self.contadorDestructoresPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level2')
                        self.PJ2Dest.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                        
        if objeto['x'] <= self.m - 1:
            for i in self.CasillasTab2:
                if i['x'] == objeto['x'] and i['x'] + 1 == objeto['x'] + 1 and i['y'] == objeto['y']:
                    vari = objeto['x']
                    valor = objeto['x'] + 1
                    while vari <= valor:
                        DestructoresPJ2.agregarCoordenadas(self.contadorDestructoresPJ2, objeto['y'], vari)
                        TableroPJ2.modificar(objeto['y'], vari, 'Level2')
                        self.PJ2Dest.append({'x':vari, 'y':objeto['y']})
                        vari += 1
                elif (i['x'] - 1 == objeto['x'] - 1) > 0 and i['y'] == objeto['y']:
                    if i['x'] - 1 == objeto['x'] - 1 and i['x'] == objeto['x'] and i['y'] == objeto['y']:
                        vari = objeto['x'] - 1
                        valor = objeto['x']
                        while vari <= valor:
                            DestructoresPJ2.agregarCoordenadas(self.contadorSubmarinosPJ1, objeto['y'], vari)
                            TableroPJ2.modificar(objeto['y'], vari, 'Level2')
                            self.PJ2Dest.append({'x':vari, 'y':objeto['y']})
                            vari += 1
        self.contadorDestructoresPJ2 += 1
        self.numeroDestrPJ2 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ2Dest):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab2):
                if self.CasillasTab2[valorsecundario]['x'] == self.PJ2Dest[valorinicial]['x'] and self.CasillasTab2[valorsecundario]['y'] == self.PJ2Dest[valorinicial]['y']:
                    self.CasillasTab2.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
            
    def BuquesCasillasPJ2(self, objeto):
        BuquesPJ2.agregarBarco('Buque')
        vari = objeto['x']
        BuquesPJ2.agregarCoordenadas(self.contadorBuquesPJ2, objeto['y'], vari)
        TableroPJ2.modificar(objeto['y'], vari, 'Level1')
        self.PJ2Buqu.append({'x':vari, 'y':objeto['y']})
        self.contadorBuquesPJ2 += 1
        self.numeroBuquePJ2 += 1
        valorinicial = 0
        while valorinicial < len(self.PJ2Buqu):
            valorsecundario = 0
            while valorsecundario < len(self.CasillasTab2):
                if self.CasillasTab2[valorsecundario]['x'] == self.PJ2Buqu[valorinicial]['x'] and self.CasillasTab2[valorsecundario]['y'] == self.PJ2Buqu[valorinicial]['y']:
                    self.CasillasTab2.pop(valorsecundario)
                valorsecundario += 1
            valorinicial += 1
        
        #----------------------------------Tablero PJ2----------------------------------
        #----------------------------------Tablero PJ2----------------------------------
        #----------------------------------Tablero PJ2----------------------------------

    #--------------------------------Agregar Piezas--------------------------------
    #--------------------------------Agregar Piezas--------------------------------
    #--------------------------------Agregar Piezas--------------------------------
    
    #-------------------------------------TURNOS-------------------------------------
    #-------------------------------------TURNOS-------------------------------------
    #-------------------------------------TURNOS-------------------------------------
    #-------------------------------------TURNOS-------------------------------------
    
    def VerificacionBuquesNPC(self, x, y):
        PortavionesPJ1.BuscarEliminar(y, x)
        SubmarinosPJ1.BuscarEliminar(y, x)
        DestructoresPJ1.BuscarEliminar(y, x)
        BuquesPJ1.BuscarEliminar(y, x)
        self.refrescarBarcosPJ1()
        
    def ObtencionDatosNPC(self, x, y):
        TableroPJ1.modificar(y, x, 'X')
        MiniTablerodePJ1.modificar(y, x, 'X')
        self.VerificacionBuquesNPC(x, y)
        MiniTablerodePJ1.GraficarMiniTableroPJ1()
        TableroPJ1.graficarTablero()
        self.refrescarTableroPJ1()
    
    def EnvioTurnoNPC(self):
        movimiento = ''
        #print(self.MovimientosNPC)
        movimiento = random.choice(self.MovimientosNPC)
        contador = 0
        while contador < len(self.MovimientosNPC):
            if self.MovimientosNPC[contador]['x'] == movimiento['x'] and self.MovimientosNPC[contador]['y'] == movimiento['y']:
                self.MovimientosNPC.pop(contador)
                break
                #print(contador)
            contador += 1
        self.ObtencionDatosNPC(movimiento['x'], movimiento['y'])
        print('Disparo en:',movimiento)
        self.TurnoPJ1()
    
    def TurnoNPC(self):
        self.EntryPosX.config(state='disabled')
        self.EntryPosY.config(state='disabled')
        self.ButonXY.config(state='disabled')
        #self.EntryPosX2.config(state="disabled")
        #self.EntryPosY2.config(state="disabled")
        #self.ButonXY2.config(state="disabled")
        self.EnvioTurnoNPC()
    
    def TurnoPJ2(self):
        self.EntryPosX.config(state='disabled')
        self.EntryPosY.config(state='disabled')
        self.ButonXY.config(state='disabled')
        self.EntryPosX2.config(state="normal")
        self.EntryPosY2.config(state="normal")
        self.ButonXY2.config(state="normal")
    
    def TurnoPJ1(self):
        if self.JugadorVsJugador == True:
            self.EntryPosX2.config(state="disabled")
            self.EntryPosY2.config(state="disabled")
            self.ButonXY2.config(state="disabled")
        self.EntryPosX.config(state='normal')
        self.EntryPosY.config(state='normal')
        self.ButonXY.config(state='normal')
    
    def VerificacionBuquesPJ1(self):
        PortavionesPJ2.BuscarEliminar(int(self.valorY), int(self.valorX))
        SubmarinosPJ2.BuscarEliminar(int(self.valorY), int(self.valorX))
        DestructoresPJ2.BuscarEliminar(int(self.valorY), int(self.valorX))
        BuquesPJ2.BuscarEliminar(int(self.valorY), int(self.valorX))
        self.refrescarBarcosPJ2()
        
    def ObtencionDatosPJ1(self):
        #if len(self.PosicionesPJ1) == 0:
        self.PosicionesPJ1.append({'x': self.valorX, 'y': self.valorY})
        TableroPJ2.modificar(self.valorY, self.valorX, 'X')
        MiniTablerodePJ2.modificar(self.valorY, self.valorX, 'X')
        TableroPJ2.graficarTableroPJ2()
        MiniTablerodePJ2.GraficarMiniTableroPJ2()
        self.refrescarTableroPJ2()
        self.VerificacionBuquesPJ1()
        
    def botonEnviarPJ1(self):
        numeroX = self.EntryPosX.get()
        numeroY = self.EntryPosY.get()
        if numeroX.isdigit() == True and numeroY.isdigit() == True:
            self.valorX = int(numeroX)
            self.valorY = int(numeroY)
            if self.valorX > 0 and self.valorX <= self.m and self.valorY > 0 and self.valorY <= self.m:
                self.ObtencionDatosPJ1()
                if self.CajaOpcionesPJorNPC.get() == 'NPC':
                    self.TurnoNPC()
                    self.TurnoNonPlayerComputer = True
                if self.CajaOpcionesPJorNPC.get() == 'PJ2':
                    self.TurnoPJ2()
            else:
                if self.valorX <= 0:
                    print('X debe ser mayor que 0')
                if self.valorY <= 0:
                    print('Y debe ser mayor que 0')
                if self.valorX > self.m:
                    print('X debe ser menor que ' + str(self.m))
                if self.valorY > self.m:
                    print('Y debe ser menor que ' + str(self.m))
    
    def VerificacionBuquesPJ2(self):
        PortavionesPJ1.BuscarEliminar(int(self.valorY2), int(self.valorX2))
        SubmarinosPJ1.BuscarEliminar(int(self.valorY2), int(self.valorX2))
        DestructoresPJ1.BuscarEliminar(int(self.valorY2), int(self.valorX2))
        BuquesPJ1.BuscarEliminar(int(self.valorY2), int(self.valorX2))
        self.refrescarBarcosPJ1()
    
    def ObtencionDatosPJ2(self):
        #if len(self.PosicionesPJ2) == 0:
        self.PosicionesPJ2.append({'x': self.valorX2, 'y': self.valorY2})
        TableroPJ1.modificar(self.valorY2, self.valorX2, 'X')
        MiniTablerodePJ1.modificar(self.valorY2, self.valorX2, 'X')
        TableroPJ1.graficarTablero()
        MiniTablerodePJ1.GraficarMiniTableroPJ1()
        self.refrescarTableroPJ1()
        self.VerificacionBuquesPJ2()
        
    def botonEnviarPJ2(self):
        numeroX = self.EntryPosX2.get()
        numeroY = self.EntryPosY2.get()
        if numeroX.isdigit() == True and numeroY.isdigit() == True:
            self.valorX2 = int(numeroX)
            self.valorY2 = int(numeroY)
            if self.valorX2 > 0 and self.valorX2 <= self.m and self.valorY2 > 0 and self.valorY2 <= self.m:
                self.ObtencionDatosPJ2()
                self.TurnoPJ1()
            else:
                if self.valorX2 <= 0:
                    print('X debe ser mayor que 0')
                if self.valorY2 <= 0:
                    print('Y debe ser mayor que 0')
                if self.valorX2 > self.m:
                    print('X debe ser menor que ' + str(self.m))
                if self.valorY2 > self.m:
                    print('Y debe ser menor que ' + str(self.m))
        
    #-------------------------------------TURNOS-------------------------------------
    #-------------------------------------TURNOS-------------------------------------
    #-------------------------------------TURNOS-------------------------------------
    #-------------------------------------TURNOS-------------------------------------
    
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    
    def aHoras(self,segundos):
        segundos = segundos % (24 * 3600)
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
        return "%02d:%02d:%02d" % (horas, minutos, segundos)
    
    def aSegundos(self, hora):
        h, m, s = hora.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    
    def cuenta(self, restante = None):
        if restante != None:
            self.restante = restante
        if self.restante <= 0:
            Mensajefinal = '00:00:00'
            self.LabelCuenta.configure(text=Mensajefinal)
            if self.secioniniciada == True:
                self.LabelCuenta['fg'] = '#EE4420'
                self.CantidadComprasUsuario += "\\n]\\n},"
                self.CantidadComprasUsuario_sinArreglar += "\n]\n},"
                if self.sicompro == False:
                    MerkleTree.add("1")
                    MerkleTree.auth()
                    rootMerk = MerkleTree.tophash.hash
                    cantidadceros = UsuarioAdministrador.cabeza.cantidadceros
                    strCeros = UsuarioAdministrador.cabeza.strCeros
                    Bloques.insertar("", rootMerk, cantidadceros, strCeros, "{\n},\n")
                    MerkleTree.eliminar()
                if self.sicompro == True:
                    MerkleTree.auth()
                    MerkleTree.dotget()
                    rootMerk = MerkleTree.tophash.hash
                    cantidadceros = UsuarioAdministrador.cabeza.cantidadceros
                    strCeros = UsuarioAdministrador.cabeza.strCeros
                    #MerkleTree.tophash.hash
                    Bloques.insertar(self.CantidadComprasUsuario, rootMerk, cantidadceros, strCeros, self.CantidadComprasUsuario_sinArreglar)
                    MerkleTree.eliminar()
                    self.sicompro = False
                self.CuentaRegresivaEmpezar()
                self.CantidadComprasUsuario = "{\\nFROM:"+ListaUsuariosDB.usuario_act.WalletUSR+"\\nSKINS:[\n"
                self.CantidadComprasUsuario_sinArreglar = "{\n\"FROM\":\""+ListaUsuariosDB.usuario_act.WalletUSR+"\",\n\"SKINS\":[\n"
                #Bloques.toJson()
            #print(self.CantidadComprasUsuario)
            #self.ButtonIDProd.config(state='disabled')
            #ListaUsuariosDB.LimpiarCarro()
            #self.refrescarCarrito()
            
            print("FINALIZADO")
        else:
            horaActual = self.aHoras(self.restante)
            self.LabelCuenta.configure(text=horaActual)
            self.LabelCuenta['fg'] = '#2093EE'
            self.restante = self.restante - 1
            self.after(1000, self.cuenta)
            
    def CuentaRegresivaEmpezar(self):
        total = self.aSegundos("{0}:{1}:{2}".format(0, UsuarioAdministrador.cabeza.tiempomin, UsuarioAdministrador.cabeza.tiemposeg))
        if total > 0:
            self.cuenta(total)
    
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    #---------------------------------TIEMPO/TEMPORIZADOR---------------------------------
    
    #--------------------------------Tablero Tamanio--------------------------------
    #--------------------------------Tablero Tamanio--------------------------------
    #--------------------------------Tablero Tamanio--------------------------------
    
    def LlenarAutomaticamente(self):
        self.ButonM.config(state="disabled")
        #self.BotonBuscarUserID.config(state="normal")
        self.ButtonLlenarTableros.config(state="disabled")
        self.CajaOpcionesPJorNPC.config(state="normal")
        self.BotonOptionsPJorNPC.config(state="normal")
        #Poner comandos para llenar automaticamente de barcos el tablero
        TableroPJ1.graficarTablero()
        TableroPJ2.graficarTableroPJ2()
        self.refrescarTablero()
        self.refrescarBarcos()
    
    def LlenarTableroPJ1(self):
        #Portaviones
        for i in range(self.numeroPortaviones):
            self.PortavionesCasillasPJ1(random.choice(self.CasillasTab1))
        for i in range(self.numeroSubmarinos):
            self.SubmarinosCasillasPJ1(random.choice(self.CasillasTab1))
        for i in range(self.numeroDestructores):
            self.DestructoresCasillasPJ1(random.choice(self.CasillasTab1))
        for i in range(self.numeroBuques):
            self.BuquesCasillasPJ1(random.choice(self.CasillasTab1))
    
    def LlenarTableroPJ2(self):
        for i in range(self.numeroPortaviones):
            self.PortavionesCasillasPJ2(random.choice(self.CasillasTab2))
        for i in range(self.numeroSubmarinos):
            self.SubmarinosCasillasPJ2(random.choice(self.CasillasTab2))
        for i in range(self.numeroDestructores):
            self.DestructoresCasillasPJ2(random.choice(self.CasillasTab2))
        for i in range(self.numeroBuques):
            self.BuquesCasillasPJ2(random.choice(self.CasillasTab2))
    
    def BuscarSeleccionadoUsuarioID(self):
        self.usuarioSeleccionadoporID = None
        usuariobuscar = ListaUsuariosDB.cabeza
        while usuariobuscar != None:
            if int(self.CajaOpcionesUsuarios.get()) == usuariobuscar.id:
                self.NickUsuarioSeleccionadoporID = usuariobuscar.nick
                self.usuarioSeleccionadoporID = usuariobuscar.id
                self.LabelUsuarioIDBuscar['text'] = 'Usuario: ' + usuariobuscar.nick
            usuariobuscar = usuariobuscar.siguiente
        
    def OKUsuarioIDEscogido(self):
        self.CajaOpcionesUsuarios.config(state="disabled")
        self.BotonBuscarUserID.config(state='disabled')
        self.BotonOptionsUserID.config(state='disabled')
        self.LabelUsuarioIDBuscar['fg'] = 'green'
        self.LabelUsuarioIDBuscar['text'] = self.UsuarioNombre + ' VS ' + self.NickUsuarioSeleccionadoporID
        ListaUsuariosDB.LlamarJugador2(self.usuarioSeleccionadoporID)
        self.refrescar()
        self.TurnoPJ1()
    
    def OKBotonOptPJorNPC(self):
        if self.CajaOpcionesPJorNPC.get() == 'NPC':
            self.JugadorVsNPC = True
            self.JugadorVsJugador = False
            self.BotonOptionsPJorNPC.config(state='disabled')
            self.CajaOpcionesPJorNPC.config(state='disabled')
            self.LabelUsuarioIDBuscar['fg'] = 'gray'
            self.LabelUsuarioIDBuscar['text'] = 'Jugador VS NPC'
            self.TurnoPJ1()
            
        if self.CajaOpcionesPJorNPC.get() == 'PJ2':
            self.JugadorVsNPC = False
            self.JugadorVsJugador = True
            self.PosX2 = Label(self.p4, text='Pos X', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
            self.PosX2.place(x=600, y=300)
            self.EntryPosX2 = Entry(self.p4, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
            self.EntryPosX2.insert(0, 'Pos Col')
            self.EntryPosX2.config(state="disabled")
            self.EntryPosX2.bind("<FocusIn>", lambda args: self.entry_in_XY(self.EntryPosX2))
            self.EntryPosX2.bind("<FocusOut>", lambda args: self.entry_out_XY(self.EntryPosX2, 'Pos Col'))
            self.EntryPosX2.place(x=600, y=340)
            
            self.PosY2 = Label(self.p4, text='Pos Y', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
            self.PosY2.place(x=700, y=300)
            self.EntryPosY2 = Entry(self.p4, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
            self.EntryPosY2.insert(0, 'Pos Row')
            self.EntryPosY2.config(state="disabled")
            self.EntryPosY2.bind("<FocusIn>", lambda args: self.entry_in_XY(self.EntryPosY2))
            self.EntryPosY2.bind("<FocusOut>", lambda args: self.entry_out_XY(self.EntryPosY2, 'Pos Row'))
            self.EntryPosY2.place(x=700, y=340)
            
            self.ButonXY2 = Button(self.p4, text= 'OK', command = lambda:self.botonEnviarPJ2(),activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
            self.ButonXY2.config(state="disabled")
            self.ButonXY2.place(x=800, y=340)
            
            self.LabelMoneyPJ2 = Label(self.p4, text='Tokens: ' + str(0), bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 10, 'bold'))
            self.LabelMoneyPJ2.place(x=600, y=400)
            
            self.BotonOptionsPJorNPC.config(state='disabled')
            self.CajaOpcionesPJorNPC.config(state='disabled')
            self.CajaOpcionesUsuarios.config(state='normal')
            self.BotonBuscarUserID.config(state='normal')
            self.BotonOptionsUserID.config(state='normal')
    
    def PosicionesMovimientos(self):
        while self.valori <= self.m:
            valorj = 1
            while valorj <= self.m:
                self.MovimientosNPC.append({'x': valorj, 'y': self.valori})
                self.CasillasTab1.append({'x': valorj, 'y': self.valori})
                self.CasillasTab2.append({'x': valorj, 'y': self.valori})
                valorj += 1
            self.valori += 1
    
    def LlenandoTabsUwU(self):
        self.LlenarTableroPJ1()
        self.LlenarTableroPJ2()
        self.ButtonLlenarTab.config(state='disabled')
        self.ButtonLlenarTableros.config(state='normal')
    
    def mxmOption(self):
        self.MatematicoCantidadBarcos = 0
        numeroobtenido = self.EntryM.get()
        if numeroobtenido.isdigit() == True:
            self.valormxm = int(self.EntryM.get())
            if self.valormxm >= 10 and self.valormxm <= 50:
                TableroPJ1.llenarTablero(self.valormxm)
                TableroPJ2.llenarTablero(self.valormxm)
                MiniTablerodePJ1.llenarTablero(self.valormxm)
                MiniTablerodePJ2.llenarTablero(self.valormxm)
                TableroPJ1.graficarTablero()
                TableroPJ2.graficarTableroPJ2()
                MiniTablerodePJ1.GraficarMiniTableroPJ1()
                MiniTablerodePJ2.GraficarMiniTableroPJ2()
                self.m = self.valormxm
                self.LabeErrorM['text'] = ''
                self.MatematicoCantidadBarcos = int(round(((self.valormxm-1)/10)+1))
                self.numeroPortaviones = self.MatematicoCantidadBarcos
                self.numeroSubmarinos = self.MatematicoCantidadBarcos * 2
                self.numeroDestructores = self.MatematicoCantidadBarcos * 3
                self.numeroBuques = self.MatematicoCantidadBarcos * 4
                self.PosicionesMovimientos()
                self.ButtonLlenarTab.config(state="normal")
                self.ButonM.config(state='disabled')
                self.EntryM.config(state="disabled")
                self.refrescarTablero()
            else:
                if self.valormxm < 10:
                    self.LabeErrorM['text'] = 'M debe ser mayor que 10'
                if self.valormxm > 50:
                    self.LabeErrorM['text'] = 'M debe ser menor que 50'
        else:
            self.LabeErrorM['text'] = 'M NO VALIDO (debe ser n)'
    
    #--------------------------------Tablero Tamanio--------------------------------
    #--------------------------------Tablero Tamanio--------------------------------
    #--------------------------------Tablero Tamanio--------------------------------
    #--------------------------------Tablero Tamanio--------------------------------
        
    def ArbolAVL(self):
        #ListaUsuariosDB.GraficarArbolUsuarioActivo()
        print()
    
        
    #----------------------------------Widgets Clase----------------------------------
    #----------------------------------Widgets Clase----------------------------------
    #----------------------------------Widgets Clase----------------------------------
    #----------------------------------Widgets Clase----------------------------------
    
    def widgets_sec(self):
        if ListaUsuariosDB.usuario_act.LlaveWallet == "":
            priv = secrets.token_hex(32)
            priv_key = priv
            ListaUsuariosDB.AgregarKeyWallet(priv_key)
            
        print('User Addres:', ListaUsuariosDB.usuario_act.WalletUSR)
        print('Key (No Compartir):', ListaUsuariosDB.usuario_act.LlaveWallet)
        
        self.CantidadComprasUsuario = "{\\nFROM:"+ListaUsuariosDB.usuario_act.WalletUSR+"\\nSKINS:[\n"
        self.CantidadComprasUsuario_sinArreglar = "{\n\"FROM\":\""+ListaUsuariosDB.usuario_act.WalletUSR+"\",\n\"SKINS\":[\n"
        #MENU
        #print('{}::{}:{}:{}'.format(now.date(), now.hour, now.minute, now.second))
        self.menubar = Menu(self.master, bg='#1D1A1A', fg='white', activebackground='#485B67')
        self.menuinicial = Menu(self.menubar, tearoff=0, bg='#1D1A1A', fg='white', activebackground='#485B67', activeforeground='white')
        self.menuinicial.add_command(label='Generar AVL Usuario', command=lambda: self.ArbolAVL())
        self.master.config(menu = self.menubar)
        self.menubar.add_cascade(label='Generar', menu=self.menuinicial)
        #Panel para pestanias
        s = ttk.Style()
        s.configure('new.TFrame', background='#1D1A1A')
        self.nb = ttk.Notebook(self.master)
        self.nb.pack(fill='both', expand='yes')
        #crear pest
        self.p1 = ttk.Frame(self.nb, style='new.TFrame')
        self.p2 = ttk.Frame(self.nb, style='new.TFrame')
        self.p3 = ttk.Frame(self.nb, style='new.TFrame')
        self.p4 = ttk.Frame(self.nb, style='new.TFrame')
        #agregar pest
        self.nb.add(self.p1, text='Tienda')
        self.nb.add(self.p2, text='Perfil Usuario')
        self.nb.add(self.p3, text='TableroPJ1')
        self.nb.add(self.p4, text='TableroPJ2')
        
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        
        self.LabelCuenta = Label(self.p1, text='00:00:00', font=('Courier New',30, 'bold'), bg='#1D1A1A', fg='#2093EE')
        self.LabelCuenta.place(x=737, y=130)
        self.secioniniciada = True
        if self.secioniniciada == True:
            self.CuentaRegresivaEmpezar()
        self.ruta = 'Images/nemesis.png'
        self.program_directory = sys.path[0]
        self.logo = PhotoImage(file=os.path.join(self.program_directory, self.ruta))
        self.logo2 = self.logo.subsample(2)
        #Imagen donde sale Nemesis
        self.image = Label(self.p1, image = self.logo2, bg='#1D1A1A',height=150, width=200)
        self.image.pack()
        self.image.place(x=20,y=10)
        self.ruta2 = 'Images/a2.png'
        #Imagen de Usuario?
        self.logoa = PhotoImage(file=os.path.join(self.program_directory, self.ruta2))
        self.logo3 = self.logoa.subsample(3)
        self.logo4 = self.logoa.subsample(4)
        self.image2 = Label(self.p1, image = self.logo3, bg='#1D1A1A',height=100, width=100)
        self.image2.pack()
        self.image2.place(x=1050,y=10)
        
        
        ##POXIMOS AJUSTES PARA NUMERO DEL CARRITO
        self.RutaCarrito = 'Images/carrito.png'
        self.ImagenCarrito = PhotoImage(file=os.path.join(self.program_directory, self.RutaCarrito)).subsample(9)
        self.BotonCarritoUsU = Button(self.p1, text='0', command=lambda:self.CarritoVer(), image=self.ImagenCarrito, borderwidth=0, compound=LEFT, bg='#1D1A1A',fg='Green', font=('Arial', 12))
        self.BotonCarritoUsU.place(x=1000, y=200)
        self.LabelCarritoUsU = Label(self.p1, text='$ 0', borderwidth=5, bg='#1D1A1A',fg='red', font=('Arial', 12))
        self.LabelCarritoUsU.place(x=1100, y=210)
        self.refrescarCarrito()
        #Boton de comprar
        #self.ButtonComprarProds = Button(self.p1, text= 'Comprar', command=lambda:self.SeleccionMandar(), activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        #self.ButtonComprarProds.place(x=1027, y=460)
        
        #label de tienda de Skins
        la = Label(self.p1, text= 'Tienda de SKINS', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 24, 'bold'))
        la.pack()
        la.place(y=30, x=320)
        #Boton salida
        self.ruta_boton_salida = 'Images/off.png'
        self.imagen_boton_salida = PhotoImage(file=os.path.join(self.program_directory, self.ruta_boton_salida)).subsample(10)
        boton_salida = Button(self.p1, image=self.imagen_boton_salida, text='Cerrar Sesion', compound=LEFT, bg='#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A', command=lambda:self.regresar(), width=140)
        boton_salida.place(x=1000, y=120)
        #Label Monedas
        self.nombreLabel = Label(self.p1, text=self.UsuarioNombre, bg='#1D1A1A', fg='white', font=('Lucia Sans', 15, 'bold'))
        self.nombreLabel.place(x=230, y=110)
        self.monedasLAbel = Label(self.p1, text='Tokens: ' + str(self.UsuarioMoned), bg='#1D1A1A', fg='white', font=('Lucia Sans', 15, 'bold'))
        self.monedasLAbel.place(x=230, y=140)
        #contenedor
        self.prim = Frame(self.p1)
        self.prim.config(bg='black')
        mycanvas = Canvas(self.prim)
        #mycanvas.pack(side=LEFT, fill='both', expand='yes')
        xscrollbar = ttk.Scrollbar(self.prim, orient="horizontal", command=mycanvas.xview)
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar = ttk.Scrollbar(self.prim, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        mycanvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar, bg='#1D1A1A', width=900, height=350)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        mycanvas.pack(side=LEFT)
        myframe = Frame(mycanvas, bg='#1D1A1A')
        mycanvas.create_window((0,0), window=myframe)
        self.prim.pack()
        self.prim.place(x=20, y=180)
        #Box para buscar articulo
        self.LabelIDProd = Label(self.p1, text='Producto Buscar', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelIDProd.place(x=960, y=320)
        self.entradaIDProd = Entry(self.p1, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=20)
        self.entradaIDProd.insert(0, 'Cantidad a Comprar')
        self.entradaIDProd.bind("<FocusIn>", lambda args: self.entry_in2(self.entradaIDProd))
        self.entradaIDProd.bind("<FocusOut>", lambda args: self.entry_out2(self.entradaIDProd, 'Cantidad a Comprar'))
        self.entradaIDProd.place(x=990, y=350)
        self.ButtonIDProd = Button(self.p1, text= 'Buscar',  command =lambda:self.BuscarProducto(),activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        self.ButtonIDProd.place(x=1030, y=390)
        x = 0
        ListaGraficar = ListaLArticulos.cabeza
        while ListaGraficar != None:
            i = 0
            Label(myframe, text= ListaGraficar.categoria, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold')).grid(row=x, column=0)
            if ListaGraficar.abajo != None:
                ListaSecGraficar = ListaGraficar.abajo.cabeza
                while ListaSecGraficar != None:
                    Button(myframe, image=self.logo4, text='ID: '+str(ListaSecGraficar.id)+'\nPrecio: '+str(ListaSecGraficar.precio)+'\nNombre: '+ListaSecGraficar.nombre, fg='white', bg='#1D1A1A', width=190, height=60, compound=LEFT, command=lambda:self.SeleccionMandar, font= ('Lucida Sans', 9)).grid(column=i+1, row=x)
                    i = i + 1
                    ListaSecGraficar = ListaSecGraficar.siguiente
            x = x + 1
            ListaGraficar = ListaGraficar.siguiente
        
            
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        
        #P2 perfil
        self.imagen_en_perfil = Label(self.p2, image=self.logo3, bg='#1D1A1A',height=100, width=100)
        self.imagen_en_perfil.pack()
        self.imagen_en_perfil.place(x=1050,y=10)
        #P2 IMAGEN NEMESIS
        self.neme = Label(self.p2, image = self.logo2, bg='#1D1A1A',height=150, width=200)
        self.neme.pack()
        self.neme.place(x=20,y=10)
        #Boton salida
        boton_salida2 = Button(self.p2, image=self.imagen_boton_salida, text='Cerrar Sesion', compound=LEFT, bg='#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A', command=lambda:self.regresar())
        boton_salida2.place(x=1000, y=120)
        #label de Info Usuario
        la2 = Label(self.p2, text= 'Informacion Usuario', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 24, 'bold'))
        la2.pack()
        la2.place(y=30, x=430)
        #Entrada ID
        self.LabelID = Label(self.p2, text='ID Nueva', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelID.place(x=100, y=190)
        self.entradaID = Entry(self.p2, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=40)
        self.entradaID.insert(0, 'ID: '+ str(self.UsuarioID))
        self.entradaID.config(state="disabled")
        self.entradaID.bind("<FocusIn>", lambda args: self.entry_in(self.entradaID))
        self.entradaID.bind("<FocusOut>", lambda args: self.entry_out(self.entradaID, 'ID: '+ str(self.UsuarioID)))
        self.entradaID.place(x=100, y=220)
        #Entrada EDAD
        self.LabelEdad = Label(self.p2, text='Edad Nueva', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelEdad.place(x=500, y=190)
        self.entradaEdad = Entry(self.p2, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=40)
        self.entradaEdad.insert(0, 'Edad: '+ str(self.UsuarioEdad))
        self.entradaEdad.config(state="disabled")
        self.entradaEdad.bind("<FocusIn>", lambda args: self.entry_in(self.entradaEdad))
        self.entradaEdad.bind("<FocusOut>", lambda args: self.entry_out(self.entradaEdad, 'Edad: '+ str(self.UsuarioEdad)))
        self.entradaEdad.place(x=500, y=220)
        #Entrada Nombre
        self.LabelNombre = Label(self.p2, text='Nombre Nuevo', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelNombre.place(x=100, y=280)
        self.entradaNom = Entry(self.p2, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=40)
        self.entradaNom.insert(0, 'Nombre: '+ self.UsuarioNombre)
        self.entradaNom.config(state="disabled")
        self.entradaNom.bind("<FocusIn>", lambda args: self.entry_in(self.entradaNom))
        self.entradaNom.bind("<FocusOut>", lambda args: self.entry_out(self.entradaNom, 'Nombre: '+ self.UsuarioNombre))
        self.entradaNom.place(x=100, y=310)
        #Entrada Password
        self.LabelPassword = Label(self.p2, text='Password Nueva', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelPassword.place(x=500, y=280)
        self.entradaPass = Entry(self.p2, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=40)
        self.entradaPass.insert(0, 'Password: ' + self.UsuarioPass)
        self.entradaPass.config(state="disabled")
        self.entradaPass.bind("<FocusIn>", lambda args: self.entry_in(self.entradaPass))
        self.entradaPass.bind("<FocusOut>", lambda args: self.entry_out(self.entradaPass, 'Password: ' + self.UsuarioPass))
        self.entradaPass.place(x=500, y=310)
        #Entrada Monedas
        self.LabelMonedas = Label(self.p2, text='Cantidad de Tokens', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelMonedas.place(x=100, y=370)
        self.entradaMon = Entry(self.p2, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=40)
        self.entradaMon.insert(0, 'Tokens: '+ str(self.UsuarioMoned))
        self.entradaMon.config(state="disabled")
        self.entradaMon.bind("<FocusIn>", lambda args: self.entry_in(self.entradaMon))
        self.entradaMon.bind("<FocusOut>", lambda args: self.entry_out(self.entradaMon, 'Tokens: '+ str(self.UsuarioMoned)))
        self.entradaMon.place(x=100, y=400)
        #Boton para desbloquear
        self.botondesbloquear = Button(self.p2, text= 'Modificar Datos (Desbloquear)',  command = self.DesbloquearCasillas,activebackground='#1D1A1A',activeforeground='white',  bg='white', font=('Arial', 10,'bold'))
        self.botondesbloquear.place(x=540, y=400)
        #Boton para modificar cambios
        self.botonmodificar = Button(self.p2, text= 'Cambiar Informacion',  command = self.Cambiar,activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        self.botonmodificar.config(state='disabled')
        self.botonmodificar.place(x=1000, y=530)
        #Boton eliminar
        self.botonEliminar = Button(self.p2, text= 'Eliminar',  command = self.EliminarUsuario,activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        self.botonEliminar.place(x=1000, y=480)
        
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        
        self.rutaTablero = 'Images/nemesis.png'
        self.logoTablero = Image.open(self.rutaTablero)
        self.resizeTab = self.logoTablero.resize((558,558))
        self.ImageTKTAB = ImageTk.PhotoImage(self.resizeTab)
        if self.UsuarioNombre != None:
            self.LabelTablero = Label(self.p3, image=self.ImageTKTAB, width=558, height=558)
        else:
            self.LabelTablero = Label(self.p3, width=558, height=558)
        self.LabelTablero.place(x=5, y=5)
        
        #self.rutaMinTabPJ2 = 'Images/nemesis.png'
        self.resizeminTabPJ2 = self.logoTablero.resize((310,310))
        self.ImageTKMinTAB2 = ImageTk.PhotoImage(self.resizeminTabPJ2)
        if self.UsuarioNombre != None:
            self.LabelMinTab2 = Label(self.p3, image=self.ImageTKMinTAB2, width=310, height=310)
        else:
            self.LabelMinTab2 = Label(self.p3, width=310, height=310)
        self.LabelMinTab2.place(x=880, y=5)
            
        
        #M tamanio
        self.TamM = Label(self.p3, text='m x m', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.TamM.place(x=600, y=20)
        self.EntryM = Entry(self.p3, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
        self.EntryM.insert(0, 'm x m')
        self.EntryM.bind("<FocusIn>", lambda args: self.entry_in_XY(self.EntryM))
        self.EntryM.bind("<FocusOut>", lambda args: self.entry_out_XY(self.EntryM, 'm x m'))
        self.EntryM.place(x=700, y=20)
        self.ButonM = Button(self.p3, text= 'M OK', command = lambda:self.mxmOption(),activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        self.ButonM.place(x=800, y=20)
        self.LabeErrorM = Label(self.p3, bg='#1D1A1A', fg= 'red', font= ('Lucida Sans', 9, 'bold'))
        self.LabeErrorM.place(x=650, y=54)
        
        self.ButtonLlenarTab = Button(self.p3, text='Agregar Barcos', command = lambda:self.LlenandoTabsUwU(), activebackground='white', activeforeground='#1A1A1A', bg='#1D1A1A', fg='white', font=('Arial', 10, 'bold'))
        self.ButtonLlenarTab.config(state="disabled")
        self.ButtonLlenarTab.place(x=600, y=80)
        
        self.ButtonLlenarTableros = Button(self.p3, text='Mostrar Tablero', command = lambda:self.LlenarAutomaticamente(), activebackground='white', activeforeground='#1A1A1A', bg='#1D1A1A', fg='white', font=('Arial', 10, 'bold'))
        self.ButtonLlenarTableros.config(state="disabled")
        self.ButtonLlenarTableros.place(x=740, y=80)
        
        #Box Seleccionar PJ VS PJ o PJ vs NPC
        self.selectetNPCorCategory = StringVar()
        self.LabelOpcionesPJoNPC = Label(self.p3, text='Opciones a Jugar', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelOpcionesPJoNPC.place(x=600, y=120)
        OptionsNPCorPC = ['NPC', 'PJ2']
        self.CajaOpcionesPJorNPC = ttk.Combobox(self.p3, values=OptionsNPCorPC, textvariable=self.selectetNPCorCategory)
        self.CajaOpcionesPJorNPC.config(state='disabled')
        self.CajaOpcionesPJorNPC.place(x=600, y=160)
        self.BotonOptionsPJorNPC = Button(self.p3, text='Ok', command = lambda:self.OKBotonOptPJorNPC(), activebackground='white', activeforeground='#1A1A1A', bg='#1D1A1A', fg='white', font=('Arial', 10, 'bold'))
        self.BotonOptionsPJorNPC.config(state='disabled')
        self.BotonOptionsPJorNPC.place(x=800, y=157)
        
        #Box que contiene usuarios 
        #ListaUsuariosDB
        self.LabelOpcionesIDUsuario = Label(self.p3, text='ID Usuario Jugar', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelOpcionesIDUsuario.place(x=600, y=190)
        self.selectedIDUser = StringVar()
        ListadoUsuariosJugar = []
        CategoriaUsuarios = ListaUsuariosDB.cabeza
        while CategoriaUsuarios != None:
            ListadoUsuariosJugar.append(CategoriaUsuarios.id)
            CategoriaUsuarios = CategoriaUsuarios.siguiente
        valorinic = 0
        while valorinic < len(ListadoUsuariosJugar):
            if ListadoUsuariosJugar[valorinic] == self.UsuarioID:
                ListadoUsuariosJugar.pop(valorinic)
            valorinic += 1
            
        self.CajaOpcionesUsuarios = ttk.Combobox(self.p3, values=ListadoUsuariosJugar, textvariable=self.selectedIDUser)
        self.CajaOpcionesUsuarios.config(state="disabled")
        self.CajaOpcionesUsuarios.place(x=600, y=230)
        self.BotonBuscarUserID = Button(self.p3, text='Buscar', command = lambda:self.BuscarSeleccionadoUsuarioID(), activebackground='white', activeforeground='#1A1A1A', bg='#1D1A1A', fg='white', font=('Arial', 10, 'bold'))
        self.BotonBuscarUserID.config(state='disabled')
        self.BotonBuscarUserID.place(x=800, y=227)
        
        self.LabelUsuarioIDBuscar = Label(self.p3, bg='#1D1A1A', fg= 'red', font= ('Lucida Sans', 10, 'bold'))
        self.LabelUsuarioIDBuscar.place(x=600, y=270)
        
        self.BotonOptionsUserID = Button(self.p3, text='Ok', command = lambda:self.OKUsuarioIDEscogido(), activebackground='white', activeforeground='#1A1A1A', bg='#1D1A1A', fg='white', font=('Arial', 10, 'bold'))
        self.BotonOptionsUserID.config(state='disabled')
        self.BotonOptionsUserID.place(x=815, y=267)
        
        #Inputs X Y
        self.PosX = Label(self.p3, text='Pos X', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.PosX.place(x=600, y=300)
        self.EntryPosX = Entry(self.p3, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
        self.EntryPosX.insert(0, 'Pos Col')
        self.EntryPosX.config(state="disabled")
        self.EntryPosX.bind("<FocusIn>", lambda args: self.entry_in_XY(self.EntryPosX))
        self.EntryPosX.bind("<FocusOut>", lambda args: self.entry_out_XY(self.EntryPosX, 'Pos Col'))
        self.EntryPosX.place(x=600, y=340)
        
        self.PosY = Label(self.p3, text='Pos Y', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.PosY.place(x=700, y=300)
        self.EntryPosY = Entry(self.p3, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=10)
        self.EntryPosY.insert(0, 'Pos Row')
        self.EntryPosY.config(state="disabled")
        self.EntryPosY.bind("<FocusIn>", lambda args: self.entry_in_XY(self.EntryPosY))
        self.EntryPosY.bind("<FocusOut>", lambda args: self.entry_out_XY(self.EntryPosY, 'Pos Row'))
        self.EntryPosY.place(x=700, y=340)
        
        self.ButonXY = Button(self.p3, text= 'OK', command = lambda:self.botonEnviarPJ1(),activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        self.ButonXY.config(state="disabled")
        self.ButonXY.place(x=800, y=340)
        
        self.LabelMoneyPJ1 = Label(self.p3, text='Tokens: ' + str(self.UsuarioMoned), bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 10, 'bold'))
        self.LabelMoneyPJ1.place(x=600, y=400)
        
        self.LabelBarcosInGamePJ1 = Label(self.p3, text='Portaviones (in Game): \t' + str(0) + '\nSubmarinos (in Game): \t' + str(0) + '\nDestructores (in Game): \t' + str(0) + '\nBuques (in Game): \t' + str(0), justify=LEFT, bg='#1D1A1A', fg= 'green', font= ('Lucida Sans', 9, 'bold'))
        self.LabelBarcosInGamePJ1.place(x=600, y=450)
        
        self.LabelGanOPerd = Label(self.p3, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 14, 'bold'))
        self.LabelGanOPerd.place(x=650, y=530)
        
        #inputprueva
        #self.botonpruebas = Button(self.p3, text='Grafph', command = lambda:self.GrafoAdyacencia())
        #self.botonpruebas.place(x=780, y=530)
        
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        
        #--------------------------------------- TABPJ2 ---------------------------------------
        #--------------------------------------- TABPJ2 ---------------------------------------
        #--------------------------------------- TABPJ2 ---------------------------------------
        
        self.ImageTKTAB2 = ImageTk.PhotoImage(self.resizeTab)
        if self.UsuarioNombre != None:
            self.LabelTablero2 = Label(self.p4, image=self.ImageTKTAB, width=558, height=558)
        else:
            self.LabelTablero2 = Label(self.p4, width=558, height=558)
        self.LabelTablero2.place(x=5, y=5)
        
        self.LabelPJ2NPCorPJ2 = Label(self.p4, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 14, 'bold'))
        self.LabelPJ2NPCorPJ2.place(x=600, y=100)
            
        self.LabelBarcosInGamePJ2 = Label(self.p4, text='Portaviones (in Game): \t' + str(0) + '\nSubmarinos (in Game): \t' + str(0) + '\nDestructores (in Game): \t' + str(0) + '\nBuques (in Game): \t' + str(0), justify=LEFT, bg='#1D1A1A', fg= 'green', font= ('Lucida Sans', 9, 'bold'))
        self.LabelBarcosInGamePJ2.place(x=600, y=450)
        
        self.LabelGanOPerd2 = Label(self.p4, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 14, 'bold'))
        self.LabelGanOPerd2.place(x=650, y=530)
        
        #self.rutaMinTabPJ2 = 'Images/nemesis.png'
        self.resizeminTabPJ1 = self.logoTablero.resize((310,310))
        self.ImageTKMinTAB1 = ImageTk.PhotoImage(self.resizeminTabPJ1)
        if self.UsuarioNombre != None:
            self.LabelMinTab1 = Label(self.p4, image=self.ImageTKMinTAB1, width=310, height=310)
        else:
            self.LabelMinTab1 = Label(self.p4, width=310, height=310)
        self.LabelMinTab1.place(x=880, y=5)
        
        
        #--------------------------------------- TABPJ2 ---------------------------------------
        #--------------------------------------- TABPJ2 ---------------------------------------
        #--------------------------------------- TABPJ2 ---------------------------------------
        #--------------------------------------- TABPJ2 ---------------------------------------
        
    #----------------------------------Widgets Clase----------------------------------
    #----------------------------------Widgets Clase----------------------------------
    #----------------------------------Widgets Clase----------------------------------

#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
   
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------

class Inicio(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.user_marcar = "Ingrese Usuario"
        self.contra_marcar = "Ingresar Password"
        self.UsuarioNombre = None
        self.UsuarioID = None
        self.UsuarioMoned = None
        self.PartidasJugadas = None
        self.UsuarioIngresado = False
        self.Data_archivo = None
        self.widgets()
        
    #---------------------------------Entradas---------------------------------
    #---------------------------------Entradas---------------------------------
    #---------------------------------Entradas---------------------------------
        
    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) ==0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
        if self.entry2.get() != 'Ingresar Password':
            self.entry2['show'] = ""
        if self.entry2.get() != 'Ingrese Usuario':
            self.entry2['show'] = "*"
            
    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
        if self.entry2.get() != 'Ingresar Password':
            self.entry2['show'] = "*"
        if self.entry2.get() == 'Ingresar Password':
            self.entry2['show'] = ""
    
    #---------------------------------Entradas---------------------------------
    #---------------------------------Entradas---------------------------------
    #---------------------------------Entradas---------------------------------
    
    #---------------------------------SalidaAP---------------------------------
    #---------------------------------SalidaAP---------------------------------
    
    def salir(self):
        messagebox.showinfo(message='Saliendo del Programa\nGraficas generandose')
        self.master.destroy()
        self.master.quit()
    
    #---------------------------------SalidaAP---------------------------------
    #---------------------------------SalidaAP---------------------------------
    
    #---------------------------------VentanaSec---------------------------------
    #---------------------------------VentanaSec---------------------------------
    #---------------------------------VentanaSec---------------------------------
        
    def acceder_Ventana_Sec(self):
        for i in  range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.003)
            
        self.master.withdraw()
        self.Ventana_Sec = Toplevel()
        self.Ventana_Sec.title('Proyecto Fase 3 - 201906051')
        x_wi = 1200
        y_he = 600
        x_pos = (self.Ventana_Sec.winfo_screenwidth() // 2) - (x_wi // 2)
        y_pos = (self.Ventana_Sec.winfo_screenheight() // 2) - (y_he // 2) - 25
        position = str(x_wi) + "x" + str(y_he) + "+" + str(x_pos) + "+" + str(y_pos)
        self.Ventana_Sec.geometry(position)
        self.Ventana_Sec.resizable(0,0)
        self.Ventana_Sec.protocol("WM_DELETE_WINDOW", self.salir)
        self.Ventana_Sec.config(bg= '#1D1A1A')
        app2 = Secundaria(self.Ventana_Sec, self.Data_archivo)#Agregar las variables
        app2.mainloop()
    
    #---------------------------------VentanaSec---------------------------------
    #---------------------------------VentanaSec---------------------------------
    #---------------------------------VentanaSec---------------------------------
    #---------------------------------VentanaSec---------------------------------
    
    #---------------------------------VentanaAdmin---------------------------------
    #---------------------------------VentanaAdmin---------------------------------
    #---------------------------------VentanaAdmin---------------------------------
    #---------------------------------VentanaAdmin---------------------------------
    
    def AccederVentanaAdmin(self):
        for i in range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.003)

        self.master.withdraw()
        self.VentanaAdministrador = Toplevel()
        self.VentanaAdministrador.title('Proyecto Fase 3 - Admin')
        x_wi = 350
        y_he = 500
        xpos = y_he
        ypos = (self.VentanaAdministrador.winfo_screenheight() // 2) - (y_he // 2) - 25
        post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
        self.VentanaAdministrador.geometry(post)
        self.VentanaAdministrador.resizable(0,0)
        self.VentanaAdministrador.protocol("WM_DELETE_WINDOW", self.salir)
        self.VentanaAdministrador.config(bg= '#1D1A1A')
        adminApp = Administrador(self.VentanaAdministrador)
        adminApp.mainloop()
        
    #---------------------------------VentanaAdmin---------------------------------
    #---------------------------------VentanaAdmin---------------------------------
    #---------------------------------VentanaAdmin---------------------------------
    #---------------------------------VentanaAdmin---------------------------------
    
    #---------------------------------CrearUSR---------------------------------
    #---------------------------------CrearUSR---------------------------------
    #---------------------------------CrearUSR---------------------------------
    #---------------------------------CrearUSR---------------------------------
        
    def CrearUsuario_NuevaVent(self):
        self.master.withdraw()
        self.Ventana_Registro = Toplevel()
        self.Ventana_Registro.title('Registro Usuario')
        self.Ventana_Registro.config(bg='#1D1A1A')
        ruta = 'Images/IMGF.png'
        program_directory=sys.path[0]
        self.Ventana_Registro.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
        x_wi = 350
        y_he = 500
        xpos = y_he
        ypos = (self.Ventana_Registro.winfo_screenheight() // 2) - (y_he // 2) -25
        post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
        self.Ventana_Registro.geometry(post)
        self.Ventana_Registro.resizable(0,0)
        app3 = Registro(self.Ventana_Registro)
        app3.mainloop()
    
    #---------------------------------CrearUSR---------------------------------
    #---------------------------------CrearUSR---------------------------------
    #---------------------------------CrearUSR---------------------------------
    #---------------------------------CrearUSR---------------------------------
    
    #-------------------------Verificacion Credencia----------------------------
    #-------------------------Verificacion Credencia----------------------------
    #-------------------------Verificacion Credencia----------------------------
    #-------------------------Verificacion Credencia----------------------------
    
    def verificacion_users(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()
        self.UsuarioIngresado = ListaUsuariosDB.InicioSecion(users_entry, password_entry)
        self.UserAdmin = UsuarioAdministrador.InicioAdmin(users_entry, password_entry)
        
        if self.UsuarioIngresado == True:
            self.UsuarioNombre = ListaUsuariosDB.nombreUsuario()
            self.UsuarioID = ListaUsuariosDB.idUsuario()
            self.UsuarioMoned = ListaUsuariosDB.monedasUsuario()
            self.PartidasJugadas = ListaUsuariosDB.obtenercantidadjugadas()
            print("Bienvenido: " + self.UsuarioNombre)
            self.acceder_Ventana_Sec()
        
        if self.UserAdmin == True:
            print('Bienvenido ADMIN: ', UsuarioAdministrador.cabeza.nick)
            self.AccederVentanaAdmin()
            
        if users_entry.isalnum() == False:
            if users_entry == '':
                self.indica1['text'] = 'Usuario no Ingresado'
                return
            self.indica1['text'] = 'Usuario no Aceptado'
        if password_entry.isalnum() == False:
            if password_entry == '':
                self.indica2['text'] = 'Password no Ingresada'
                return
            self.indica2['text'] = 'Password no Valida'
    
    #-------------------------Verificacion Credencia----------------------------
    #-------------------------Verificacion Credencia----------------------------
    #-------------------------Verificacion Credencia----------------------------
    
    #----------------------------Widgets Principal-------------------------------
    #----------------------------Widgets Principal-------------------------------
    #----------------------------Widgets Principal-------------------------------
        
    def widgets(self):
        self.ruta = 'IM.png'
        self.program_directory = sys.path[0]
        self.logo = PhotoImage(file=os.path.join(self.program_directory, self.ruta))
        self.logo2 = self.logo.subsample(2)
        Label(self.master, image = self.logo2, bg='#1D1A1A',height=150, width=200).pack()
        Label(self.master, text= 'Usuario', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold')).pack(pady = 5)
        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry1.insert(0, self.user_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.user_marcar))
        self.entry1.pack(pady = 4)
        self.indica1 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica1.pack(pady=2)
        #Contrasenia y entrada
        Label(self.master, text= 'Contraseña', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry2 = Entry(self.master,font=('Comic Sans MS', 12),justify = 'center',  fg='grey', highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5)
        self.entry2.insert(0, self.contra_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.contra_marcar))
        self.entry2.pack(pady=4)
        self.indica2 = Label(self.master, bg='#1D1A1A', fg= 'red', font= ('Arial', 8, 'bold'))
        self.indica2.pack(pady=2)
        Button(self.master, text= 'Iniciar Sesion',  command = self.verificacion_users,activebackground='#1D1A1A',activeforeground='white',  bg='white', font=('Arial', 12,'bold')).pack(pady = 5)
        ruta_reg = 'k1.png'
        logoa = PhotoImage(file=os.path.join(self.program_directory, ruta_reg))
        self.logo3 = logoa.subsample(10)
        self.boton_crear = Button(self.master, image=self.logo3, text='Crear\nUsuario', bg='#1D1A1A', foreground='white', activebackground='white', activeforeground='#1D1A1A', width=80, height=15, font=('Arial', 8, 'bold'),compound=LEFT, command=lambda:self.CrearUsuario_NuevaVent())
        self.boton_crear.place(x=5, y=465)
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TProgressbar", foreground='red', background='white',troughcolor='#1D1A1A', bordercolor='white',lightcolor='#970BD9', darkcolor='black')
        self.barra = ttk.Progressbar(self.master, orient= HORIZONTAL, length=200, mode='determinate', maximum=100, style="TProgressbar")
        self.barra.pack()
        Button(self.master, text= 'Salir', bg='white',activebackground='#1D1A1A',activeforeground='white', bd=0, fg = 'black', font=('Arial', 10,'bold'),command= self.salir).pack(pady = 10)
        #Barra del menu (Creo que solo del inicio sera)
        self.menubar = Menu(self.master, bg='#1D1A1A', fg='white', activebackground='#485B67')
        self.menuinicial = Menu(self.menubar, tearoff=0, bg='#1D1A1A', fg='white', activebackground='#485B67', activeforeground='white')
        self.menuinicial.add_command(label='Cargar Archivo', command=lambda: self.Abrir_Archivo())
        self.menuinicial.add_command(label='Cargar Bloques', command=lambda: self.CrearGraficas())
        self.master.config(menu = self.menubar)
        self.menubar.add_cascade(label='Cargar', menu=self.menuinicial)
        
    #----------------------------Widgets Principal-------------------------------
    #----------------------------Widgets Principal-------------------------------
    #----------------------------Widgets Principal-------------------------------
    
    #----------------------------Creacion Graficas-------------------------------
    #----------------------------Creacion Graficas-------------------------------
    #----------------------------Creacion Graficas-------------------------------
    
    def CrearGraficas(self):
        #ListaLArticulos.Graph()
        #ListaListas.Graph()
        print()
        #ColaTutorial.GraphoCola()
        #ListaUsuariosDB.GraficarArbolB()
        
    #----------------------------Creacion Graficas-------------------------------
    #----------------------------Creacion Graficas-------------------------------
    #----------------------------Creacion Graficas-------------------------------
    
    #----------------------------Carga Masiva Archivos-------------------------------
    #----------------------------Carga Masiva Archivos-------------------------------
    #----------------------------Carga Masiva Archivos-------------------------------
        
    def Abrir_Archivo(self):
        print('Cargando Archivo')
        try:
            archivo = filedialog.askopenfilename(title="Archivo tipo JSON: ", filetypes=(("JSON File", "*.json"),("all files","*.*")))
            with open(archivo) as f:
                data = json.load(f)
            self.Data_archivo = data
            contador = 0
            for i in data['usuarios']:
                #print(i['id'])#Por si acaso agregar el Wallet
                ListaUsuariosDB.add(i['id'], i['nick'], i['password'], i['edad'], i['monedas'], web3.eth.accounts[contador])
                contador += 1
            for i in data['articulos']:
                ListaLArticulos.AgregarCate(i['categoria'])
                ListaArticulosPrim.add(i['id'], i['categoria'], i['nombre'], i['precio'], i['src'])
                #print(i)
            ListaLArticulos.Burbuja()
            ListaArticulosPrim.Bubble()
            for i in data['articulos']:
                ListaLArticulos.agregarArticulo(i['id'], i['categoria'], i['nombre'], i['precio'], i['src'])
            #ColaTutorial.agregardim(data['tutorial']['m'])
            #for i in data['tutorial']['movimientos']:
            #    ColaTutorial.enque(i['x'], i['y'])
            #ListaLArticulos.Display2()
            print('Archivo Cargado con Exito')
        except:
            print('Error')
    
        ListaUsuariosDB.Bubble()
        
    #----------------------------Carga Masiva Archivos-------------------------------
    #----------------------------Carga Masiva Archivos-------------------------------
    #----------------------------Carga Masiva Archivos-------------------------------
        
if __name__ == "__main__":
    ventana = Tk()
    ventana.config(bg='#1D1A1A')
    ventana.title("Proyecto Fase 3 - 201906051 (Inicio)")
    ruta = 'Images/IMGF.png'
    program_directory=sys.path[0]
    ventana.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
    x_wi = 350
    y_he = 500
    xpos = y_he
    ypos = (ventana.winfo_screenheight() // 2) - (y_he // 2) -25
    post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
    ventana.geometry(post)
    ventana.resizable(0,0)
    app = Inicio(ventana)
    app.mainloop()