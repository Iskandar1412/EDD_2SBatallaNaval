//Matriz Dispersa
class Nodo_Cabecera {
    constructor(id) {
        this.id = id;
        this.siguiente = null;
        this.anterior = null;
        this.acceso = null;
    }
    
}

class Nodo_Celda {
    constructor(x, y, libro) {
            this.coordenadaX = x;
            this.coordenadaY = y;
            this.libro = libro;
            //this.pila = new Lista_Pila();
            this.arriba = null;
            this.abajo = null;
            this.izquierda = null;
            this.derecha = null;
        }
}

class Lista_Cabecera {
    constructor(tipo) {
        this.primero = null;
        this.ultimo = null;
        this.tipo = tipo;
        this.size = 0;
    }
    
    insertar_nodoCabecera(nuevo) {
        this.size += 1;
        if (this.primero == null) {
            this.primero = nuevo;
            this.ultimo = nuevo;
        } else {
            if (nuevo.id < this.primero.id) {
                nuevo.siguiente = this.primero;
                this.primero.anterior = nuevo;
                this.primero = nuevo;
            } else if (nuevo.id > this.ultimo.id) {
                this.ultimo.siguiente = nuevo;
                nuevo.anterior = this.ultimo;
                this.ultimo = nuevo;
            } else {
                var temporalCabecera = this.primero;
                while (temporalCabecera != null) {
                    if (nuevo.id < temporalCabecera.id) {
                        nuevo.siguiente = temporalCabecera;
                        nuevo.anterior = temporalCabecera.anterior;
                        temporalCabecera.anterior.siguiente = nuevo;
                        temporalCabecera.anterior = nuevo;
                        break;
                    } else if (nuevo.id > temporalCabecera.id) {
                        temporalCabecera = temporalCabecera.siguiente;
                    } else {
                        break;
                    }
                }
            }
        }
    }

    mostrarCabeceras() {
        let tmp = this.primero;
        while (tmp != null) {
            tmp = tmp.siguiente;
        }
    }

    getCabecera(id) {
        var temporalCabecera;
        temporalCabecera = this.primero;
        while (temporalCabecera != null) {
            if (temporalCabecera.id == id) {
                return temporalCabecera;
            }
            temporalCabecera = temporalCabecera.siguiente;
        }
        return null;
    }

}



class Matriz_Dispersa {
    constructor() {
        this.filas = new Lista_Cabecera("fila");
        this.columnas = new Lista_Cabecera("columna");
        this.capa = 0;
    }
    insertar(row, col, libro) {
        var nueva_celda = new Nodo_Celda(row, col, libro);
        var nodo_X = this.filas.getCabecera(row);
        var nodo_Y = this.columnas.getCabecera(col);
        if (nodo_X == null) {
            nodo_X = new Nodo_Cabecera(row);
            this.filas.insertar_nodoCabecera(nodo_X);
        }
        if (nodo_Y == null) {
            nodo_Y = new Nodo_Cabecera(col);
            this.columnas.insertar_nodoCabecera(nodo_Y);
        }
        if (nodo_X.acceso == null) {
            nodo_X.acceso = nueva_celda;
        } else {
            if (nueva_celda.coordenadaY < nodo_X.acceso.coordenadaY) {
                nueva_celda.derecha = nodo_X.acceso;
                nodo_X.acceso.izquierda = nueva_celda;
                nodo_X.acceso = nueva_celda;
            } else {
                var tmp = nodo_X.acceso;
                while (tmp != null) {
                    if (nueva_celda.coordenadaY < tmp.coordenadaY) {
                        nueva_celda.derecha = tmp;
                        nueva_celda.izquierda = tmp.izquierda;
                        tmp.izquierda.derecha = nueva_celda;
                        tmp.izquierda = nueva_celda;
                        break;
                    } else if (nueva_celda.coordenadaX == tmp.coordenadaX && nueva_celda.coordenadaY == tmp.coordenadaY) {
                        break;
                    } else {
                        if (tmp.derecha == null) {
                            tmp.derecha = nueva_celda;
                            nueva_celda.izqueirda = tmp;
                            break;
                        } else {
                            tmp = tmp.derecha;
                        }
                    }
                }
            }
        }
        if (nodo_Y.acceso == null) {
            nodo_Y.acceso = nueva_celda;
        } else {
            if (nueva_celda.coordenadaX < nodo_Y.acceso.coordenadaX) {
                nueva_celda.abajo = nodo_Y.acceso;
                nodo_Y.acceso.arriba = nueva_celda;
                nodo_Y.acceso = nueva_celda;
            } else {
                var tmp2 = nodo_Y.acceso;
                while (tmp2 != null) {
                    if (nueva_celda.coordenadaX < tmp2.coordenadaX) {
                        nueva_celda.abajo = tmp2;
                        nueva_celda.arriba = tmp2.arriba;
                        tmp2.arriba.abajo = nueva_celda;
                        tmp2.arriba = nueva_celda;
                        break;
                    } else if (nueva_celda.coordenadaX == tmp2.coordenadaX && nueva_celda.coordenadaY == tmp2.coordenadaY) {
                        break;
                    } else {
                        if (tmp2.abajo == null) {
                            tmp2.abajo = nueva_celda;
                            nueva_celda.arriba = tmp2;
                            break;
                        } else {
                            tmp2 = tmp2.abajo;
                        }
                    }
                }
            }
        }
    }

    imprimir() {
        var Contador = 0;
        while (Contador <= 25) {
            Contador += 1;
            try {
                var Nodo = this.filas.getCabecera(Contador).acceso;
            } catch (e) {
                console.log("No se ha encontrado el libro aún");
            }
            while (Nodo != null) {
                console.log("X: " + Nodo.coordenadaX + " Y: " + Nodo.coordenadaY + " Libro: " + Nodo.pila);
                console.log(Nodo.pila.contar());
                Nodo = Nodo.derecha;
            }

        }
    }

