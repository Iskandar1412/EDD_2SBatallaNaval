#include <string>
#include <iostream>
#include <stdlib.h>
using namespace std;

class Articulo{
    private:
        //
        int id;
        string categoria;
        int precio;
        string nombre;
        string src;
    public:
        //
        Articulo(int id, string categoria, int precio, string nombre, string src){
            this->id = id;
            this->categoria = categoria;
            this->precio = precio;
            this->nombre = nombre;
            this->src = src;
        }
        int getID(){
            return this->id;
        }
        void setID(int id){
            this->id = id;
        }
        string getCategoria(){
            return this->categoria;
        }
        void setCategoria(string categoria){
            this->categoria = categoria;
        }
        int getPrecio(){
            return this->precio;
        }
        void setPrecio(int precio){
            this->precio = precio;
        }
        string getNombre(){
            return this->nombre;
        }
        void setNombre(string nombre){
            this->nombre = nombre;
        }
        string getSRC(){
            return this->src;
        }
        void setSRC(string src){
            this->src = src;
        }
};

class NodoART{
    public:
        //
        Articulo articulo = Articulo(0, "", 0, "", "");
        Articulo valor = Articulo(0, "", 0, "", "");
        NodoART* siguiente;
        NodoART(){
            siguiente = NULL;
            articulo = valor;    
        }
};

class NodoCAT{
    public:
        //
        ListaCAT listaprincipal;
        Articulo articulo = Articulo(0, "", 0, "", "");
        Articulo valor = Articulo(0, "", 0, "", "");
        NodoCAT* siguiente;
        NodoCAT(){
            siguiente = NULL;
            articulo = valor;
        }
};

class ListaART{
    public:
        //
        NodoART* inicio;
        ListaART(){
            inicio = NULL;
        }
        void InsertarFinal(Articulo valor);
        void InsertarOrden(Articulo valor);
        void Mostrar();
};

class ListaCAT{
    public:
        //
        NodoCAT* cabeza;
        ListaCAT(){
            cabeza = NULL;
        }
        void MostrarLista();
        void Grafo();
        void Insertar(Articulo* articulo, string categoria);
        NodoCAT * BuscarNodo(NodoCAT* inicio, string categoria);
};


//METODOS
//METODOS PARA LA LISTA DE CATEGORIAS (NODO SEC.)
void ListaART::InsertarFinal(Articulo valor){
    NodoART* category = new NodoART();
    category->valor = valor;
    if(inicio == NULL){
        inicio = category;
    }else{
        NodoART* aux = inicio;
        while(aux != NULL){
            if(aux->siguiente == NULL){
                aux->siguiente = category;
                break;
            }
            aux = aux->siguiente;
        }
    }
}; 

void ListaART::InsertarOrden(Articulo valor){
    NodoART* category = new NodoART();
    category->valor = valor;
    if(inicio == NULL){
        inicio = category;
    }else{
        NodoART* aux = inicio;
        NodoART* auxsig;
        while(aux != NULL){
            auxsig = aux->siguiente;
            if(((category->valor).getPrecio())<((aux->valor).getPrecio())){
                category->siguiente = aux;
                inicio = category;
                break;
            }else if(auxsig != NULL){
                aux->siguiente = category;
                break;
            }else if(((category->valor).getPrecio())<((auxsig->valor).getPrecio())){
                aux->siguiente = category;
                category->siguiente = auxsig->siguiente;
                break;
            }
            aux = aux->siguiente;
        }
    }
};

void ListaART::Mostrar(){
    NodoART* temp = inicio;
    while(temp != NULL){
        cout<<(temp->valor).getCategoria()<<endl;
        temp = temp->siguiente;
    }
};

//LISTA DE CATEGORIAS (LISTA QUE CONTIENE TODO)

void ListaCAT::MostrarLista(){
    NodoCAT* category = cabeza;
    while(category != NULL){
        cout<<(category->valor).getCategoria()<<endl;
        
    }
}