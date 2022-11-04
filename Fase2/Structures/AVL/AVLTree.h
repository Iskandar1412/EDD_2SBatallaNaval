#include <fstream>
#include <stddef.h>
#include <iostream>
#include <iomanip>


//incluir string
//#include ".././TreeB/BTree.h"
#include "../../Funciones/sha256.h"
//PARA INTERACTUAR CON LA ARBOL AVL DobleLUSR
//PARA INTERACTUAR CON B TreeB

using namespace std;

//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------


class NodoB_B{
    public:
        int id;
        string nick;
        string password;
        int monedas;
        int edad;
        NodoB_B* siguiente;
        NodoB_B* anterior;
        NodoB_B* derecha;
        NodoB_B* izquierda;
        NodoB_B(int id, string nick, string password, int edad, int monedas){
            this->id = id;
            this->nick = nick;
            this->password = password;
            this->monedas = monedas;
            this->edad = edad;
            this->siguiente = NULL;
            this->anterior = NULL;
            this->derecha = NULL;
            this->izquierda = NULL;
        }
};

class TreeB{
    public:
        int orden_arbol = 4;
        NodoB_B* raiz;
        TreeB(){
            this->raiz = NULL;
        }

        void add(int id, string nick, string password, int edad, int monedas){
            NodoB_B* temp = new NodoB_B(id, nick, password, edad, monedas);
            if(this->raiz == NULL){
                this->raiz = temp;
            }else{
                pair<NodoB_B*, pair<bool,bool>>ret = Creacion_rama(temp, raiz);
                NodoB_B* aux = ret.first;
                if((ret.second.first || ret.second.second) && aux != NULL){
                    this->raiz = aux;
                }
            }
        }

        pair<NodoB_B*, pair<bool, bool>>Creacion_rama(NodoB_B* nodo, NodoB_B* rama){
            pair<NodoB_B*, pair<bool, bool>>ResultadoRama;
            ResultadoRama.first = NULL;
            ResultadoRama.second.first = false;
            ResultadoRama.second.second = false;
            if(Es_Hoja(rama)){
                pair<NodoB_B*, bool>resultado = Insertar_en_Rama(rama, nodo);
                ResultadoRama.first = resultado.first;
                ResultadoRama.second.second = resultado.second;
                if(Graph(resultado.first) == orden_arbol){
                    ResultadoRama.first = dividir(resultado.first);
                    ResultadoRama.second.first = true;
                }
            }else{
                NodoB_B* temp = rama;
                do{
                    if(nodo->id == temp->id){
                        return ResultadoRama;
                    }else if(nodo->id < temp->id){
                        pair<NodoB_B*, pair<bool, bool>>ResultadoInsert = Creacion_rama(nodo, temp->izquierda);
                        if(ResultadoInsert.second.second && ResultadoInsert.first != NULL){
                            ResultadoRama.second.second = true;
                            temp->izquierda = ResultadoInsert.first;
                        }
                        if(ResultadoInsert.second.first){
                            pair<NodoB_B*, bool>auxInsert = Insertar_en_Rama(rama, ResultadoInsert.first);
                            rama = auxInsert.first;
                            if(auxInsert.second){
                                ResultadoInsert.first = rama;
                            }
                            if(Graph(rama) == orden_arbol){
                                ResultadoRama.first = dividir(rama);
                                ResultadoRama.second.first = true;
                            }
                        }
                        return ResultadoRama;
                    }else if(temp->siguiente == NULL){
                        pair<NodoB_B*, pair<bool, bool>>ResultadoInsert = Creacion_rama(nodo, temp->derecha);
                        if(ResultadoInsert.second.second && ResultadoInsert.first != NULL){
                            ResultadoRama.second.second = true;
                            temp->derecha = ResultadoInsert.first;
                        }
                        if(ResultadoInsert.second.first){
                            pair<NodoB_B*, bool>auxInsert = Insertar_en_Rama(rama, ResultadoInsert.first);
                            rama = auxInsert.first;
                            if(auxInsert.second){
                                ResultadoRama.first = rama;
                            }
                            if(Graph(rama) == orden_arbol){
                                ResultadoRama.first = dividir(rama);
                                ResultadoRama.second.first = true;
                            }
                        }
                        return ResultadoRama;
                    }
                    temp = temp->siguiente;
                }while(temp != NULL);
            }
            return ResultadoRama;
        }

