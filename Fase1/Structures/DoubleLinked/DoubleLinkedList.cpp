//lista doblemente circular
#include "./DoubleLinkedList.h"
#include <fstream>
#include <iterator>
#include <iomanip>
#include <iostream>

//metodos llamados desde lista doble

void DoubleLinkedList::agregarUsuario(string nick, string password, int edad, int monedas){
    //crear instancia del nodo
    
    Nodo_Double* temporal = new Nodo_Double(nick, password, edad, monedas);
    
    if(cabeza == NULL){
        cabeza = temporal;
        ultimo = temporal;
        cabeza->siguiente = cabeza;
        cabeza->anterior = ultimo;
        longitud++;
    }else{
        ultimo->siguiente = temporal;
        temporal->anterior = ultimo;
        temporal->siguiente = cabeza;
        ultimo = temporal;
        cabeza->anterior = ultimo;
        ultimo->siguiente = cabeza;
        cabeza->anterior = ultimo;
        
        longitud++;
    }
    
};

void DoubleLinkedList::mostrarUsuarios(){
    Nodo_Double* temporal = cabeza;
    int val = 0;
    while(val < longitud){
        cout<<temporal->nick<<endl;
        temporal = temporal->siguiente;
        val++;
    }
};

void DoubleLinkedList::eliminarUsuario(string nombre){
    Nodo_Double* temporal = cabeza;
    int val = 0;
    while(val < longitud){
        if(nombre == cabeza->nick && nombre == temporal->nick){
            cabeza = cabeza->siguiente;
            cabeza->anterior = ultimo;
            ultimo->siguiente = cabeza;
            longitud--;
        }else if(nombre == ultimo->nick && nombre == temporal->nick){
            ultimo = ultimo->anterior;
            ultimo->siguiente = cabeza;
            cabeza->anterior = ultimo;
            longitud--;
        }else if(nombre == temporal->nick){
            Nodo_Double* eliminado = temporal->anterior;
            Nodo_Double* el = temporal->siguiente;
            temporal = eliminado;
            //temporal->anterior = el;
            //Nodo* siguiente = temporal->siguiente;
            //cout<<eliminado->nick + "   :::"<<endl;
            temporal->siguiente = eliminado->siguiente->siguiente;
            //temporal->anterior = el;
            temporal->siguiente->anterior = temporal;
            //temporal->siguiente->anterior = el;
            //cout<<"::: " + temporal->anterior->nick<<endl;
            //free(eliminado);
            longitud--;   
        }
        //cout<<temporal->nick<<endl;
        temporal = temporal->siguiente;
        val++;
    }

    /*
    Nodo* inicio = cabeza;
    cout<<"Siguientes"<<endl;
    cout<<inicio->nick<<endl;
    cout<<inicio->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->nick<<endl;
    cout<<inicio->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->siguiente->nick<<endl;
    cout<<"Anteriores"<<endl;
    cout<<inicio->nick<<endl;
    cout<<inicio->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->anterior->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<inicio->anterior->anterior->anterior->anterior->anterior->anterior->anterior->anterior->anterior->anterior->nick<<endl;
    cout<<"cabeza: " + cabeza->nick<<endl;
    cout<<"final: " + ultimo->nick<<endl;
    */
};

void DoubleLinkedList::modificarUsuario(string nombre, string nuevonombre, string pass, int edad){
    Nodo_Double* temporal = cabeza;
    int val = 0;
    while(val < longitud){
        //
        if(nombre == temporal->nick){
            temporal->nick = nuevonombre;
            temporal->edad = edad;
            temporal->password = pass;
        }
        temporal = temporal->siguiente;
        val++;
    }
};

void DoubleLinkedList::GraficarUsuarios(){
    Nodo_Double* temporal = cabeza;
    string concat = "";
    int val = 0;
    while(val < longitud + 1){
        //

    }
};  

///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!
///VALIEDNO MADRES ¡¡¡A CREAR OTRA LISTA PARA ARREGLAR!!!

class NodoDobleL{
    public:
        //
        SHA256* sha;
        string nick;
        //int id;
        string password;
        int edad;
        int monedas;
        string encrypt;
        NodoDobleL* siguiente;
        NodoDobleL* anterior;
        NodoDobleL(string nick, string password, int edad, int monedas){
            //this->id = 0;
            this->nick = nick;
            this->password = password;
            this->edad = edad;
            this->monedas = monedas;
            this->encrypt = sha->cifrar(password);
            this->siguiente = NULL;
            this->anterior = NULL;
        }
};

