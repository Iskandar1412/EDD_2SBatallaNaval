//para llamar al nodo
//#include "Nodo.h"
//para mostrar en consola
#include <iostream>
//para que se acepten valores nulos
#include <stddef.h>
//incluir string
#include <cstring>

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


class DoubleLinkedList{
    public:
        //
        Nodo_Double* cabeza = NULL;
        Nodo_Double* ultimo = NULL;
        int longitud = 0;

        DoubleLinkedList(){
            cabeza = NULL;
            ultimo = NULL;
            longitud = 0;
        }
        //metodos
        void agregarUsuario(string nick, string password, int edad, int monedas);
        void mostrarUsuarios();
        void eliminarUsuario(string nombre);
        void modificarUsuario(string nombre, string nuevonam, string pass, int edad);
        void GraficarUsuarios();
    private:
        //
};



void SortUsuarios(DoubleLinkedList* listausuarios){
    


};