    modificar(fila, columna, libro) {
        var Nodo = this.filas.getCabecera(fila).acceso;
        while (Nodo != null) {
            if (Nodo.coordenadaX == fila && Nodo.coordenadaY == columna) {
                Nodo.libro = libro;
                break;
            }
            Nodo = Nodo.derecha;
        }
    }

    graficarNeato() {
        var contenido = "digraph G{\n";
        contenido += 'layout = neato;\nbgcolor="none";\n';
        contenido += 'ranksep=2;\nnodesep=2;\n'
        contenido += 'node[shape=box, width=0.5, height=0.5, fontname="Arial", fillcolor="white", style=filled];\n' +
            'edge[dir="both", color="red"];\n' +
            "node[label = \"" + " " + '"  fillcolor="black" pos = "-1,1!"]raiz;\n';
        contenido += 'label = "TABLERO";\nfontname="Arial Black" \nfontsize="25pt" \n';


        var pivote = this.filas.primero;
        var posx = 0;
        while (pivote != null) {
            contenido += '\n\ty' + pivote.id + '[label = "' + pivote.id + '"  fillcolor="black" fontcolor="white" pos="-1,-' + posx + '!"];';
            pivote = pivote.siguiente;
            posx += 1;
        }
        pivote = this.filas.primero;
        while (pivote.siguiente != null) {
            //contenido += '\n\tx' + pivote.id + '->x' + pivote.siguiente.id + ';';
            contenido += '\n\ty' + pivote.id + '->y' + pivote.siguiente.id + ';';
            pivote = pivote.siguiente;
        }
        contenido += '\n\traiz->y' + this.filas.primero.id + ';';

        var pivotey = this.columnas.primero;
        var posy = 0;

        while (pivotey != null) {
            contenido += '\n\tx' + pivotey.id + '[label="' + pivotey.id + '" fillcolor="black" fontcolor="white" pos="' + posy + ',1!"];';
            pivotey = pivotey.siguiente;
            posy += 1;
        }
        pivotey = this.columnas.primero;
        while (pivotey.siguiente != null) {
            //contenido += '\n\ty' + pivotey.id + '->y' + pivotey.siguiente.id + ';';
            contenido += '\n\tx' + pivotey.id + '->x' + pivotey.siguiente.id + ';';
            pivotey = pivotey.siguiente;
        }
        contenido += '\n\traiz->x' + this.columnas.primero.id + ';';

        var pivote = this.filas.primero;
        var posx = 0;

        while (pivote != null) {
            var pivote_celda = pivote.acceso;
            while (pivote_celda != null) {
                var pivotey = this.columnas.primero;
                var posy_celda = 0;
                while (pivotey != null) {
                    if (pivotey.id == pivote_celda.coordenadaY) {
                        break;
                    }
                    posy_celda += 1;
                    pivotey = pivotey.siguiente;
                }
                contenido += '\n\ti' + pivote_celda.coordenadaX + '_' + pivote_celda.coordenadaY + '[label="' + pivote_celda.libro + '" fillcolor="gray" color="white" pos="' + posy_celda + ',-' + posx + '!"];';
                pivote_celda = pivote_celda.derecha;
            }
            pivote_celda = pivote.acceso;
            while (pivote_celda != null) {
                if (pivote_celda.derecha != null) {
                    //contenido += '\n\ti' + pivote_celda.coordenadaX + '_' + pivote_celda.coordenadaY + '->i' + pivote_celda.derecha.coordenadaX + '_' + pivote_celda.derecha.coordenadaY + ';';
                    contenido += '\n\ti' + pivote_celda.coordenadaX + '_' + pivote_celda.coordenadaY + '->i' + pivote_celda.derecha.coordenadaX + '_' + pivote_celda.derecha.coordenadaY + ';';
                }
                pivote_celda = pivote_celda.derecha
            }
            //contenido += '\n\tx' + pivote.id + '->i' + pivote.acceso.coordenadaX + '_' + pivote.acceso.coordenadaY + ';';
            contenido += '\n\ty' + pivote.id + '->i' + pivote.acceso.coordenadaX + '_' + pivote.acceso.coordenadaY + ';';
            pivote = pivote.siguiente;
            posx += 1;
        }







        pivote = this.columnas.primero;
        while (pivote != null) {
            var pivote_celda = pivote.acceso;
            while (pivote_celda != null) {
                if (pivote_celda.abajo != null) {
                    //contenido += '\n\ti' + pivote_celda.coordenadaX + '_' + pivote_celda.coordenadaY + '->i' + pivote_celda.abajo.coordenadaX + '_' + pivote_celda.abajo.coordenadaY + ';';
                    contenido += '\n\ti' + pivote_celda.coordenadaX + '_' + pivote_celda.coordenadaY + '->i' + pivote_celda.abajo.coordenadaX + '_' + pivote_celda.abajo.coordenadaY + ';';
                }
                pivote_celda = pivote_celda.abajo
            }
            //contenido += '\n\ty' + pivote.id + '->i' + pivote.acceso.coordenadaX + '_' + pivote.acceso.coordenadaY + ';';
            contenido += '\n\tx' + pivote.id + '->i' + pivote.acceso.coordenadaX + '_' + pivote.acceso.coordenadaY + ';';
            pivote = pivote.siguiente;
        }
        contenido += '\n}';
        console.log(contenido)
        return contenido;

    }
}

let matriz = new Matriz_Dispersa()

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
matriz.graficarNeato()
matriz.modificar(40, 40, "XA")
matriz.graficarNeato()