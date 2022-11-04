//Llamar

#include <iostream>
#include <stddef.h>
#include <cstring>
#include "Articulo.h"

using namespace std;

typedef struct Nodo{
    Articulo articulo;
    struct Nodo* siguiente;
}Nodo;

typedef struct List{
    Nodo* cabeza;
    int longitud;
}List;


void InsertarPrincipio(List* lista, Articulo* articulo);
void InsertarFinal(List* lista, Articulo* articulo);
void InsertarDespues(int n, List* lista, Articulo* articulo);
void ObtenerTodo(List* lista);
void Obtener(int n, List* lista);
void EliminarPrincipio(List* lista);
void EliminarUltimo(List* lista);
void EliminarElemento(int n, List* lista);
Articulo* toString(List* lista);

