class NodoAdministrador:
    def __init__(self, nick, password, edad, monedas):
        self.nick = nick
        self.password = password
        self.edad = edad
        self.monedas = monedas
        self.tiempomin = 3
        self.tiemposeg = 0
        self.cantidadceros = 4
        self.strCeros = "0000"
        self.siguiente = None
        self.anterior = None

class ListaUsuarioAdministrador:
    def __init__(self):
        self.cabeza = None
        self.final = None
        self.usuarioiniciado = None
    
    def add(self, nick, password, edad, monedas):
        if self.cabeza == None:
            nodoadmin = NodoAdministrador(nick, password, edad, monedas)
            
            self.cabeza = nodoadmin
            self.final = nodoadmin
        else:
            poderono = False
            temp = self.cabeza
            while temp != None:
                if temp.nick == nick:
                    poderono = False
                    break
                else:
                    poderono = True
                temp = temp.siguiente
            if poderono == True:
                temp = NodoAdministrador(nick, password, edad, monedas)
                
                self.final.siguiente = temp
                temp.anterior = self.final
                self.final = temp
            return
    
    def InicioAdmin(self, nick, password):
        if self.cabeza == None:
            return
        else:
            temp = self.cabeza
            while temp != None:
                if temp.nick == nick and temp.password == password:
                    self.usuarioiniciado = temp
                    return True
                temp = temp.siguiente
            return False
                
    
    def agregartiempocronometro(self, min, seg):
        if self.usuarioiniciado == None:
            return
        else:
            tiempomin = min
            tiemposeg = seg
            self.usuarioiniciado = self.usuarioiniciado
            self.usuarioiniciado.tiempomin = tiempomin
            self.usuarioiniciado.tiemposeg = tiemposeg
            self.ajustarcronometro(tiempomin, tiemposeg)
            
    def ajustarcronometro(self, min, seg):
        temp = self.cabeza
        temp.tiempomin = min
        temp.tiemposeg = seg
    
    def ajustarceros(self, contador):
        temp = self.cabeza.strCeros
        temp = ""
        contando = 0
        while contando < contador:
            temp += "0"
            #print(temp)
            contando += 1    
    
    def modificarceroshash(self, cantidadceros):
        if self.usuarioiniciado == None:
            return
        else:
            self.usuarioiniciado = self.usuarioiniciado
            #self.usuarioiniciado.cantidadceros = cantidadceros
            self.usuarioiniciado.strCeros = cantidadceros
            #print(cantidadceros)
            self.usuarioiniciado.cantidadceros = ""
            
            