
#include "SLinkedList.h"
#include "sstream"
using namespace std;

void SLinkedList::add(Articulo* data){
    //Articulo* a = new Articulo(5, "S", 33, "sdf", "ssssss");
    stringstream sotu;
    sotu<<id;
    string tost;
    sotu>>tost;
    string ide = "n"+id;
    Nodo_Sample* temporal = new Nodo_Sample(ide, data);
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

void SLinkedList::addCant(Articulo* data, int money){
    //
    stringstream sotu;
    sotu<<id;
    string tost;
    sotu>>tost;
    string ide = "n"+id;
    Nodo_Sample* temporal = new Nodo_Sample(ide, data);
    temporal->cant = money;
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
/**/