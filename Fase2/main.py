
from tkinter import *
from tkinter import ttk
import time
import json
from tkinter import filedialog
import sys, os
from PIL import ImageTk, Image
#ESTRUCTURA DE LA MATRIZ DISPERSA :v
from Structures.Dispersa.MatrizDispersa import Lista, MatrizDispersa
#CONEXION CON C++
#DobleLinkUSR = Nodo de la lista que tiene el arbol
#DobleLUSR = Lista
from Structures.AVL.AVLTree import DobleLUSR
from Structures.ListL.ListadeListas import ListaListas
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
                   #ID Nick  Pass     Edad Mon
ListaUsuariosAV = DobleLUSR()
ListaUsuariosAV.add(1, "EDD", "edd123", 22, 8888)
#Booleano para el ingreso
#Usuario_Esta = False




class Registro(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.user_marcar = "Ingresar Usuario"
        self.contra_marcar = "Ingresar Password"
        self.id_marcar = "Ingresar ID"
        self.edad_marcar = "Ingresar Edad"
        self.money_marcar = "Ingresar Cant. Monedas"
        self.widgets_register()

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
                ListaUsuariosAV.add(id_aceptada, user_aceptado, pass_aceptado, edad_aceptada, moneda_aceptada)
                print('Usuario Creado con Exito')
                #ListaUsuariosAV.Display()
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
        
    def Regresar(self):
        self.master.withdraw()
        self.Ventana_Pric = Toplevel()
        self.Ventana_Pric.config(bg='#1D1A1A')
        self.Ventana_Pric.title("Proyecto Fase 2 - 201906051 (Inicio)")
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

#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------
#-------------CLASE PARA MOSTRAR PRODUCTO SELECCIONADO-------------z
class VentanaProducto(Toplevel):
    def __init__(self, id, precio, nombre, src, categoria, monedausuario, callback=None):
        super().__init__()
        self.callback = callback
        self.config(bg="#1D1A1A")
        self.geometry('500x500+500+100')
        self.resizable(0,0)
        self.title('Articulo Seleccionado: ' + nombre)
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
        self.botonenvio = Button(self, text='comprar', command=self.Compra)
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
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------
#-------------------------Clase Secundaria-------------------------


class Secundaria(Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.usuarioeliminado = False
        self.NoImagenMostrada = ListaUsuariosAV.obtenercantidadjugadas()
        self.DataArchivo = data
        self.UsuarioNombre = ListaUsuariosAV.nombreUsuario()
        self.UsuarioID = ListaUsuariosAV.idUsuario()
        self.UsuarioMoned = ListaUsuariosAV.monedasUsuario()
        self.UsuarioPass = ListaUsuariosAV.passUsuario()
        self.UsuarioPassEncrypt = ListaUsuariosAV.passEncrypt()
        self.UsuarioEdad = ListaUsuariosAV.edadUsuario()
        self.PartidasJugadas = ListaUsuariosAV.obtenercantidadjugadas()
        
        
        self.widgets_sec()
        
        
    #Salida del Usuario
    def regresar(self):
        if self.usuarioeliminado == False:
            ListaUsuariosAV.GraficarArbolUsuarioActivo()
            self.master.withdraw()
            self.Ventana_principal = Toplevel()
            self.Ventana_principal.config(bg='#1D1A1A')
            self.Ventana_principal.title("Proyecto Fase 2 - 201906051 (Inicio)")
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
            self.master.withdraw()
            self.Ventana_principal = Toplevel()
            self.Ventana_principal.config(bg='#1D1A1A')
            self.Ventana_principal.title("Proyecto Fase 2 - 201906051 (Inicio)")
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
    
    def EliminarUsuario(self):
        ListaUsuariosAV.eliminarUsuario(self.UsuarioID)
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
                ListaUsuariosAV.modificarUsuario(IDAceptada, UsuarioAceptado, PassAceptada, EdadAceptada, TokenAceptado)
                self.BloquearCasillas()
                self.refrescar()
                print('Usuario Modificado Correctamente - Regresando al menu principal')
                #self.regresar()
                
    def SeleccionMandar(self):
        print(Button['text'])
        
    def BuscarProducto(self):
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
                #print(self.IDArticulo)
                #print(self.PrecioArticulo)
                #print(self.NombreArticulo)
                self.ventanaProducto = VentanaProducto(self.IDArticulo, self.PrecioArticulo, self.NombreArticulo, self.SRCArticulo, self.CategoriaArticulo, self.UsuarioMoned, callback=self.cantidad)
                #print(self.cantidad)
                #print(self.cantidad)
    
    
    def cantidad(self, cantidad):
        #print(cantidad)
        self.total = cantidad * self.PrecioArticulo
        #print(self.total)
        ListaUsuariosAV.AgregarCompra(int(self.IDArticulo), self.NombreArticulo, int(cantidad), int(self.PrecioArticulo))
        ListaUsuariosAV.RestandoMonedas(int(self.PrecioArticulo), int(cantidad))
        ListaUsuariosAV.ModificarMonedas()
        self.refrescar()
    
    def refrescar(self):
        self.nombreLabel['text'] = ListaUsuariosAV.nombreUsuario()
        self.monedasLAbel['text'] = 'Tokens: '+str(ListaUsuariosAV.monedasUsuario())
        
    
    def widgets_sec(self):
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
        self.nb.add(self.p3, text='Juego')
        self.nb.add(self.p4, text='Tutorial')
        
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        #--------------------------------------- TIENDA ---------------------------------------
        self.ruta = 'Images/nemesis.png'
        self.program_directory = sys.path[0]
        self.logo = PhotoImage(file=os.path.join(self.program_directory, self.ruta))
        self.logo2 = self.logo.subsample(2)
        #self.imagen = Image.open(self.ruta)
        #Imagen donde sale Nemesis
        self.image = Label(self.p1, image = self.logo2, bg='#1D1A1A',height=150, width=200)
        self.image.pack()
        self.image.place(x=20,y=10)
        self.ruta2 = 'Images/a2.png'
        #Imagen de Usuario?
        self.logoa = PhotoImage(file=os.path.join(self.program_directory, self.ruta2))
        self.logo3 = self.logoa.subsample(3)
        self.image2 = Label(self.p1, image = self.logo3, bg='#1D1A1A',height=100, width=100)
        self.image2.pack()
        self.image2.place(x=750,y=10)
        #label de tienda de Skins
        la = Label(self.p1, text= 'Tienda de SKINS', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 24, 'bold'))
        la.pack()
        la.place(y=30, x=320)
        #Boton salida
        self.ruta_boton_salida = 'Images/off.png'
        self.imagen_boton_salida = PhotoImage(file=os.path.join(self.program_directory, self.ruta_boton_salida)).subsample(10)
        boton_salida = Button(self.p1, image=self.imagen_boton_salida, text='Cerrar Sesion', compound=LEFT, bg='#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A', command=lambda:self.regresar())
        boton_salida.place(x=720, y=120)
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
        mycanvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar, bg='#1D1A1A', width=600, height=350)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        mycanvas.pack(side=LEFT)
        #mycanvas.place(x=20, y=180)
        myframe = Frame(mycanvas, bg='#1D1A1A')
        mycanvas.create_window((0,0), window=myframe)
        self.prim.pack()
        self.prim.place(x=20, y=180)
        #Box para buscar articulo
        self.LabelIDProd = Label(self.p1, text='Producto Buscar', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold'))
        self.LabelIDProd.place(x=660, y=320)
        self.entradaIDProd = Entry(self.p1, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E20303", highlightcolor= "#1AD620", highlightthickness = 5, width=20)
        #self.entradaIDProd.insert(0, 'ID Producto Buscar')
        self.entradaIDProd.place(x=690, y=350)
        
        self.ButtonIDProd = Button(self.p1, text= 'Buscar',  command = self.BuscarProducto,activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        self.ButtonIDProd.place(x=730, y=390)
        
        #ListaLArticulos
        x = 0
        ListaGraficar = ListaLArticulos.cabeza
        while ListaGraficar != None:
            i = 0
            #print(ListaGraficar.categoria)
            Label(myframe, text= ListaGraficar.categoria, bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold')).grid(row=x, column=0)
            if ListaGraficar.abajo != None:
                ListaSecGraficar = ListaGraficar.abajo.cabeza
                while ListaSecGraficar != None:
                    #print(str(ListaSecGraficar.id) + "-" + ListaSecGraficar.nombre)
                    Button(myframe, image=self.logo3, text=str(ListaSecGraficar.id), fg='white', bg='#1D1A1A', width=200, height=100, compound=LEFT, command=lambda:self.SeleccionMandar).grid(column=i+1, row=x)
                    i = i + 1
                    ListaSecGraficar = ListaSecGraficar.siguiente
            x = x + 1
            ListaGraficar = ListaGraficar.siguiente
        #for x in range(3):
            #print(NombreUsuario)
            #Label(myframe, text= 'Contraseña', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 16, 'bold')).grid(row=x, column=0)    
            #for i in range(20):
                #Frame(myframe, bg='red', width=200, height=100).grid(column=i, row=1)
                #self.rutabo = 'Images/a2.png'
                #self.logob = PhotoImage(file=os.path.join(self.program_directory, self.rutabo))
                #self.logo4 = self.logob.subsample(3)
                #Button(myframe, image=self.logo3, text='sdf', fg='white', bg='#1D1A1A', width=200, height=100, compound=LEFT).grid(column=i+1, row=x)
                #Frame()
        
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
        self.imagen_en_perfil.place(x=750,y=10)
        #P2 IMAGEN NEMESIS
        self.neme = Label(self.p2, image = self.logo2, bg='#1D1A1A',height=150, width=200)
        self.neme.pack()
        self.neme.place(x=20,y=10)
        #Boton salida
        #self.ruta_boton_salida = 'Images/off.png'
        #self.imagen_boton_salida2 = PhotoImage(file=os.path.join(self.program_directory, self.ruta_boton_salida)).subsample(10)
        boton_salida2 = Button(self.p2, image=self.imagen_boton_salida, text='Cerrar Sesion', compound=LEFT, bg='#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A', command=lambda:self.regresar())
        boton_salida2.place(x=720, y=120)
        #label de Info Usuario
        la2 = Label(self.p2, text= 'Informacion Usuario', bg='#1D1A1A', fg= 'white', font= ('Lucida Sans', 24, 'bold'))
        la2.pack()
        la2.place(y=30, x=300)
        
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
        self.botonmodificar.place(x=720, y=530)
        #Boton eliminar
        self.botonEliminar = Button(self.p2, text= 'Eliminar',  command = self.EliminarUsuario,activebackground='white',activeforeground='#1D1A1A',  bg='#1D1A1A', fg='white', font=('Arial', 10,'bold'))
        #self.botonEliminar.config(state='disabled')
        self.botonEliminar.place(x=720, y=480)
        
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        #--------------------------------------- PERFIL ---------------------------------------
        
        
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        
        
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        #--------------------------------------- JUEGO ---------------------------------------
        
        
                
            

#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
#--------------------------------------------Clase Inicio--------------------------------------------
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
        #ListaUsuarios.add(compra=(5, "sd", 4))
        #self.datos = conexion.Registro_datos()
        self.widgets()
        
        
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
            
    def salir(self):
        self.master.destroy()
        self.master.quit()
        
    def acceder_Ventana_Sec(self):
        for i in  range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.005)
            
        self.master.withdraw()
        self.Ventana_Sec = Toplevel()
        self.Ventana_Sec.title('Proyecto Fase 2 - 201906051')
        x_wi = 900
        y_he = 600
        x_pos = (self.Ventana_Sec.winfo_screenwidth() // 2) - (x_wi // 2)
        y_pos = (self.Ventana_Sec.winfo_screenheight() // 2) - (y_he // 2) - 25
        position = str(x_wi) + "x" + str(y_he) + "+" + str(x_pos) + "+" + str(y_pos)
        self.Ventana_Sec.geometry(position)
        self.Ventana_Sec.resizable(0,0)
        self.Ventana_Sec.protocol("WM_DELETE_WINDOW", self.salir)
        self.Ventana_Sec.config(bg= '#1D1A1A')
        app2 = Secundaria(self.Ventana_Sec, self.Data_archivo)#Agregar las variables
        #print(self.UsuarioID)
        #print(self.UsuarioNombre)
        app2.mainloop()
        
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
        
        
        
        #self.Ventana_Sec.state('zoomed')
        
        #Label(self.Ventana_Sec, text='VENTANA DOS', font='Arial 40', bg= '#1D1A1A', fg='white').pack(expand=True)
        #Button(self.Ventana_Sec, text='Salir', font='Arial 10', bg= '#1D1A1A', fg='white', activebackground='white', activeforeground='#1D1A1A',command= self.salir).pack(expand=True)
        
    def verificacion_users(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()
        self.UsuarioIngresado = ListaUsuariosAV.InicioSecion(users_entry, password_entry)
        #print(Usuario_Activo) #Deveria mostrar un true or false
        if self.UsuarioIngresado == True:
            self.UsuarioNombre = ListaUsuariosAV.nombreUsuario()
            self.UsuarioID = ListaUsuariosAV.idUsuario()
            self.UsuarioMoned = ListaUsuariosAV.monedasUsuario()
            self.PartidasJugadas = ListaUsuariosAV.obtenercantidadjugadas()
            print("Bienvenido: " + self.UsuarioNombre)
            #print(IDUsuario)
            #print(MonedasUsuario)
            #print(PartidasJugadas)
            self.acceder_Ventana_Sec()
        
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
        
    
    def widgets(self):
        self.ruta = 'IM.png'
        self.program_directory = sys.path[0]
        self.logo = PhotoImage(file=os.path.join(self.program_directory, self.ruta))
        self.logo2 = self.logo.subsample(2)
        #self.imagen = Image.open(self.ruta)
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
        self.menuinicial.add_command(label='Generar Graficas', command=lambda: self.CrearGraficas())
        self.master.config(menu = self.menubar)
        self.menubar.add_cascade(label='Cargar', menu=self.menuinicial)
        #self.menubar.add_cascade(label='Generar Graficos', menu=self.menuinicial)
    
    def CrearGraficas(self):
        ListaLArticulos.Graph()
        #ListaListas.Graph()
        ColaTutorial.GraphoCola()
        ListaUsuariosAV.GraficarArbolB()
        
        
    
    def Abrir_Archivo(self):
        print('Cargando Archivo')
        try:
            archivo = filedialog.askopenfilename(title="Archivo tipo JSON: ", filetypes=(("JSON File", "*.json"),("all files","*.*")))
            
            with open(archivo) as f:
                data = json.load(f)
            self.Data_archivo = data;  
            for i in data['usuarios']:
                #print(i['id'])
                ListaUsuariosAV.add(i['id'], i['nick'], i['password'], i['edad'], i['monedas'])
            ListaUsuariosAV.Bubble()
            for i in data['articulos']:
                ListaLArticulos.AgregarCate(i['categoria'])
                ListaArticulosPrim.add(i['id'], i['categoria'], i['nombre'], i['precio'], i['src'])
                #print(i)
            ListaLArticulos.Burbuja()
            ListaArticulosPrim.Bubble()
            for i in data['articulos']:
                ListaLArticulos.agregarArticulo(i['id'], i['categoria'], i['nombre'], i['precio'], i['src'])
            
            ColaTutorial.agregardim(data['tutorial']['m'])
            for i in data['tutorial']['movimientos']:
                ColaTutorial.enque(i['x'], i['y'])
                
            ListaLArticulos.Display2()
            #ColaTutorial.peek()
            #ColaTutorial.dequeue()
            #ColaTutorial.peek()
            #ListaLArticulos.Display()
            
            print('Archivo Cargado con Exito')
        except:
            print('Error')
        
        
      
      
      
        
if __name__ == "__main__":
    ventana = Tk()
    ventana.config(bg='#1D1A1A')
    ventana.title("Proyecto Fase 2 - 201906051 (Inicio)")
    ruta = 'Images/IMGF.png'
    program_directory=sys.path[0]
    ventana.iconphoto(True, PhotoImage(file=os.path.join(program_directory, ruta)))
    x_wi = 350
    y_he = 500
    xpos = y_he
    ypos = (ventana.winfo_screenheight() // 2) - (y_he // 2) -25
    #ventana.geometry('350x500+500+50')
    post = str(x_wi) + 'x' + str(y_he) + '+' + str(xpos) + '+' + str(ypos)
    #print(post)
    ventana.geometry(post)
    #ventana.overrideredirect(1)
    ventana.resizable(0,0)
    app = Inicio(ventana)
    app.mainloop()
        
        
        
        
            
            
            
