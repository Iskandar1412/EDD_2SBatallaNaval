
//para valor nulo
#include <stddef.h>
#include <cstring>


#include <iostream>
using namespace std;
#include "../../Funciones/sha256.h"

class Nodo_Double{
    public:
    
        Nodo_Double* siguiente;
        Nodo_Double* anterior;
        SHA256* sha;
        string nick;
        string password;
        int edad;
        int monedas;
        string encriptacion;
        Nodo_Double(string name, string pass, int eda, int mon){
            siguiente = NULL;
            anterior = NULL;
            nick = name;
            password = pass;
            edad = eda;
            monedas = mon;
            encriptacion = sha->cifrar(password);
        }
        
    private:
        /* data */
        //int setEdad(int edad);
        //int setMonedas(int monedas);
        //string setNick(string nombre);
        //string setPass(string pass);
};

