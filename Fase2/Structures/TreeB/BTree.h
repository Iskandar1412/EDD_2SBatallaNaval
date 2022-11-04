#include <stddef.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>


using namespace std;

class Usuario_ABB{
    public:
        int id;
        string nick;
        string password;
        int monedas;
        int edad;
        Usuario_ABB(int,string,string,int,int);
        Usuario_ABB() = default;
};

Usuario_ABB::Usuario_ABB(int _id, string _nick, string _password, int _monedas, int _edad){
            id = _id;
            nick = _nick;
            password = _password;
            monedas = _monedas;
            edad = _edad;
}

class Nodo_AB {
    public:
        Usuario_ABB Usuario_ABB;
        Nodo_AB* siguiente;
        Nodo_AB* anterior;

        Nodo_AB* derecha;
        Nodo_AB* izquierda;

        Nodo_AB(Usuario_ABB _usuario) {
            Usuario_ABB = _usuario;
            siguiente = NULL;
            anterior = NULL;
            derecha = NULL;
            izquierda = NULL;
        }
};

class ArbolB {
public:
    int orden_arbol = 4;
    Nodo_AB* raiz;
    ArbolB() {
        raiz = NULL;
    }
    void add(Usuario_ABB Usuario_ABB){
        Nodo_AB* nodo = new Nodo_AB(Usuario_ABB);
        if (raiz == NULL) {
            raiz = nodo;
        } else {
            pair < Nodo_AB*, pair<bool, bool>> ret = Creacion_rama(nodo, raiz);
            Nodo_AB* obj = ret.first;
            if ((ret.second.first || ret.second.second) && obj != NULL) {//si se divide la rama o se inserta al inicio, la raiz cambia
                
                raiz = obj;
            }
        }
    }
    pair<Nodo_AB*, pair<bool, bool>> Creacion_rama(Nodo_AB* nodo, Nodo_AB* rama){
        pair < Nodo_AB*, pair<bool, bool>> ResultadoRama;
        ResultadoRama.first = NULL; 
        ResultadoRama.second.first = false; 
        ResultadoRama.second.second = false; 
        if (Es_Hoja(rama)) {
            pair < Nodo_AB*, bool> resultado = Insertar_en_Rama(rama, nodo); 
            ResultadoRama.first = resultado.first; 
            ResultadoRama.second.second = resultado.second; 
            if (Graph(resultado.first) == orden_arbol) {
                ResultadoRama.first = dividir(resultado.first); 
                ResultadoRama.second.first = true; 
            }
        } else {
            Nodo_AB*temp = rama;
            do {
                if (nodo->Usuario_ABB.id == temp->Usuario_ABB.id) {
                    return ResultadoRama;
                } else if (nodo->Usuario_ABB.id < temp->Usuario_ABB.id) {
                    pair < Nodo_AB*, pair<bool, bool>> ResultadoInsert = Creacion_rama(nodo, temp->izquierda);
                    if (ResultadoInsert.second.second && ResultadoInsert.first != NULL) {
                        ResultadoRama.second.second = true;
                        temp->izquierda = ResultadoInsert.first;
                    }
                    if (ResultadoInsert.second.first) {
                        pair < Nodo_AB*, bool> auxInsert = Insertar_en_Rama(rama, ResultadoInsert.first);
                        rama = auxInsert.first;
                        if (auxInsert.second) {
                            ResultadoRama.first = rama;
                        }
                        if (Graph(rama) == orden_arbol) {
                            ResultadoRama.first = dividir(rama);
                            ResultadoRama.second.first = true;
                        }
                    }
                    return ResultadoRama;
                } else if (temp->siguiente == NULL) {
                    pair < Nodo_AB*, pair<bool, bool>> ResultadoInsert = Creacion_rama(nodo, temp->derecha);
                    if (ResultadoInsert.second.second && ResultadoInsert.first != NULL) {
                        ResultadoRama.second.second = true;
                        temp->derecha = ResultadoInsert.first;
                    }
                    if (ResultadoInsert.second.first) {
                        pair < Nodo_AB*, bool> auxInsert = Insertar_en_Rama(rama, ResultadoInsert.first);
                        rama = auxInsert.first;
                        if (auxInsert.second) {
                            ResultadoRama.first = rama;
                        }
                        if (Graph(rama) == orden_arbol) {
                            ResultadoRama.first = dividir(rama);
                            ResultadoRama.second.first = true;
                        }
                    }
                    return ResultadoRama;
                }
                temp = temp->siguiente;
            } while (temp != NULL);
        }
        return ResultadoRama;
    }
    Nodo_AB* dividir(Nodo_AB* rama){
        Usuario_ABB val = Usuario_ABB(0,"","",-1,-1);
        Nodo_AB*temp = NULL;
        Nodo_AB*Nuevito = NULL;
        Nodo_AB*aux = rama;

        Nodo_AB*rderecha = NULL;
        Nodo_AB*rizquierda = NULL;

        int cont = 0;
        while (aux != NULL) {
            cont++;
            if (cont < 3) {
                val = Usuario_ABB(aux->Usuario_ABB.id, aux->Usuario_ABB.nick, aux->Usuario_ABB.password, aux->Usuario_ABB.monedas, aux->Usuario_ABB.edad);
                temp = new Nodo_AB(val);
                temp->izquierda = aux->izquierda;
                if (cont == 2) {
                    temp->derecha = aux->siguiente->izquierda;
                } else {
                    temp->derecha = aux->derecha;
                }
                rizquierda = Insertar_en_Rama(rizquierda, temp).first;
            } else if (cont == 3) {
                val = Usuario_ABB(aux->Usuario_ABB.id, aux->Usuario_ABB.nick, aux->Usuario_ABB.password, aux->Usuario_ABB.monedas, aux->Usuario_ABB.edad);
                Nuevito = new Nodo_AB(val);
            } else {
                val = Usuario_ABB(aux->Usuario_ABB.id, aux->Usuario_ABB.nick, aux->Usuario_ABB.password, aux->Usuario_ABB.monedas, aux->Usuario_ABB.edad);;
                temp = new Nodo_AB(val);
                temp->izquierda = aux->izquierda;
                temp->derecha = aux->derecha;
                rderecha = Insertar_en_Rama(rderecha, temp).first;
            }
            aux = aux->siguiente;
        }
        Nuevito->derecha = rderecha;
        Nuevito->izquierda = rizquierda;
        return Nuevito;
    }
    pair<Nodo_AB*, bool>  Insertar_en_Rama(Nodo_AB* primero, Nodo_AB* nuevo){
        pair < Nodo_AB*, bool> ret;
        ret.second = false;
        if (primero == NULL) {
            ret.second = true;
            primero = nuevo;
        } else {
            Nodo_AB* aux = primero;
            while (aux != NULL) {
                if (aux->Usuario_ABB.id == nuevo->Usuario_ABB.id) {
                    break;
                } else {
                    if (aux->Usuario_ABB.id > nuevo->Usuario_ABB.id) {
                        if (aux == primero) {
                            aux->anterior = nuevo;
                            nuevo->siguiente = aux;
                            aux->izquierda = nuevo->derecha;
                            nuevo->derecha = NULL;
                            ret.second = true;
                            primero = nuevo;
                            break;
                        } else {
                            nuevo->siguiente = aux;
                            aux->izquierda = nuevo->derecha;
                            nuevo->derecha = NULL;

                            nuevo->anterior = aux->anterior;
                            aux->anterior->siguiente = nuevo;
                            aux->anterior = nuevo;
                            break;
                        }
                    } else if (aux->siguiente == NULL) {
                        aux->siguiente = nuevo;
                        nuevo->anterior = aux;
                        break;
                    }
                }
                aux = aux->siguiente;
            }

        }
        ret.first = primero;

        return ret;
    }
    bool Es_Hoja(Nodo_AB* primero){
        Nodo_AB* aux = primero;
        while (aux != NULL) {
            //cout << "[" << aux->Usuario_ABB.id << "]->";
            if (aux->izquierda != NULL || aux->derecha != NULL) {
                return false;
            }
            aux = aux->siguiente;
        }
        //cout << "Null\n";
        return true;
    }
    int Graph(Nodo_AB* primero){
        int Graph = 0;
        Nodo_AB* aux = primero;
        while (aux != NULL) {
            Graph++;
            aux = aux->siguiente;
        }
        return Graph;
    }
    void Grafo(){
        string dotFull = "";

        dotFull += "digraph G {\n";
        dotFull += "node[shape=record]\n";
        dotFull += "//Agregar Nodos Rama\n";
        dotFull += B_Graph(raiz);
        dotFull += "//Agregar conexiones\n";
        dotFull += Conect_Branches(raiz);

        dotFull += "}";
        ofstream file;
        file.open("Arbol_Usuarios.dot");
        file << dotFull;
        file.close();

        system(("dot -Tsvg Arbol_Usuarios.dot -o  Images/Arbol_Usuarios.svg"));


    }
    string B_Graph(Nodo_AB*rama){
        string dot = "";
        if (rama != NULL) {
            dot += Graph_Branches(rama);
            Nodo_AB*aux = rama;
            while (aux != NULL) {
                if (aux->izquierda != NULL) {
                    dot += B_Graph(aux->izquierda);
                }
                if (aux->siguiente == NULL) {
                    if (aux->derecha != NULL) {
                        dot += B_Graph(aux->derecha);
                    }
                }
                aux = aux->siguiente;
            }
        }
        return dot;
    }
    string Graph_Branches(Nodo_AB*rama){
            string dot = "";
            stringstream auxiliar;
            if (rama != NULL) {
                Nodo_AB*aux = rama;
                auxiliar.str("");
                auxiliar << rama;
                dot = dot + "R" + auxiliar.str() + "[label=\"";
                int r = 1;
                while (aux != NULL) {
                    if (aux->izquierda != NULL) {
                        dot = dot + "<C" + to_string(r) + ">|";
                        r++;
                    }
                    if (aux->siguiente != NULL) {
                        dot = dot + "ID: " + to_string(aux->Usuario_ABB.id) + "\\nUsr: " + aux->Usuario_ABB.nick + "\\nPass: " +aux->Usuario_ABB.password + "\\nMon: " + to_string(aux->Usuario_ABB.monedas) + "\\nYears: " + to_string(aux->Usuario_ABB.edad) +"|";
                        
                    } else {
                        dot = dot + "ID: " + to_string(aux->Usuario_ABB.id) + "\\nUsr: " + aux->Usuario_ABB.nick + "\\nPass: " +aux->Usuario_ABB.password + "\\nMon: " + to_string(aux->Usuario_ABB.monedas) + "\\nYears: " + to_string(aux->Usuario_ABB.edad);
                        if (aux->derecha != NULL) {
                            dot = dot + "|<C" + to_string(r) + ">";
                        }
                    }
                    aux = aux->siguiente;
                }
                dot = dot + "\"];\n";
            }
            return dot;
        }
        string Conect_Branches(Nodo_AB*rama){
            string dot = "";
            stringstream auxiliar;
            if (rama != NULL) {
                Nodo_AB*aux = rama;
                auxiliar << rama;
                string actual = "R" + auxiliar.str();
                int r = 1;
                while (aux != NULL) {
                    if (aux->izquierda != NULL) {
                        auxiliar.str("");
                        auxiliar << aux->izquierda;
                        dot += actual + ":C" + to_string(r) + "->" + "R" + auxiliar.str() + ";\n";
                        r++;
                        dot += Conect_Branches(aux->izquierda);
                    }
                    if (aux->siguiente == NULL) {
                        if (aux->derecha != NULL) {
                            auxiliar.str("");
                            auxiliar << aux->derecha;
                            dot += actual + ":C" + to_string(r) + "->" + "R" + auxiliar.str() + ";\n";
                            r++;
                            dot += Conect_Branches(aux->derecha);
                        }
                    }
                    aux = aux->siguiente;
                }
            }
            return dot;
        }
        void Eliminar(Usuario_ABB Usuario_ABB);

    };

//Creacion Arbol


