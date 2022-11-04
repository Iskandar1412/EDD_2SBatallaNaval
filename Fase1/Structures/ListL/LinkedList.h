/*
#include <stddef.h>
#include <cstring>
#include <iostream>
using namespace std;
//incluir la de la lista enlazada secundaria
#include "SLinkedList.cpp"


///para la que obtendrá la primera cadena
class Nodo_Simple{
    public:
        //
        string id;
        string categoria;
        Nodo_Simple* siguiente;
        SLinkedList* nuevoarticulo;
        Nodo_Simple(string id, string data){
            this->id = id;
            this->categoria = data;
            nuevoarticulo = new SLinkedList();
            siguiente = NULL;
        }
        string tostring();
        void addArticle(Articulo* data, int money);
};

class LinkedList{
    public:
        //
        Nodo_Simple* cabeza = NULL;
        Nodo_Simple* final = NULL;
        int longitud;
        int id;
        LinkedList(){
            cabeza = NULL;
            final = NULL;
            longitud = 0;
            id = 0;
        }
        void agregar(string categoria);

};
*/
/*
class Category{
    public:
        //
        string categoria;
        SLinkedList* article;
        Category(string categoria){
            this->categoria = categoria;
            article = new SLinkedList();
        }
        //metodos para ello
        //SLinkedList* agregarCat(Articulo* data, int money);
        string tostring();
        void addArticle(Articulo* data, int money);
};
*/