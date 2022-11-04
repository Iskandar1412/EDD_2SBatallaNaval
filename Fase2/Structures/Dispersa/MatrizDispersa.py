import os


class Nodo:
    def __init__(self, x, y, data):
        self.data = data
        self.col = x 
        self.row = y 
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def setUp(self, up):
        self.up = up
    def setDown(self, down):
        self.down = down
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
    def getUp(self):
        return self.up
    def getDown(self):
        return self.down
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

class Nodo_Matriz:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.prev = None
        self.key = None

    def setKey(self, val):
        self.key = val
    def getKey(self):
        return self.key


class Lista():
    def __init__(self, valor):
        self.primero = None
        self.ultimo = None
        self.valor = valor
        self.tamanio = 0

    def insert(self, nuevo : Nodo_Matriz):
        self.tamanio += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            if nuevo.id < self.primero.id:
                nuevo.next = self.primero
                self.primero.prev = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.next = nuevo
                nuevo.prev = self.ultimo
                self.ultimo = nuevo
            else:
                tmp: Nodo_Matriz = self.primero 
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.next = tmp
                        nuevo.prev = tmp.prev
                        tmp.prev.next = nuevo
                        tmp.prev = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp = tmp.next
                    else:
                        break

    def mostrarCabeceras(self):
        tmp = self.primero
        while tmp != None:
            print('Cabecera', self.valor, tmp.id)
            tmp = tmp.next

    def getCabecera(self, id) -> Nodo_Matriz:
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.next
        return None


