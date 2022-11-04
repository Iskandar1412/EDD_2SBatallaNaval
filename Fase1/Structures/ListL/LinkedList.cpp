/*
#include "LinkedList.h"
#include "SLinkedList.cpp"

void LinkedList::agregar(string categoria){
    stringstream sotu;
    sotu<<id;
    string tost;
    sotu>>tost;
    string ide = "n"+id;
    Nodo_Simple* temporal = new Nodo_Simple(ide, categoria);
    if(cabeza == NULL){
        cabeza = temporal;
        final = temporal;
    }else{
        final->siguiente = temporal;
        final = temporal;
    }
    longitud++;
    id++;
};



string Nodo_Simple::tostring(){
    string texto = "Categoria: " + categoria;
    return texto;
};

void Nodo_Simple::addArticle(Articulo *article, int money){
    nuevoarticulo->addCant(article, money);
};
*/