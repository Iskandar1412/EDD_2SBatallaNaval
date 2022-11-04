
#include <stddef.h>
#include <cstring>
#include <iostream>
using namespace std;
//para agregar los articulos


class Nodo_Sample{
    public:
        //
        string id;
        Articulo* data;
        Nodo_Sample* siguiente;
        int cant;
        Nodo_Sample(string id, Articulo* data){
            this->id = id;
            this->data = data;
            siguiente = NULL;
            cant = 0;
        }
};

class SLinkedList{
    public:
        //
        int id;
        int longitud;
        Nodo_Sample* cabeza = NULL;
        Nodo_Sample* final = NULL;
        SLinkedList(){
            id = 0;
            longitud = 0;
            cabeza = NULL;
            final = NULL;
        }
        //metodos
        void add(Articulo* data);
        void addCant(Articulo* data, int money);
};



class Articulo{
    public:
        //
        int id;
        string categoria;
        int precio;
        string nombre;
        string src;
        Articulo(int id, string categoria, int precio, string nombre, string src){
            this->id = id;
            this->categoria = categoria;
            this->precio = precio;
            this->nombre = nombre;
            this->src = src;
        }
};
/**/