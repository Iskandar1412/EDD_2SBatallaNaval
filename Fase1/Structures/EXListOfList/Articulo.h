
#define Articulo_h

#include <stddef.h>
#include <cstring>
#include <iostream>
using namespace std;

typedef struct Articulo{
    int id;
    string categoria;
    int precio;
    string nombre;
    string src;
}Articulo;