        NodoB_B* dividir(NodoB_B* rama){
            NodoB_B* temp = NULL;
            NodoB_B* nuevito = NULL;
            NodoB_B* aux = rama;
            NodoB_B* rderecha = NULL;
            NodoB_B* rizquierda = NULL;

            int cont = 0;
            while(aux != NULL){
                cont++;
                if(cont < 3){
                    temp = new NodoB_B(aux->id, aux->nick, aux->password, aux->edad, aux->monedas);
                    temp->izquierda = aux->izquierda;
                    if(cont == 2){
                        temp->derecha = aux->siguiente->izquierda;
                    }else{
                        temp->derecha = aux->derecha;
                    }
                    rizquierda = Insertar_en_Rama(rizquierda, temp).first;
                }else if(cont == 3){
                    nuevito = new NodoB_B(aux->id, aux->nick, aux->password, aux->edad, aux->monedas);
                }else{
                    temp = new NodoB_B(aux->id, aux->nick, aux->password, aux->edad, aux->monedas);
                    temp->izquierda = aux->izquierda;
                    temp->derecha = aux->derecha;
                    rderecha = Insertar_en_Rama(rderecha, temp).first;
                }
                aux = aux->siguiente;
            }
            nuevito->derecha = rderecha;
            nuevito->izquierda = rizquierda;
            return nuevito;
        }

        pair<NodoB_B*, bool>Insertar_en_Rama(NodoB_B* primero, NodoB_B* final){
            pair<NodoB_B*, bool>ret;
            ret.second = false;
            if(primero == NULL){
                ret.second = true;
                primero = final;
            }else{
                NodoB_B* temp = primero;
                while(temp != NULL){
                    if(temp->id == final->id){
                        break;
                    }else{
                        if(temp->id > final->id){
                            if(temp == primero){
                                temp->anterior = final;
                                final->siguiente = temp;
                                temp->izquierda = final->derecha;
                                final->derecha = NULL;
                                ret.second = true;
                                primero = final;
                                break;
                            }else{
                                final->siguiente = temp;
                                temp->izquierda = final->derecha;
                                final->derecha = NULL;
                                final->anterior = temp->anterior;
                                temp->anterior->siguiente = final;
                                temp->anterior = final;
                                break;
                            }
                        }else if(temp->siguiente == NULL){
                            temp->siguiente = final;
                            final->anterior = temp;
                            break;
                        }
                    }
                    temp = temp->siguiente;
                }
            }
            ret.first = primero;
            return ret;
        }

        bool Es_Hoja(NodoB_B* primero){
            NodoB_B* temp = primero;
            while(temp != NULL){
                if(temp->izquierda != NULL || temp->derecha != NULL){
                    return false;
                }
                temp = temp->siguiente;
            }
            return true;
        }

        int Graph(NodoB_B* primero){
            int valor = 0;
            NodoB_B* temp = primero;
            while(temp != NULL){
                valor++;
                temp = temp->siguiente;
            }
            return valor;
        }

        string Grapho_Ramas(NodoB_B* nodo){
            string dot = "";
            if(nodo != NULL){
                dot = dot + Grapho_Raices(nodo);
                NodoB_B* temp = nodo;
                while(temp != NULL){
                    if(temp->izquierda != NULL){
                        dot = dot + Grapho_Ramas(temp->izquierda);
                    }
                    if(temp->siguiente == NULL){
                        if(temp->derecha != NULL){
                            dot = dot + Grapho_Ramas(temp->derecha);
                        }
                    }
                    temp = temp->siguiente;
                }
            }
            return dot;
        }