class MatrizDispersa:
    def __init__(self):
        self.capa = 0
        self.filas = Lista('fila')
        self.columnas = Lista('columna')

    def insertar(self, pos_x, pos_y, data):
        nueva_celda = Nodo(pos_x, pos_y, data) 
        nodo_X = self.filas.getCabecera(pos_x)
        nodo_Y = self.columnas.getCabecera(pos_y)

        if nodo_X == None: 
            nodo_X = Nodo_Matriz(pos_x)
            self.filas.insert(nodo_X)

        if nodo_Y == None: 
            nodo_Y = Nodo_Matriz(pos_y)
            self.columnas.insert(nodo_Y)

        if nodo_X.getKey() == None: 
            nodo_X.setKey(nueva_celda)
        else: 
            if nueva_celda.row < nodo_X.getKey().row:    
                nueva_celda.setRight(nodo_X.getKey())        
                nodo_X.getKey().setLeft(nueva_celda)
                nodo_X.setKey(nueva_celda)
            else:
                tmp : Nodo = nodo_X.getKey() 
                while tmp != None:                      
                    if nueva_celda.row < tmp.row:
                        nueva_celda.setRight(tmp)
                        nueva_celda.setLeft(tmp.getLeft())
                        tmp.getLeft().setRight(nueva_celda)
                        tmp.setLeft(nueva_celda)
                        break
                    elif nueva_celda.col == tmp.col and nueva_celda.row == tmp.row: 
                        break
                    else:
                        if tmp.getRight() == None:
                            tmp.setRight(nueva_celda)
                            nueva_celda.setLeft(tmp)
                            break
                        else:
                            tmp = tmp.getRight() 
                           
        if nodo_Y.getKey() == None: 
            nodo_Y.setKey(nueva_celda)
        else: 
            if nueva_celda.col < nodo_Y.getKey().col:
                nueva_celda.setDown(nodo_Y.getKey())
                nodo_Y.getKey().setUp(nueva_celda)
                nodo_Y.setKey(nueva_celda)
            else:
                tmp2 : Nodo = nodo_Y.getKey()
                while tmp2 != None:
                    if nueva_celda.col < tmp2.col:
                        nueva_celda.setDown(tmp2)
                        nueva_celda.setUp(tmp2.getUp())
                        tmp2.getUp().setDown(nueva_celda)
                        tmp2.setUp(nueva_celda)
                        break
                    elif nueva_celda.col == tmp2.col and nueva_celda.row == tmp2.row: 
                        break
                    else:
                        if tmp2.getDown() == None:
                            tmp2.setDown(nueva_celda)
                            nueva_celda.setUp(tmp2)
                            break
                        else:
                            tmp2 = tmp2.getDown()


    def InsertFil(self, fila):
        inicio : Nodo_Matriz = self.filas.getCabecera(fila)
        if inicio == None:
            print('Esa coordenada de filas no existe')
            return None
            
        tmp : Nodo = inicio.getKey()
        while tmp != None:
            print(tmp.data)
            tmp = tmp.getRight()

    
    def InsertCol(self, columna):
        inicio : Nodo_Matriz = self.columnas.getCabecera(columna)
        if inicio == None:
            print('Esa coordenada de columna no existe')
            return None

        tmp : Nodo = inicio.getKey()
        while tmp != None:
            print(tmp.data)
            tmp = tmp.getDown()


    def search(self, fila, columna):
        try:
            tmp : Nodo = self.filas.getCabecera(fila).getKey()
            while tmp != None:
                if tmp.col == fila and tmp.row == columna:
                    return tmp
                tmp = tmp.getRight()
            return None
        except:
            print('Coordenada no encontrada')
            return None

    def DeleteNode(self, x, y):
        self.columnas

    def GraphTable(self):
        dot = 'digraph G{\nnode[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled];\nedge[style = invis];\nraiz[label = "" fillcolor="#969696" pos = "-1,1!"];\n'
        dot += 'label = "" \nfontname="Arial Black"; \nfontsize="25pt";\n'

        # Fila
        pivote_x = self.filas.primero
        pos_x = 0
        while pivote_x != None:
            dot += '\nx{}[label = "{}" fillcolor="#F58F63" fontcolor="#FFFFFF" pos="{},1!" shape=box];'.format(pivote_x.id, pivote_x.id, pos_x)
            pivote_x = pivote_x.next
            pos_x += 1
        pivote_x = self.filas.primero
        while pivote_x.next != None:
            dot += '\nx{}->x{}[dir=back];'.format(pivote_x.id, pivote_x.next.id)
            pivote_x = pivote_x.next
        dot += '\nraiz->x{};'.format(self.filas.primero.id)

        # Columna
        pivote_y = self.columnas.primero
        pos_y = 0
        while pivote_y != None:
            dot += '\ny{}[label = "{}" fillcolor="#56F18C" fontcolor="#FFFFFF" pos = "-1,-{}!" shape=box];'.format(pivote_y.id, pivote_y.id, pos_y)
            pivote_y = pivote_y.next
            pos_y += 1
        pivote_y = self.columnas.primero
        while pivote_y.next != None:
            dot += '\ny{}->y{}[dir=back];'.format(pivote_y.id, pivote_y.next.id)
            pivote_y = pivote_y.next
        dot += '\nraiz->y{};'.format(self.columnas.primero.id)

        # Nodos
        pivote_x = self.filas.primero
        pos_x = 0
        while pivote_x != None:
            pivote : Nodo = pivote_x.key
            while pivote != None:
                pivote_y = self.columnas.primero
                posy_celda = 0
                while pivote_y != None:
                    if pivote_y.id == pivote.row: break
                    posy_celda += 1
                    pivote_y = pivote_y.next
                #Colores para Buques
                #Buques Ya Destruido
                if pivote.data == '*':
                    dot += '\ni{}_{}[label="*" fillcolor="#4E4D4D" pos="{},-{}!" shape=box];'.format(pivote.col, pivote.row, pos_x, posy_celda)
                #Buque Portaviones
                elif pivote.data == 'Level1':
                    dot += '\ni{}_{}[label="P" fillcolor="#F1700A" pos="{},-{}!" shape=box];'.format(pivote.col, pivote.row, pos_x, posy_celda)
                #Buque Submarino
                elif pivote.data == 'Level2':
                    dot += '\ni{}_{}[label="S" fillcolor="#0DF10A" pos="{},-{}!" shape=box];'.format(pivote.col, pivote.row, pos_x, posy_celda)
                #Buque Destructor
                elif pivote.data == 'Level3':
                    dot += '\ni{}_{}[label="D" fillcolor="#0A92F1" pos="{},-{}!" shape=box];'.format(pivote.col, pivote.row, pos_x, posy_celda)
                #Buque 1
                elif pivote.data == 'Level4':
                    dot += '\ni{}_{}[label="B" fillcolor="#540AF1" pos="{},-{}!" shape=box];'.format(pivote.col, pivote.row, pos_x, posy_celda)
                elif pivote.data == 'Lev':
                    dot += '\ni{}_{}[label=" " fillcolor="#F10A96" pos="{},-{}!" shape=box];'.format( pivote.col, pivote.row, pos_x, posy_celda) 
                pivote = pivote.right
            
            pivote = pivote_x.key
            while pivote != None:
                if pivote.right != None:
                    dot += '\ni{}_{}->i{}_{}[dir=back];'.format(pivote.col, pivote.row,
                    pivote.right.col, pivote.right.row)
                pivote = pivote.right
            dot += '\nx{}->i{}_{}[dir=back];'.format(pivote_x.id, pivote_x.key.col, pivote_x.key.row)
            pivote_x = pivote_x.next
            pos_x += 1
        
        pivote_x = self.columnas.primero
        while pivote_x != None:
            pivote : Nodo = pivote_x.key
            while pivote != None:
                if pivote.down != None:
                    dot += '\ni{}_{}->i{}_{}[dir=back];'.format(pivote.col, pivote.row,pivote.down.col, pivote.down.row) 
                pivote = pivote.down
            dot += '\ny{}->i{}_{}[dir=back];'.format(pivote_x.id, pivote_x.key.col, pivote_x.key.row)
            pivote_x = pivote_x.next
        dot += '\n}'
        print(dot)
        with open("Fase2/Images/Tablero.dot", 'w') as grafo:
            grafo.write(dot)
        os.system("neato -Tpng Fase2/Images/Tablero.dot -o Fase2/Images/Tablero.png")
        
    def Graphos(self):
        dot = 'digraph G{\nnode[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled];\nedge[style = invis];\nraiz[label = "" fillcolor="#969696" pos = "-1,1!"];\n'
        dot += 'label = "" \nfontname="Arial Black"; \nfontsize="25pt";\n'

       
'''     
matriz = MatrizDispersa()
matriz.insertar(5,5,"P")
matriz.insertar(5,6,"P")
matriz.insertar(5,7,"P")
matriz.insertar(5,8,"P")
matriz.insertar(15,20,"S")
matriz.insertar(16,20,"S")
matriz.insertar(17,20,"S")
matriz.insertar(18,20,"D")
matriz.insertar(19,20,"D")
matriz.insertar(7,9,"B")
matriz.insertar(7,10,"B")
matriz.insertar(8,11,"B")#x y val

matriz.GraphTable()
'''