class Nodo_inicial:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.siguiente = None
        
class Lista_Coordenadas:
    def __init__(self):
        self.cabeza = None
        self.vacia = False
        self.long = 0
        self.numbacia = 0
        
    def Agregar_Coordenada(self, row, col):
        nodo = Nodo_inicial(row, col)
        if self.cabeza == None:
            self.cabeza = nodo
            self.long += 1
        else:
            puntero = self.cabeza
            while puntero.siguiente != None:
                puntero = puntero.siguiente
            puntero.siguiente = nodo
            self.long += 1
            
    def estaVacia(self):
        if self.cabeza == None:
            self.vacia = True
            self.numbacia = 1
            #print('Barco Caido')
        else:
            self.vacia = False
            self.numbacia = 0
    
    def Mostrar_Coordenadas(self):
        if self.cabeza == None:
            print('none')
            return
        else:
            temp = self.cabeza
            while temp != None:
                print('x: ' +  str(temp.col) + ' y: ' + str(temp.row))
                temp = temp.siguiente
    
    def buscarEliminar(self, row, col):
        if self.cabeza == None:
            return
        else:
            temp = self.cabeza
            if temp == None:
                return
            else:
                puntero = self.cabeza
                contador = 1
                while puntero != None:
                    if puntero.col == col and puntero.row == row:
                        self.Eliminar_Movimiento(contador, row, col)
                        break
                    contador += 1
                    puntero = puntero.siguiente
            
    def Eliminar_Movimiento(self, pos,row, col):
        if self.cabeza == None:
            return
        else:
            if pos == 1:
                primer = self.cabeza
                self.cabeza = self.cabeza.siguiente
                primer.siguiente = None
                self.long -= 1
            else:
                temp = self.cabeza
                contador = 1
                while contador < (pos - 1):
                    temp = temp.siguiente
                    contador += 1
                aux = temp.siguiente
                temp.siguiente = aux.siguiente
                aux.siguiente = None
                self.long -= 1
    
                    
class Nodo_Barco:
    def __init__(self, nombre_barco):
        self.id_barco = 0
        self.nombre_barco = nombre_barco
        self.coordenadas = Lista_Coordenadas()
        self.siguiente = None
        self.anterior = None
        