        string Grapho_Raices(NodoB_B* nodo){
            string dot = "";
            stringstream auxiliar;
            if(nodo != NULL){
                NodoB_B* temp = nodo;
                auxiliar.str("");
                auxiliar<<nodo;
                dot = dot + "R" + auxiliar.str() + "[label=\"";
                int val = 1;
                while(temp != NULL){
                    if(temp->izquierda != NULL){
                        dot = dot + "<C" + to_string(val) + ">|";
                        val++;
                    }
                    if(temp->siguiente != NULL){
                        dot += "ID: " + to_string(temp->id) + "\\nUsr: " + temp->nick + "\\nPass: " + temp->password + "\\nEdad: " + to_string(temp->edad) + "\\nMonedas: " + to_string(temp->monedas) + "|";
                    }else{
                        dot += "ID: " + to_string(temp->id) + "\\nUsr: " + temp->nick + "\\nPass: " + temp->password + "\\nEdad: " + to_string(temp->edad) + "\\nMonedas: " + to_string(temp->monedas);
                        if(temp->derecha != NULL){
                            dot = dot + "|<C" + to_string(val) + ">";
                        }
                    }
                    temp = temp->siguiente;
                }
                dot = dot + "\"];\n";
            }
            return dot;
        }

        string Raices(NodoB_B* nodo){
            string dot = "";
            stringstream aux;
            if(nodo != NULL){
                NodoB_B* temp = nodo;
                aux<<nodo;
                string temporal = "R" + aux.str();
                int val = 1;
                while(temp != NULL){
                    if(temp->izquierda != NULL){
                        aux.str("");
                        aux<<temp->izquierda;
                        dot += temporal + ":C" + to_string(val) + "->R" + aux.str() + "[color=red];\n";
                        val++;
                        dot = dot + Raices(temp->izquierda);
                    }
                    if(temp->siguiente == NULL){
                        if(temp->derecha != NULL){
                            aux.str("");
                            aux<<temp->derecha;
                            dot = dot + temporal + ":C" + to_string(val) + "->R" + aux.str() + "[color=red];\n";
                            val++;
                            dot = dot + Raices(temp->derecha);
                        }
                    }
                    temp = temp->siguiente;
                }
            }
            return dot;
        }

        void Graficar(){
            string dot = "digraph G{\nnode[shape=record, color=blue];\n";
            dot = dot + Grapho_Ramas(raiz);
            dot = dot + Raices(raiz);
            dot = dot + "}";
            ofstream file;
            file.open("Arbol_Usuarios.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg Arbol_Usuarios.dot -o  Arbol_Usuarios.svg"));

        }

};








//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------
//-------AAHORA A VER SI FUNCIONA LA COSA B-------

//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v



class Compra{
    public:
        int ID_Compra;
        string nombre;
        int cantidad;
        Compra(int,string,int);
        Compra() = default;
};

Compra::Compra(int _idCompra, string _nombre, int _cantidad){
    ID_Compra = _idCompra;
    nombre = _nombre;
    cantidad = _cantidad; 
}


int correlativo = 1;
class NodoAVL{
    public:
    
        Compra compra;
        int id;
        int altura;
        
        NodoAVL* izquierda;
        NodoAVL* derecha;

        NodoAVL(Compra _compra) {
            compra = _compra;
            izquierda = NULL;
            derecha = NULL;
            altura = 0;
            id = correlativo++;
        }
};

class AVLTree {
    public:
        NodoAVL* raiz;

        AVLTree() {
            raiz = NULL;
        }

