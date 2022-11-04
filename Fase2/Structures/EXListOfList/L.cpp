#include <stddef.h>
#include <cstring>
#include <iostream>
using namespace std;

class Nodo{
    private:
        //
    public:
        //
        Nodo* siguiente;
        Nodo* abajo;
        string categoria;
        Nodo(){
            categoria = "";
            siguiente = NULL;
            abajo = NULL;
        }


};