#include <stddef.h>
#include <cstring>
#include <iostream>
using namespace std;
#include "List.cpp"

typedef struct Tipo{
    string tipo;
    List* lista = new List();
}Tipo;