        int Val_Max(int valor_minimo, int valor_maximo){
            if(valor_minimo > valor_maximo){
                return valor_minimo;
            }else{
                return valor_maximo;
            }
        }
        int altura(NodoAVL* nodo){
            if(nodo == NULL){
                return -1;
            }else{
                return nodo->altura;
            }
        }
        void add(Compra compra){
            raiz = agregar_val(compra, raiz);
        }
        NodoAVL* agregar_val(Compra compra, NodoAVL* nodo){
            if(nodo == NULL){
                return new NodoAVL(compra);
            }else{
                if(compra.ID_Compra < nodo->compra.ID_Compra){
                    nodo->izquierda = agregar_val(compra, nodo->izquierda);
                    if(altura(nodo->derecha)-altura(nodo->izquierda)== -2){
                        if(compra.ID_Compra < nodo->izquierda->compra.ID_Compra){
                            nodo = rotar_izquierda(nodo);
                        }else{
                            nodo = rotar_izquierda_d(nodo);
                        }
                    }
                }else if(compra.ID_Compra > nodo->compra.ID_Compra){
                    nodo->derecha = agregar_val(compra, nodo->derecha);
                    if(altura(nodo->derecha)-altura(nodo->izquierda)== 2){
                        if(compra.ID_Compra > nodo->derecha->compra.ID_Compra){
                            nodo = rotar_derecha(nodo);
                        }else{
                            nodo = rotar_derecha_d(nodo);
                        }
                    }
                }else{
                    //cout << "No se puede agregar";
                }
            }
            nodo->altura = Val_Max(altura(nodo->izquierda),altura(nodo->derecha))+1;
            return nodo;
        }
        NodoAVL* rotar_izquierda(NodoAVL* nodo){
            NodoAVL* aux = nodo->izquierda;
            nodo->izquierda = aux->derecha;
            aux->derecha = nodo;
            //aux->izquierda = nodo;
            nodo->altura = Val_Max(altura(nodo->derecha),altura(nodo->izquierda))+1;
            aux->altura = Val_Max(altura(nodo->izquierda), nodo->altura)+1;
            return aux;
        }
        NodoAVL* rotar_derecha(NodoAVL* nodo){
            NodoAVL* aux = nodo->derecha;
            nodo->derecha = aux->izquierda;
            aux->izquierda = nodo;

            nodo->altura = Val_Max(altura(nodo->derecha),altura(nodo->izquierda))+1;
            aux->altura = Val_Max(altura(nodo->derecha), nodo->altura)+1;
            return aux;
        }
        NodoAVL* rotar_derecha_d(NodoAVL* nodo){
            nodo->derecha = rotar_izquierda(nodo->derecha);
            return rotar_derecha(nodo);
        }
        NodoAVL* rotar_izquierda_d(NodoAVL* nodo){
            nodo->izquierda = rotar_derecha(nodo->izquierda);
            return rotar_izquierda(nodo);
        }

        void GraphCU(string nombre){
            string dot = "";
            dot += "digraph G{label = \"Compras "+nombre+"\" fontname=\"Arial Black\" fontsize=\"15pt\";\nnode [shape = diamond, style=filled, fillcolor=black, fontcolor=white];\n" + Ramas_dot(raiz) + "\n}"; 
            ofstream file;
            file.open("Compras.dot");
            file << dot;
            file.close();
            system(("dot -Tsvg Compras.dot -o Compras.svg"));
        }

        

        string Ramas_dot(NodoAVL* nodo){
            string dot = "";
        
            if((nodo->izquierda == NULL) && (nodo->derecha == NULL)){
                dot += "N" + std::to_string(nodo->id)+ "[label = \"ID: "+ to_string(nodo->compra.ID_Compra) +"\\nNombre: "+ nodo->compra.nombre +"\\nCantidad: "+ to_string(nodo->compra.cantidad)+"\"];\n";
            }else{
                dot += "N" +std::to_string(nodo->id)+"[label = \"ID: "+  to_string(nodo->compra.ID_Compra) +"\\nNombre: "+ nodo->compra.nombre +"\\nCantidad: "+ to_string(nodo->compra.cantidad)+"\"];\n";
            }
            if(nodo->izquierda != NULL){
                dot += Ramas_dot(nodo->izquierda) +"N"+std::to_string(nodo->id) + ":C0->N" + std::to_string(nodo->izquierda->id)+"\n";
            }
            if(nodo->derecha != NULL){
                dot += Ramas_dot(nodo->derecha)+"N"+std::to_string(nodo->id)+":C1->N"+std::to_string(nodo->derecha->id)+"\n";                    
            }
            return dot;
        }
};
  
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v
//Ahora VER SI AGARRA LA LISTA LA LISTA DE COMPRAS :v

//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO

class DobleLinkUSR{
    public:
        //
        SHA256* sha;
        string nick;
        int id;
        string password;
        int edad;
        int monedas;
        int cantidad_jugadas;
        string encrypt;
        DobleLinkUSR* siguiente;
        DobleLinkUSR* anterior;
        AVLTree* ArbolAVL;
        DobleLinkUSR(int id, string nick, string password, int edad, int monedas){
            this->id = id;
            this->nick = nick;
            this->password = password;
            this->edad = edad;
            this->monedas = monedas;
            this->cantidad_jugadas = 0;
            this->ArbolAVL = new AVLTree();
            this->encrypt = sha->cifrar(password);
            this->siguiente = NULL;
            this->anterior = NULL;
        }
};