class Barcos_List:
    def __init__(self):
        self.contador = 0
        self.cabeza = None
        self.final = None
        self.Barcos_Hundidos = 0
        self.Barcos_Vivos = 0
    
    def agregarBarco(self, nombre_barco):
        self.contador += 1
        nodo = Nodo_Barco(nombre_barco)
        nodo.id_barco = self.contador
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            temp = self.cabeza
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = nodo
        #nodo = Nodo_Barco(nombre_barco)
        #nodo.id_barco = self.contador
        #if self.cabeza == None:
        #    self.cabeza = nodo
        #    self.final = nodo
        #    return
        #else:
        #    self.final.siguiente = nodo
        #    nodo.anterior = self.final
        #    self.final = nodo
        #    return
    
    def agregarCoordenadas(self, id, row, col):
        if self.cabeza == None:
            return
        else:
            temp = self.cabeza
            while temp != None:
                if temp.id_barco == id:
                    temp.coordenadas.Agregar_Coordenada(row, col)
                    return
                temp = temp.siguiente
    
    def eliminarCoordenada(self, id, row, col):
        if self.cabeza == None:
            self.cabeza = None
            return
        else:
            temp = self.cabeza
            while(temp != None):
                if temp.id_barco == id:
                    temp.coordenadas.buscarEliminar(row, col)
                    return
                temp = temp.siguiente
    
    def eliminarBarco(self, id):
        if self.cabeza == None:
            return
        else:
            self.contador -= 1
            if id == 1:
                primer = self.cabeza
                self.cabeza = self.cabeza.siguiente
                primer.siguiente = None
            else:
                temp = self.cabeza
                contador = 1
                while contador < (id - 1):
                    temp = temp.siguiente
                    contador += 1
                aux = temp.siguiente
                temp.siguiente = aux.siguiente
                aux.siguiente = None
        #temp = None
        #self.contador -= 1
        #if self.cabeza == None:
        #    return
        #else:
        #    if self.cabeza.id_barco == id:
        #        temp = self.cabeza
        #        self.cabeza = self.cabeza.siguiente
        #        if self.cabeza != None:
        #            self.cabeza.anterior = None
        #        else:
        #            self.final = None
        #    elif self.final.id_barco == id:
        #        temp = self.final
        #        self.final = self.final.anterior
        #        if self.final != None:
        #            self.final.siguiente = None
        #        else:
        #            self.cabeza = None
        #    else:
        #        temp = self.cabeza
        #        while temp != None and temp.id_barco == id:
        #            temp = temp.siguiente
        #        if temp == None:
        #            return
        #        else:
        #            temp.anterior.siguiente = temp.siguiente
        #            if temp.siguiente != None:
        #                temp.siguiente.anterior = temp.anterior
    
    def eliminarTodosBarcos(self):
        val = 0
        while val <= self.contador + 40:
            self.eliminarBarco(1)
            val += 1
            
    
    def BuscarEliminar(self, row, col):
        if self.cabeza == None:
            return
        else:
            temp = self.cabeza
            valx = 1
            while valx <= self.contador:
                if valx == temp.id_barco:
                    if temp.coordenadas != None:
                        aux = temp.coordenadas.cabeza
                        while aux != None:
                            if aux.row == row and aux.col == col:
                                print('Barco Alcanzado :"v')
                                self.eliminarCoordenada(valx, row, col)
                                break
                            else:
                                aux = aux.siguiente
                temp = temp.siguiente
                valx += 1
        
    def Mostrar_Barcos(self):
        if self.cabeza == None:
            return
        else:
            temp = self.cabeza
            print('Barco:: ' + temp.nombre_barco)
            while temp != None:
                print('ID Barco: ' + str(temp.id_barco))
                if temp.coordenadas != None:
                    aux = temp.coordenadas
                    aux.Mostrar_Coordenadas()
                temp = temp.siguiente

    def Barcos_En_Pie(self):
        if self.cabeza == None:
            return
        else:
            self.Barcos_Vivos = 0
            temp = self.cabeza
            while temp != None:
                if temp.coordenadas != None:
                    aux = temp.coordenadas
                    
                    aux.estaVacia()
                    if aux.numbacia == 0:
                        self.Barcos_Vivos += 1
                temp = temp.siguiente
    
    def Barcos_Caidos(self):
        contador = self.contador
        barcosexistentes = self.Barcos_Vivos
        self.Barcos_Hundidos = contador - barcosexistentes
        
        

#Funcional
#barcos = Barcos_List()
#barcos.agregarBarco('barco')
#barcos.agregarBarco('barco')
#barcos.agregarBarco('barco')
#barcos.agregarBarco('barco')
#barcos.agregarBarco('barco')
#barcos.agregarCoordenadas(1, 5, 1)
#barcos.agregarCoordenadas(1, 5, 2)
#barcos.agregarCoordenadas(1, 5, 3)
#barcos.agregarCoordenadas(1, 6, 1)
#barcos.agregarCoordenadas(1, 7, 1)
#barcos.agregarCoordenadas(1, 8, 1)
#barcos.agregarCoordenadas(2, 5, 1)
#barcos.agregarCoordenadas(2, 6, 1)
#barcos.agregarCoordenadas(3, 6, 2)
#barcos.agregarCoordenadas(3, 6, 3)
#barcos.agregarCoordenadas(4, 5, 5)
#barcos.Mostrar_Barcos()
#barcos.BuscarEliminar(8,9)
#barcos.BuscarEliminar(5,1)
#barcos.BuscarEliminar(5,2)
#barcos.BuscarEliminar(6,2)
#barcos.BuscarEliminar(5,3)
#barcos.BuscarEliminar(7,1)
#barcos.BuscarEliminar(6,1)
#
#barcos.Mostrar_Barcos()
#barcos.Barcos_En_Pie()
#barcos.Barcos_Caidos()
#print('barcos vivos',barcos.Barcos_Vivos)
#print(barcos.contador)
#print('barcos muertos ',barcos.Barcos_Hundidos)
#
#