class DobleL{
    public:
        //
        //int valor;
        NodoDobleL* cabeza;
        NodoDobleL* final;
        DobleL(){
            //this->valor = 0;
            this->cabeza = NULL;
            this->final = NULL;
        }
        void Insertar(string nombre, string password, int edad, int monedas){
            
            NodoDobleL* nodo = new NodoDobleL(nombre, password, edad, monedas);
            //nodo->id = this->valor++;
            if(this->cabeza == NULL){
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                this->final->siguiente = nodo;
                nodo->anterior = this->final;
                this->final = nodo;
            }
        }
        void Display(){
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }else{
                NodoDobleL* temp = this->cabeza;
                
                cout<<setw(20)<<"Nombre" <<setw(80)<< "Contraseña" <<setw(10)<<"Edad"<<endl;
                cout<<endl;
                while(temp != NULL){
                    cout<<setw(20)<<temp->nick<<setw(80)<<temp->encrypt<<setw(10)<<to_string(temp->edad)<<endl;
                    
                    temp = temp->siguiente; 
                }
            }
            cout<<endl;
        }

        void modificarUsuario(string nombre, string nuevonombre, string password, string nuevapassword, int edad, int money){
            SHA256* sha;
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }else{
                NodoDobleL* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == nombre && temp->password == password){
                        temp->nick = nuevonombre;
                        temp->password = nuevapassword;
                        temp->edad = edad;
                        temp->monedas = money;
                        temp->encrypt = sha->cifrar(nuevapassword);
                    }
                    temp = temp->siguiente;
                }
            }
        }

        NodoDobleL* InicioSecion(string nick, string password){
            if(this->cabeza == NULL){
                return NULL;
            }else{
                NodoDobleL* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == nick && temp->password == password){
                        return temp;
                        break;
                    }
                    temp = temp->siguiente;
                }
                return NULL;
            }
        }

        void eliminarUsuario(string nombre){
            NodoDobleL* temp = NULL;
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }
            if(this->cabeza->nick == nombre){
                temp = this->cabeza;
                this->cabeza = this->cabeza->siguiente;
                if(this->cabeza != NULL){
                    this->cabeza->anterior = NULL;
                }else{
                    this->final = NULL;
                }
                delete temp;
            }else if(this->final->nick == nombre){
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
                while(temp != NULL && temp->nick != nombre){
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

        void mover(NodoDobleL* inicio, NodoDobleL* final){
            string nom = inicio->nick;
            string pas = inicio->password;
            int ed = inicio->edad;
            int mon = inicio->monedas;
            inicio->nick = final->nick;
            inicio->password = final->password;
            inicio->edad = final->edad;
            inicio->monedas = final->monedas;
            final->nick = nom;
            final->password = pas;
            final->edad = ed;
            final->monedas = mon;
        }

        void Bubble(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            NodoDobleL* inicio = this->cabeza;
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
            NodoDobleL *temp = this->cabeza;
            string dot = "digraph G{\nnode[shape=box];\nedge[dir=both];\nlabel=\"Lista de Usuarios\";\n";
            while(temp != NULL){
                dot += temp->nick+temp->password+"[label=\"Nombre: "+temp->nick+" \\n\\ Password: "+temp->encrypt+" \\n\\ Edad: " + to_string(temp->edad) + +" \\n\\ Monedas: " + to_string(temp->monedas) + "\"];\n";
                temp = temp->siguiente;
            }
            dot += "\n{rank=same\n";
            NodoDobleL *aux = this->cabeza;
            
            while(aux->siguiente != NULL){
                dot += aux->nick+aux->password+"->"+aux->siguiente->nick+aux->siguiente->password+";\n";
                aux = aux->siguiente;
            }
            dot += this->cabeza->nick+this->cabeza->password+"->"+this->final->nick+this->final->password+";\n";
            dot += "}\n}\n";
            ofstream file;
            file.open("ListaUsuarios.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg ListaUsuarios.dot -o Images/ListaUsuarios.svg"));
        }

        
};