class DobleLUSR{//LISTA
    public:
        //
        //int valor;
        int contadorB;
        int contador_regresos;
        DobleLinkUSR* cabeza;
        DobleLinkUSR* final;

        bool secionIniciada;
        DobleLinkUSR* usuario_act;
        TreeB* arbolB;
        TreeB* arbolB2;
        TreeB* arbolB3;
        TreeB* arbolB4;
        TreeB* arbolB5;
        TreeB* arbolB6;
        DobleLUSR(){
            //this->valor = 0;
            this->contadorB = 0;
            this->contador_regresos = 0;
            this->cabeza = NULL;
            this->final = NULL;
            this->usuario_act = NULL;

            this->secionIniciada = false;
            this->arbolB = new TreeB();
            this->arbolB2 = new TreeB();
            this->arbolB3 = new TreeB();
            this->arbolB4 = new TreeB();
            this->arbolB5 = new TreeB();
            this->arbolB6 = new TreeB();
        }

        void add(int id, string nombre, string password, int edad, int monedas){
            //nodo->id = this->valor++;
            if(this->cabeza == NULL){
                DobleLinkUSR* nodo = new DobleLinkUSR(id, nombre, password, edad, monedas);
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                bool poderono = false;
                DobleLinkUSR* temp = cabeza;
                while(temp  != NULL){
                    if(temp->id == id){
                        cout<<"ID Existente :v"<<endl;
                        poderono = false;
                        break;
                    }else{
                        poderono = true;
                    }
                    temp = temp->siguiente;
                }
                if(poderono == true){
                    DobleLinkUSR* nodo = new DobleLinkUSR(id, nombre, password, edad, monedas);
                    this->final->siguiente = nodo;
                    nodo->anterior = this->final;
                    this->final = nodo;
                }
                return;
            }
        }

