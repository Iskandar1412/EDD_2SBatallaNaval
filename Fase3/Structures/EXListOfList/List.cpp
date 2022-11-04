#include "./List.h"
#include <iostream>
#include <stddef.h>
#include <cstring>
using namespace std;


Nodo* CrearNodo(Articulo* articulo){
    Nodo* nodo = (Nodo *) malloc(sizeof(Nodo));
    nodo->articulo.id;
    nodo->articulo.categoria;
    nodo->articulo.precio;
    nodo->articulo.nombre;
    nodo->articulo.src;
    nodo->siguiente = NULL;
    return nodo;
}

//Destruir Nodo
void DestruirNodo(Nodo* nodo){
    free(nodo);
}

void InsertarPrincipio(List* lista, Articulo* articulo){
    Nodo* nodo = CrearNodo(articulo);
    nodo->siguiente = lista->cabeza;
    lista->cabeza = nodo;
    lista->longitud++;
}

void InsertarFinal(List* lista, Articulo* articulo){
    Nodo* nodo = CrearNodo(articulo);
    if(lista->cabeza == NULL){
        lista->cabeza = nodo;

    }else{
        Nodo* puntero = lista->cabeza;
        while(puntero->siguiente){
            puntero = puntero->siguiente;
        }
        puntero->siguiente = nodo;
    }
    lista->longitud++;
}

void InsertarDespues(int n, List* lista, Articulo* articulo){
    Nodo* nodo = CrearNodo(articulo);
    if(lista->cabeza = NULL){
        lista->cabeza = nodo;
    }else{
        Nodo* puntero = lista->cabeza;
        int posicion = 0;
        while(posicion < n && puntero->siguiente){
            puntero = puntero->siguiente;
            posicion++;
        }
        //en el caso de que se llegue al final de la lista pero 
        //no alcanzamos la posición que se pide ocurre que se le asigna
        //al siguiente se le asociara lista vacia como es un nulo
        nodo->siguiente = puntero->siguiente;
        //ya se le asigna
        puntero->siguiente = nodo;
    }
    lista->longitud++;
}

void Obtener(int n, List* lista){
    if(lista->cabeza == NULL){
        //return NULL;
        cout<<"La lista está vacia"<<endl;
    }else{
        Nodo* puntero = lista->cabeza;
        int posicion = 0;
        while(posicion < n && puntero->siguiente){
            puntero = puntero->siguiente,
            posicion++;
        }
        if(posicion != n){
            cout<<"No existe valor en la posicion"<<endl;
            //return NULL;
        }else{
            //return &puntero->articulo;
            cout<<&puntero->articulo<<endl;
        }
    }
}

void ObtenerTodo(List* lista){
    Nodo* puntero = lista->cabeza;
    int posicion = 0;
    while(puntero != NULL){
        cout<<puntero->articulo.nombre<<endl;
        puntero = puntero->siguiente;
    }
}

int contar(List* lista){
    return lista->longitud;
}

//para comprobar si la lista está vacia
int EstaVacia(List* lista){
    return lista->cabeza == NULL;
}

//Eliminar elementos 
void EliminarPrincipio(List* lista){
    if(lista->cabeza){
        Nodo* eliminado = lista->cabeza;
        lista->cabeza = lista->cabeza->siguiente;
        DestruirNodo(eliminado);
        lista->longitud--;
    }
}

void EliminarUltimo(List* lista){
    if(lista->cabeza){
        if(lista->cabeza->siguiente){
            Nodo* puntero = lista->cabeza;
            while(puntero->siguiente->siguiente){
                puntero = puntero->siguiente;
            }
            Nodo* eliminado = puntero->siguiente;
            puntero->siguiente == NULL;
            DestruirNodo(eliminado);
            lista->longitud--;
        }else{
            Nodo* eliminado = lista->cabeza;
            lista->cabeza = NULL;
            DestruirNodo(eliminado);
            lista->longitud--;
        }
    }
}

void EliminarElemento(int n, List* lista){
    if(lista->cabeza){
        if(n == 0){
            Nodo* eliminado = lista->cabeza;
            lista->cabeza = lista->cabeza->siguiente;
            DestruirNodo(eliminado);
            lista->longitud--;
        }else if(n < lista->longitud){
            Nodo* puntero = lista->cabeza;
            int posicion = 0;
            while(posicion < (n - 1)){
                puntero = puntero->siguiente;
                posicion++;
            }
            Nodo* eliminado = puntero->siguiente;
            puntero->siguiente = eliminado->siguiente;
            DestruirNodo(eliminado);
            lista->longitud--;
        }
    }
}
