import os

class NodoGanador:
    def __init__(self, id, row, col):
        self.row = row
        self.col = col
        self.id = id
        self.siguiente = None
        self.acceso = None

class ListaCoordenadasGanador:
    def __init__(self):
        self.cabeza = None
        self.long = 0
    
    def agregarID(self, id, row, col):
        temp = NodoGanador(id, row, col)
        if self.cabeza == None:
            self.cabeza = temp
            self.long += 1
        else:
            puntero = self.cabeza
            while puntero.siguiente != None:
                puntero = puntero.siguiente
            puntero.siguiente = temp
            self.long += 1

class NodoListaGanador:
    def __init__(self, id):
        self.id = id
        self.listasecundaria = ListaCoordenadasGanador()
        self.siguiente = None
        self.anterior = None
    
class ListaGanador:
    def __init__(self):
        self.contador = 0
        self.cabeza = None
        self.final = None
    
    def agregarID(self, id):
        self.contador += 1
        temp = NodoListaGanador(id)
        if self.cabeza == None:
            self.cabeza = temp
            self.final = temp
            return
        else:
            self.final.siguiente = temp
            temp.anterior = self.final
            self.final = temp
            return
    
    def agregarCoordenadaseID(self, id, row, col):
        if self.cabeza == None:
            return
        else:
            temp = self.cabeza
            while temp != None:
                if temp.id == id:
                    temp.listasecundaria.agregarID(temp.id, row, col)
                    return
                temp = temp.siguiente
    
    def eliminarB(self, id):
        temp = None
        if self.cabeza == None:
            return
        else:
            if self.cabeza.id == id:
                temp = self.cabeza
                self.cabeza = self.cabeza.siguiente
                self.contador -= 1
                if self.cabeza != None:
                    self.cabeza.anterior = None
                else:
                    self.final = None
            elif self.final.id == id:
                temp = self.final
                self.final = self.final.anterior
                self.contador -= 1
                if self.final != None:
                    self.final.siguiente = None
                else:
                    self.cabeza = None
            else:
                temp = self.cabeza
                while temp != None and temp.id != id:
                    temp = temp.siguiente
                if temp == None:
                    return
                else:
                    temp.anterior.siguiente = temp.siguiente
                    if temp.siguiente != None:
                        temp.siguiente.anterior = temp.anterior
                        
    def eliminarTodo(self):
        val = 1
        if self.contador > 0:
            while val <= self.contador:
                self.eliminarB(val)
                val += 1
            
    def GraphAdyacencia(self):
        dot = 'digraph G{\n\tcolor="transparent";\n'
        dot += '\tsubgraph cluster_0{\n\t\tnode[shape=box];\n\t\tedge[color="gray38"];\n'
        dot += '\t\tsubgraph date_inicial{\n'
        dot += '\t\t\trank=NS;\n\t\t\tnode[color="orangered1", fontcolor="orangered1"];\n'
        pivote = self.cabeza
        while pivote != None:
            #if pivote.listasecundaria.cabeza != None:
            dot += '\t\t\ty{}[label="{}"];\n'.format(pivote.id, pivote.id)
            pivote = pivote.siguiente
        pivote = self.cabeza
        while pivote.siguiente != None:
            dot += '\t\t\ty{} -> y{};\n'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        dot += '\t\t}\n'
        pos = 0
        pivote = self.cabeza
        while pivote != None:
            dot += '\t\tsubgraph sub_'+str(pos)+'{\n\t\t\trank=same;\n\t\t\tnode[color="darkslateblue", fontcolor="darkslateblue"];\n'
            if pivote.listasecundaria.cabeza != None:
                aux = pivote.listasecundaria.cabeza
                while aux != None:
                    dot += '\t\t\ti{}_{}[label="X{}"];\n'.format(aux.row, aux.col, aux.col)
                    aux = aux.siguiente
                aux = pivote.listasecundaria.cabeza
                while aux.siguiente != None:
                    dot += '\t\t\ti{}_{} -> i{}_{};\n'.format(aux.row, aux.col, aux.siguiente.row, aux.siguiente.col)
                    aux = aux.siguiente
                aux = pivote.listasecundaria.cabeza
                dot += '\t\t\ty{} -> i{}_{};\n'.format(aux.id, aux.row, aux.col)
            dot += '\t\t}\n'
            pivote = pivote.siguiente
            pos += 1
        dot += '\t}\n'
        dot += '\tsubgraph cluster_1{\n\t\tnode[color="firebrick", fontcolor="firebrick"];\n\t\tedge[color="dimgrey"];\n'
        pivote = self.cabeza
        
        pivote = self.cabeza
        while pivote != None:
            if pivote.listasecundaria.cabeza != None:
                aux = pivote.listasecundaria.cabeza
                while aux != None:
                    dot += '\t\tr{}[label="{}"];\n'.format(aux.id, aux.id)
                    dot += '\t\tr{}[label="{}"];\n'.format(aux.col, aux.col)
                    dot += '\t\tr{} -> r{};\n'.format(aux.id, aux.col)
                    aux = aux.siguiente
            pivote = pivote.siguiente
        
        dot += '\t}\n'
        dot += '}'
        #print(dot)
        with open("Images/AdyacenciaGraph.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("dot -Tsvg Images/AdyacenciaGraph.dot -o Images/AdyacenciaGraph.svg")
        
        

class Nodo_cabecera:
    def __init__(self, _id):
        self.id = _id
        self.siguiente = None
        self.anterior = None
        self.acceso = None

class Nodo_Celda:
    def __init__(self, row, col, libro):
        self.coordenadaX = row
        self.coordenadaY = col
        self.libro = libro
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

class Lista_Cabecera:
    def __init__(self, tipo):
        self.primero = None
        self.ultimo = None
        self.tipo = tipo
        self.size = 0
    
    def insertar_nodoCabecera(self, nuevo):
        self.size += 1
        if(self.primero == None):
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            if(nuevo.id < self.primero.id):
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            if(self.ultimo.id < nuevo.id):
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                temporal = self.primero
                while(temporal != None):
                    if(nuevo.id < temporal.id):
                        nuevo.siguiente = temporal
                        nuevo.anterior = temporal.anterior
                        temporal.anterior.siguiente = nuevo
                        temporal.anterior = nuevo
                        break
                    if(temporal.id < nuevo.id):
                        temporal = temporal.siguiente
                    else:
                        break
                        
    def getCabecera(self, _id):
        temporalCabecera = self.primero
        while temporalCabecera != None:
            if temporalCabecera.id == _id:
                return temporalCabecera
            temporalCabecera = temporalCabecera.siguiente
        
    
class Matriz_Dispesa:
    def __init__(self):
        self.filas = Lista_Cabecera("fila")
        self.columnas = Lista_Cabecera("columna")
        self.capa = 0
        self.Adyacencia = ListaGanador()
        self.validator_number = 0
        
    def insertar(self, row, col, libro):
        nueva_celda = Nodo_Celda(row, col, libro)
        nodo_x = self.filas.getCabecera(row)
        nodo_y = self.columnas.getCabecera(col)
        
        if(nodo_x == None):
            nodo_x = Nodo_cabecera(row)
            self.filas.insertar_nodoCabecera(nodo_x)
            
        if(nodo_y == None):
            nodo_y = Nodo_cabecera(col)
            self.columnas.insertar_nodoCabecera(nodo_y)
        
        if(nodo_x.acceso == None):
            nodo_x.acceso = nueva_celda
        else:
            if(nueva_celda.coordenadaY < nodo_x.acceso.coordenadaY):
                nueva_celda.derecha = nodo_x.acceso
                nodo_x.acceso.izquierda = nueva_celda
                nodo_x.acceso = nueva_celda
            else:
                temp = nodo_x.acceso
                while temp != None:
                    if(nueva_celda.coordenadaY < temp.coordenadaY):
                        nueva_celda.derecha = temp
                        nueva_celda.izquierda = temp.izquierda
                        temp.izquierda.derecha = nueva_celda
                        temp.izquierda = nueva_celda
                        break
                    if(nueva_celda.coordenadaX == temp.coordenadaX and nueva_celda.coordenadaY == temp.coordenadaY):
                        break
                    else:
                        if(temp.derecha == None):
                            temp.derecha = nueva_celda
                            nueva_celda.izquierda = temp
                            break
                        else:
                            temp = temp.derecha
        
        if(nodo_y.acceso == None):
            nodo_y.acceso = nueva_celda
            
        else:
            if(nueva_celda.coordenadaX < nodo_y.acceso.coordenadaX):
                nueva_celda.abajo = nodo_y.acceso
                nodo_y.acceso.arriba = nueva_celda
                nodo_y.acceso = nueva_celda
            else:
                temp2 = nodo_y.acceso
                while(temp2 != None):
                    if(nueva_celda.coordenadaX < temp2.coordenadaX):
                        nueva_celda.abajo = temp2
                        nueva_celda.arriba = temp2.arriba
                        temp2.arriba.abajo = nueva_celda
                        temp2.arriba = nueva_celda
                        break
                    if(nueva_celda.coordenadaX == temp2.coordenadaX and nueva_celda.coordenadaY == temp2.coordenadaY):
                        break
                    else:
                        if(temp2.abajo == None):
                            temp2.abajo = nueva_celda
                            nueva_celda.arriba = temp2
                            break
                        else:
                            temp2 = temp2.abajo
    
    def imprimir(self):
        nodo = self.filas.getCabecera()
    
    def is_empty(self, structure):
        if structure:
            return False
        else:
            return True
    
    def EliminarTodo(self):
        valx = 1
        while valx <= self.m:
            valy = 1
            self.columnas.getCabecera(valx).acceso = None
            while valy <= self.m:
                self.filas.getCabecera(valy).acceso = None
                valy += 1
                
            valx +=1
            
    def modificar(self, row, col, libro):
        nodo = self.filas.getCabecera(row).acceso
        while(nodo != None):
            if(nodo.coordenadaX == row and nodo.coordenadaY == col):
                nodo.libro = libro
                break
            nodo = nodo.derecha
    
    def llenarTablero(self, m):
        self.m = m
        i = 1
        while i <= m:
            j = 1
            while j <= m:
                self.insertar(j, i, "")
                j += 1
            i += 1
    
    def eliminarTabGanador(self):
        self.Adyacencia.eliminarTodo()
    
    def graficarTabGanador(self):
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            #dot += '\t\t\ty{}[label="{}"];\n'.format(pivote.id, pivote.id)
            self.Adyacencia.agregarID(pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda = pivote.acceso
            #dot += '\t\tsubgraph sub_' + str(posx) + ' {\n\t\t\trank=same;\n\t\t\tnode[color="darkslateblue", fontcolor="darkslateblue"];\n'
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivote.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.libro == 'X':
                    
                    self.Adyacencia.agregarCoordenadaseID(pivote_celda.coordenadaX, pivote_celda.coordenadaX, pivote_celda.coordenadaY)
                    #dot += '\t\t\ti{}_{}[label="X{}"];\n'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.coordenadaY)
                pivote_celda = pivote_celda.derecha
            
            
            pivote = pivote.siguiente
            posx += 1
        self.Adyacencia.GraphAdyacencia()
        #dot += '\t}\n'
        #dot += '\tsubgraph cluster_1{\n'
        #dot += '\t}\n}'
        #print(dot)
        #with open("Images/AdyacenciaGraph.dot", 'w') as grafo:
        #    grafo.write(dot)
        #os.system("dot -Tpng Images/AdyacenciaGraph.dot -o Images/AdyacenciaGraph.png")
        
        
    
    def graficarNeato(self):
        dot = 'digraph G{\nlayout=neato;\nbgcolor="none";\nranksep=2;\nnodesep=2;\n'
        dot += 'node[shape=box, width=0.5, height=0.5, fontname="Arial", fillcolor="white", style=filled];\n'
        dot += 'edge[dir="both", color="red"];\n'
        dot += 'raiz[label="", fillcolor="black", pos="-1,1!"];\n'
        dot += 'label="Tablero";\nfontname="Arial Black";\nfontsize="25pt";'
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            dot += '\n\ty{}[label="{}", fillcolor="black", fontcolor="white", pos="-1,-{}!"];'.format(pivote.id, pivote.id, posx)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            dot += '\n\t\ty{} -> y{};'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        dot += '\n\t\traiz -> y{};'.format(self.filas.primero.id)
        
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            dot += '\n\tx{}[label="{}", fillcolor="black", fontcolor="white", pos="{}, 1!"];'.format(pivotey.id, pivotey.id, posy)
            pivotey = pivotey.siguiente
            posy += 1
            
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            dot += '\n\t\tx{} -> x{};'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        dot += '\n\t\traiz -> x{};'.format(self.columnas.primero.id)
        
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                    #Aqui condicionales para poder poner color a los barcos UwU
                dot += '\n\ti{}_{}[label="{}", fillcolor="gray", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            #print(pivote_celda)
            while(pivote_celda != None):
                if(pivote_celda.derecha != None):
                    #print(pivote_celda.coordenadaX)
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
            dot += '\n\t\ty{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
            
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            dot += '\n\tx{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        
        dot += '\n}'
        #print(dot)
        with open("Images/Tablero.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("neato -Tsvg Images/Tablero.dot -o Images/Tablero.svg")

    def graficarTablero(self):
        dot = 'digraph G{\nlayout=neato;\nbgcolor="none";\nranksep=2;\nnodesep=2;\n'
        dot += 'node[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled];\n'
        dot += 'edge[dir="both", color="red", style=invis];\n'
        dot += 'raiz[label="", fillcolor="black", pos="-1,1!"];\n'
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            dot += '\n\ty{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="-1,-{}!"];'.format(pivote.id, pivote.id, posx)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            dot += '\n\t\ty{} -> y{};'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        dot += '\n\t\traiz -> y{};'.format(self.filas.primero.id)
        
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            dot += '\n\tx{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="{}, 1!"];'.format(pivotey.id, pivotey.id, posy)
            pivotey = pivotey.siguiente
            posy += 1
            
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            dot += '\n\t\tx{} -> x{};'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        dot += '\n\t\traiz -> x{};'.format(self.columnas.primero.id)
        
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                    #Aqui condicionales para poder poner color a los barcos UwU
                #pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                #Portaviones Level 4
                if pivote_celda.libro == 'Level4':
                    dot += '\n\ti{}_{}[label=<<B>P</B>>, fillcolor="maroon", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Submarino Level 3
                if pivote_celda.libro == 'Level3':
                    dot += '\n\ti{}_{}[label=<<B>S</B>>, fillcolor="navy", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Destructor Level 2
                if pivote_celda.libro == 'Leve2' or pivote_celda.libro == 'Level2':
                    dot += '\n\ti{}_{}[label=<<B>D</B>>, fillcolor="gray", color="white", fontsize="30", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Buque Level 1
                if pivote_celda.libro == 'Level1':
                    dot += '\n\ti{}_{}[label=<<B>B</B>>, fillcolor="teal", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #None
                if pivote_celda.libro == '':
                    dot += '\n\ti{}_{}[label="", fillcolor="azure", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Disparo
                if pivote_celda.libro == 'X':
                    dot += '\n\ti{}_{}[label=<<B>X</B>>, fillcolor="darkred", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                
                #dot += '\n\ti{}_{}[label="{}", fillcolor="gray", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            #print(pivote_celda)
            while(pivote_celda != None):
                if(pivote_celda.derecha != None):
                    #print(pivote_celda.coordenadaX)
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
            dot += '\n\t\ty{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
            
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            dot += '\n\tx{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        
        dot += '\n}'
        #print(dot)
        with open("Images/TabPJ1.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("neato -Tpng Images/TabPJ1.dot -o Images/TabPJ1.png")

    def graficarTableroPJ2(self):
        dot = 'digraph G{\nlayout=neato;\nbgcolor="none";\nranksep=2;\nnodesep=2;\n'
        dot += 'node[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled];\n'
        dot += 'edge[dir="both", color="red", style=invis];\n'
        dot += 'raiz[label="", fillcolor="black", pos="-1,1!"];\n'
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            dot += '\n\ty{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="-1,-{}!"];'.format(pivote.id, pivote.id, posx)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            dot += '\n\t\ty{} -> y{};'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        dot += '\n\t\traiz -> y{};'.format(self.filas.primero.id)
        
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            dot += '\n\tx{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="{}, 1!"];'.format(pivotey.id, pivotey.id, posy)
            pivotey = pivotey.siguiente
            posy += 1
            
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            dot += '\n\t\tx{} -> x{};'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        dot += '\n\t\traiz -> x{};'.format(self.columnas.primero.id)
        
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                    #Aqui condicionales para poder poner color a los barcos UwU
                #pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                #Portaviones Level 4
                if pivote_celda.libro == 'Level4':
                    dot += '\n\ti{}_{}[label=<<B>P</B>>, fillcolor="maroon", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Submarino Level 3
                if pivote_celda.libro == 'Level3':
                    dot += '\n\ti{}_{}[label=<<B>S</B>>, fillcolor="navy", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Destructor Level 2
                if pivote_celda.libro == 'Level2':
                    dot += '\n\ti{}_{}[label=<<B>D</B>>, fillcolor="gray", color="white", fontsize="30", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Buque Level 1
                if pivote_celda.libro == 'Level1':
                    dot += '\n\ti{}_{}[label=<<B>B</B>>, fillcolor="teal", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #None
                if pivote_celda.libro == '':
                    dot += '\n\ti{}_{}[label="", fillcolor="azure", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Disparo
                if pivote_celda.libro == 'X':
                    dot += '\n\ti{}_{}[label=<<B>X</B>>, fillcolor="darkred", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                
                #dot += '\n\ti{}_{}[label="{}", fillcolor="gray", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            #print(pivote_celda)
            while(pivote_celda != None):
                if(pivote_celda.derecha != None):
                    #print(pivote_celda.coordenadaX)
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
            dot += '\n\t\ty{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
            
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            dot += '\n\tx{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        
        dot += '\n}'
        #print(dot)
        with open("Images/TabPJ2.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("neato -Tpng Images/TabPJ2.dot -o Images/TabPJ2.png")
        
    def GraficarMiniTableroPJ2(self):
        dot = 'digraph G{\nlayout=neato;\nbgcolor="none";\nranksep=2;\nnodesep=2;\n'
        dot += 'node[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled];\n'
        dot += 'edge[dir="both", color="red", style=invis];\n'
        dot += 'raiz[label="", fillcolor="black", pos="-1,1!"];\n'
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            dot += '\n\ty{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="-1,-{}!"];'.format(pivote.id, pivote.id, posx)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            dot += '\n\t\ty{} -> y{};'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        dot += '\n\t\traiz -> y{};'.format(self.filas.primero.id)
        
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            dot += '\n\tx{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="{}, 1!"];'.format(pivotey.id, pivotey.id, posy)
            pivotey = pivotey.siguiente
            posy += 1
            
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            dot += '\n\t\tx{} -> x{};'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        dot += '\n\t\traiz -> x{};'.format(self.columnas.primero.id)
        
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                    #Aqui condicionales para poder poner color a los barcos UwU
                #pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                #Portaviones Level 4
                #if pivote_celda.libro == 'Level4':
                #    dot += '\n\ti{}_{}[label=<<B>P</B>>, fillcolor="maroon", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##Submarino Level 3
                #if pivote_celda.libro == 'Level3':
                #    dot += '\n\ti{}_{}[label=<<B>S</B>>, fillcolor="navy", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##Destructor Level 2
                #if pivote_celda.libro == 'Level2':
                #    dot += '\n\ti{}_{}[label=<<B>D</B>>, fillcolor="gray", color="white", fontsize="30", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##Buque Level 1
                #if pivote_celda.libro == 'Level1':
                #    dot += '\n\ti{}_{}[label=<<B>B</B>>, fillcolor="teal", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##None
                if pivote_celda.libro == '':
                    dot += '\n\ti{}_{}[label="", fillcolor="azure", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Disparo
                if pivote_celda.libro == 'X':
                    dot += '\n\ti{}_{}[label=<<B>X</B>>, fillcolor="darkred", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                
                #dot += '\n\ti{}_{}[label="{}", fillcolor="gray", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            #print(pivote_celda)
            while(pivote_celda != None):
                if(pivote_celda.derecha != None):
                    #print(pivote_celda.coordenadaX)
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
            dot += '\n\t\ty{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
            
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            dot += '\n\tx{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        
        dot += '\n}'
        #print(dot)
        with open("Images/MinTabPJ2.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("neato -Tpng Images/MinTabPJ2.dot -o Images/MinTabPJ2.png")
        
    def GraficarMiniTableroPJ1(self):
        dot = 'digraph G{\nlayout=neato;\nbgcolor="none";\nranksep=2;\nnodesep=2;\n'
        dot += 'node[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled];\n'
        dot += 'edge[dir="both", color="red", style=invis];\n'
        dot += 'raiz[label="", fillcolor="black", pos="-1,1!"];\n'
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            dot += '\n\ty{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="-1,-{}!"];'.format(pivote.id, pivote.id, posx)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            dot += '\n\t\ty{} -> y{};'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        dot += '\n\t\traiz -> y{};'.format(self.filas.primero.id)
        
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            dot += '\n\tx{}[label=<<B>{}</B>>, fillcolor="black", fontcolor="white", fontsize="30", pos="{}, 1!"];'.format(pivotey.id, pivotey.id, posy)
            pivotey = pivotey.siguiente
            posy += 1
            
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            dot += '\n\t\tx{} -> x{};'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        dot += '\n\t\traiz -> x{};'.format(self.columnas.primero.id)
        
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY:
                        break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                    #Aqui condicionales para poder poner color a los barcos UwU
                #pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                #Portaviones Level 4
                #if pivote_celda.libro == 'Level4':
                #    dot += '\n\ti{}_{}[label=<<B>P</B>>, fillcolor="maroon", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##Submarino Level 3
                #if pivote_celda.libro == 'Level3':
                #    dot += '\n\ti{}_{}[label=<<B>S</B>>, fillcolor="navy", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##Destructor Level 2
                #if pivote_celda.libro == 'Level2':
                #    dot += '\n\ti{}_{}[label=<<B>D</B>>, fillcolor="gray", color="white", fontsize="30", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##Buque Level 1
                #if pivote_celda.libro == 'Level1':
                #    dot += '\n\ti{}_{}[label=<<B>B</B>>, fillcolor="teal", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                ##None
                if pivote_celda.libro == '':
                    dot += '\n\ti{}_{}[label="", fillcolor="azure", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                #Disparo
                if pivote_celda.libro == 'X':
                    dot += '\n\ti{}_{}[label=<<B>X</B>>, fillcolor="darkred", fontcolor="white", fontsize="30", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, posy_celda, posx)    
                
                #dot += '\n\ti{}_{}[label="{}", fillcolor="gray", color="white", pos="{},-{}!"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.libro, posy_celda, posx)
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            #print(pivote_celda)
            while(pivote_celda != None):
                if(pivote_celda.derecha != None):
                    #print(pivote_celda.coordenadaX)
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
            dot += '\n\t\ty{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
            
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    dot += '\n\t\ti{}_{} -> i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY, pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                pivote_celda = pivote_celda.abajo
            dot += '\n\tx{} -> i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        
        dot += '\n}'
        #print(dot)
        with open("Images/MinTabPJ1.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("neato -Tpng Images/MinTabPJ1.dot -o Images/MinTabPJ1.png")

#print(matriz.is_empty(matriz.porta1))
#matriz.porta1.append({'x':1, 'y':5})
#print(matriz.is_empty(matriz.porta1))
#print(matriz.porta1[0]['y'])
#matriz.porta1.pop(0)
#print(matriz.is_empty(matriz.porta1))
#print(matriz.porta1)

#matriz = Matriz_Dispesa()
#matriz.llenarTablero(1)
#matriz.modificar(5, 5, "Level1")
#matriz.modificar(12, 2, "Leve2")
#matriz.modificar(12, 3, "Leve2")
#matriz.modificar(1, 1, "Level3")
#matriz.modificar(1, 2, "Level3")
#matriz.modificar(1, 3, "Level3")
#matriz.modificar(6, 5, "Level4")
#matriz.modificar(7, 5, "Level4")
#matriz.modificar(8, 5, "Level4")
#matriz.modificar(9, 5, "Level4")
#matriz.modificar(6, 6, "Level1")
#matriz.modificar(7, 7, "Level1")
#matriz.modificar(9,9, 'X')
#matriz.modificar(1,3, 'X')
#matriz.graficarTablero()


'''       
matriz.insertar(5, 5, "D")
matriz.insertar(6, 5, "D")
matriz.insertar(1, 1, "D")
matriz.insertar(26, 26, "X")
matriz.insertar(7, 5, "B")
matriz.insertar(8, 5, "B")
matriz.insertar(8, 5, "B")
matriz.insertar(8, 1, "B")
matriz.insertar(40, 40, "B")
matriz.insertar(8, 2, "B")
matriz.insertar(8, 3, "A")
matriz.insertar(25, 4, "X")
#matriz.graficarNeato()
matriz.graficarTablero()
'''