        void AgregarCompra(int id, string nombre, int cantidad, int precio){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->ArbolAVL->add(Compra(id, nombre, cantidad));
            }
        }

        void RestandoMonedas(int precio, int cantidad){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas - (cantidad*precio);
            }
        }

        void RestarPorRetroceso(){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas - 5;
            }
        }

        void RestarPorAbandonar(){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas - 20;
                
            }
        }

        void ModificarMonedas(){
            if(this->usuario_act == NULL){
                return;
            }else{
                DobleLinkUSR* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == usuario_act->nick && temp->password == usuario_act->password && temp->id == usuario_act->id){
                        temp->monedas = usuario_act->monedas;
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void aumentarPartidasJugadas(){
            if(this->usuario_act == NULL){
                return;
            }else{
                DobleLinkUSR* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == usuario_act->nick && temp->password == usuario_act->password && temp->id == usuario_act->id){
                        //usuario_act->cantidad_jugadas = usuario_act->cantidad_jugadas + 1;
                        temp->cantidad_jugadas = temp->cantidad_jugadas + 1;
                    }
                    temp = temp->siguiente;
                }
            }
        }

        int obtenercantidadjugadas(){
            int cantidad;
            if(this->usuario_act == NULL){
                cout<<endl;
            }else{
                cantidad = usuario_act->cantidad_jugadas;
            }
            return cantidad;
        }

        void GanarPorHundir(){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas + 20;
            }
        }

        void Display(){
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }else{
                DobleLinkUSR* temp = this->cabeza;
                
                cout<<setw(10)<<"ID" <<setw(20)<<"Nombre" <<setw(80)<< "Contraseña" <<setw(10)<<"Edad"<<endl;
                cout<<endl;
                while(temp != NULL){
                    cout<<setw(10)<<temp->id<<setw(20)<<temp->nick<<setw(80)<<temp->encrypt<<setw(10)<<to_string(temp->edad)<<endl;
                    
                    temp = temp->siguiente; 
                }
            }
            cout<<endl;
        }

        bool InicioSecion(string nick, string password){
            if(this->cabeza == NULL){
                return false;
            }else{
                DobleLinkUSR* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == nick && temp->password == password){
                        this->usuario_act = temp;
                        this->secionIniciada = true;
                        return true;
                        break;
                    }
                    temp = temp->siguiente;
                }
                this->secionIniciada = false;
                return false;
            }
        }

        void modificarUsuario(int id, string nick, string password, int edad, int money){
            SHA256* sha;
            if(this->cabeza == NULL){
                //cout<<"Lista Vacia"<<endl;
            }else{
                DobleLinkUSR* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->id == this->usuario_act->id && temp->nick == this->usuario_act->nick && temp->password == this->usuario_act->password){
                        this->usuario_act->id = id;
                        this->usuario_act->nick = nick;
                        this->usuario_act->password = password;
                        this->usuario_act->edad = edad;
                        this->usuario_act->monedas = money;
                        temp->id = id;
                        temp->nick = nick;
                        temp->password = password;
                        temp->edad = edad;
                        temp->monedas = money;
                        temp->encrypt = sha->cifrar(password);
                        break;
                    }
                    temp = temp->siguiente;
                    
                }
            }
        }

        void cerrarSecion(){
            this->secionIniciada = false;
            this->usuario_act = NULL;
        }

        void GraficarArbolB(){
            if(this->contadorB == 0){
                if(this->cabeza == NULL){
                    return;
                }else{
                    DobleLinkUSR* temp = this->cabeza;
                    while(temp != NULL){
                        this->arbolB->add(temp->id, temp->nick, temp->encrypt, temp->edad, temp->monedas);
                        temp = temp->siguiente;
                    }
                    //this->arbolB->Graficar();
                    this->contadorB++;
                    //cout<<contadorB;
                }
                this->arbolB->Graficar();
            }
            if(this->contadorB == 1){
                if(this->cabeza == NULL){
                    return;
                }else{
                    DobleLinkUSR* temp = this->cabeza;
                    while(temp != NULL){
                        this->arbolB2->add(temp->id, temp->nick, temp->encrypt, temp->edad, temp->monedas);
                        temp = temp->siguiente;
                    }
                    this->contadorB++;
                }
                this->arbolB2->Graficar();
            }
            if(this->contadorB == 2){
                if(this->cabeza == NULL){
                    return;
                }else{
                    DobleLinkUSR* temp = this->cabeza;
                    while(temp != NULL){
                        this->arbolB3->add(temp->id, temp->nick, temp->encrypt, temp->edad, temp->monedas);
                        temp = temp->siguiente;
                    }
                    this->contadorB++;
                }
                this->arbolB3->Graficar();
            }
            if(this->contadorB == 3){
                if(this->cabeza == NULL){
                    return;
                }else{
                    DobleLinkUSR* temp = this->cabeza;
                    while(temp != NULL){
                        this->arbolB4->add(temp->id, temp->nick, temp->encrypt, temp->edad, temp->monedas);
                        temp = temp->siguiente;
                    }
                    this->contadorB++;
                }
                this->arbolB4->Graficar();
            }
            if(this->contadorB == 4){
                if(this->cabeza == NULL){
                    return;
                }else{
                    DobleLinkUSR* temp = this->cabeza;
                    while(temp != NULL){
                        this->arbolB5->add(temp->id, temp->nick, temp->encrypt, temp->edad, temp->monedas);
                        temp = temp->siguiente;
                    }
                    this->contadorB++;
                }
                this->arbolB5->Graficar();
            }
            if(this->contadorB == 5){
                if(this->cabeza == NULL){
                    return;
                }else{
                    DobleLinkUSR* temp = this->cabeza;
                    while(temp != NULL){
                        this->arbolB6->add(temp->id, temp->nick, temp->encrypt, temp->edad, temp->monedas);
                        temp = temp->siguiente;
                    }
                    this->contadorB++;
                }
                this->arbolB6->Graficar();
            }
        }

        void modificarArbol(){
            if(this->usuario_act == NULL){
                return;
            }else{
                DobleLinkUSR* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->id == usuario_act->id && temp->nick == usuario_act->nick && temp->password == usuario_act->password){
                        temp->ArbolAVL = usuario_act->ArbolAVL;
                        break;
                    }
                    temp = temp->siguiente;
                }
            }
        }
        
        string nombreUsuario(){
            string nombre = "";
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                nombre = this->usuario_act->nick;
            }
            return nombre;
        }

        int idUsuario(){
            int idusuario = 0;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                idusuario = this->usuario_act->id;
            }
            return idusuario;
        }

        int edadUsuario(){
            int edad = 0;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingressado"<<endl;
            }else{
                edad = this->usuario_act->edad;
            }
            return edad;
        }

        int monedasUsuario(){
            int monedas;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                monedas = this->usuario_act->monedas;
            }
            return monedas;
        }

        string passEncrypt(){
            string contrasenia;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                contrasenia = this->usuario_act->encrypt;
            }
            
            return contrasenia;
        }

        string passUsuario(){
            string contrasenia;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                contrasenia = this->usuario_act->password;
            }
            
            return contrasenia;
        }

        void eliminarUsuario(int id){
            DobleLinkUSR* temp = NULL;
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }
            if(this->cabeza->id == id){
                temp = this->cabeza;
                this->cabeza = this->cabeza->siguiente;
                if(this->cabeza != NULL){
                    this->cabeza->anterior = NULL;
                }else{
                    this->final = NULL;
                }
                delete temp;
            }else if(this->final->id == id){
                temp = this->final;
                this->final = this->final->anterior;
                if(this->final != NULL){
                    this->final->siguiente = NULL;
                }else{
                    this->cabeza = NULL;
                }
                delete temp;
            }else{
                temp = this->cabeza;
                while(temp != NULL && temp->id != id){
                    temp = temp->siguiente;
                }
                if(temp == NULL){
                    cout<<"No se encontro"<<endl;
                }else{
                    temp->anterior->siguiente = temp->siguiente;
                    if(temp->siguiente != NULL){
                        temp->siguiente->anterior = temp->anterior;
                    }
                    delete temp;
                }
            }

        }

        void GraficarArbolUsuarioActivo(){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->ArbolAVL->GraphCU(this->usuario_act->nick);
            }
        }

        void mover(DobleLinkUSR* inicio, DobleLinkUSR* final){
            int ide = inicio->id;
            string nom = inicio->nick;
            string pas = inicio->password;
            int ed = inicio->edad;
            int mon = inicio->monedas;
            AVLTree* arbol = inicio->ArbolAVL;
            inicio->id = final->id;
            inicio->nick = final->nick;
            inicio->password = final->password;
            inicio->edad = final->edad;
            inicio->monedas = final->monedas;
            inicio->ArbolAVL = final->ArbolAVL;
            final->id = ide;
            final->nick = nom;
            final->password = pas;
            final->edad = ed;
            final->monedas = mon;
            final->ArbolAVL = arbol;
        }

        void Bubble(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            DobleLinkUSR* inicio = this->cabeza;
            while(task == true){
                //
                task = false;
                while(inicio != NULL && inicio->siguiente != NULL){
                    if(inicio->edad > inicio->siguiente->edad){
                        this->mover(inicio, inicio->siguiente);
                        task = true;
                    }
                    inicio = inicio->siguiente;
                }
                inicio = this->cabeza;
            }
        }

        


        void GrafoDoble(){
            DobleLinkUSR *temp = this->cabeza;
            string dot = "digraph G{\nnode[shape=box];\nedge[dir=both];\nlabel=\"Lista de Usuarios\";\n";
            while(temp != NULL){
                dot += to_string(temp->id)+temp->nick+temp->password+"[label=\"Nombre: "+temp->nick+"\\nPassword: "+temp->encrypt+"\\nEdad: " + to_string(temp->edad) + +"\\nMonedas: " + to_string(temp->monedas) + "\"];\n";
                
                temp = temp->siguiente;
            }
            dot += "\n{rank=same\n";
            DobleLinkUSR *aux = this->cabeza;
            
            while(aux->siguiente != NULL){
                dot += to_string(aux->id)+ aux->nick+aux->password+"->"+to_string(aux->siguiente->id)+aux->siguiente->nick+aux->siguiente->password+";\n";
                aux = aux->siguiente;
            }
            dot += this->cabeza->nick+this->cabeza->password+"->"+this->final->nick+this->final->password+";\n";
            dot += "}\n}\n";
            ofstream file;
            file.open("ListaCUCO.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg ListaCUCO.dot -o Images/ListaCUCO.svg"));
        }
};

//DobleLinkUSR* usuario_esta_activo = NULL;

//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO
//SOLO PARA USUARIOS ARREGLADO