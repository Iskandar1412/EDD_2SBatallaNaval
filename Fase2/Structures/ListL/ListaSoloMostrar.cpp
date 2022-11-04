#include <string>
#include <fstream>
#include <stddef.h>
//incluir string
#include <iomanip>
#include <cstring>
#include <iostream>
using namespace std;

class SoloArt{
    public:
        //
        int id;
        string categoria;
        int precio;
        string nombre;
        string src;
        SoloArt* siguiente;
        SoloArt* anterior;
        SoloArt(int id, string categoria, int precio, string nombre, string src){
            this->id = id;
            this->categoria = categoria;
            this->precio = precio;
            this->nombre = nombre;
            this->src = src;
            this->siguiente = NULL;
            this->anterior = NULL;
        } 
};

class LArt{
    public:
        //
        SoloArt* cabeza;
        SoloArt* final;
        SoloArt* Seleccionado;
        LArt(){
            this->cabeza = NULL;
            this->final = NULL;
            this->Seleccionado = NULL;
        }

        void Insertar(int id, string categoria, int precio, string nombre, string src){
            SoloArt* nodo = new SoloArt(id, categoria, precio, nombre, src);
            if(this->cabeza == NULL){
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                this->final->siguiente = nodo;
                nodo->anterior = this->final;
                this->final = nodo;
            }
        }

        void Display(){
            if(this->cabeza == NULL){
                cout<<"NO EXISTEN ARTICULOS (LISTA VACIA) :("<<endl;
            }else{
                SoloArt* temp = this->cabeza;
                cout<<setw(10)<<"ID"<<setw(35)<<"Nombre"<<setw(15)<<"Categoria"<<setw(10)<<"Precio"<<endl;
                cout<<endl;
                while(temp != NULL){
                    cout<<setw(10)<<to_string(temp->id)<<setw(35)<<temp->nombre<<setw(15)<<temp->categoria<<setw(10)<<temp->precio<<endl;
                    temp = temp->siguiente;
                }
                cout<<endl;
            }
        }

        SoloArt* acomprar(int id){
            if(this->cabeza == NULL){
                return NULL;
            }
            SoloArt* nodo = this->cabeza;
            while(nodo != NULL){
                if(nodo->id == id){
                    return nodo;
                    break;
                }
                nodo = nodo->siguiente;
            }
            return NULL;
        }

        void mover(SoloArt* inicio, SoloArt* final){
            int id = inicio->id;
            string categoria = inicio->categoria;
            int precio = inicio->precio;
            string nombre = inicio->nombre;
            string src = inicio->src;
            inicio->id = final->id;
            inicio->categoria = final->categoria;
            inicio->precio = final->precio;
            inicio->nombre = final->nombre;
            inicio->src = final->src;
            final->id = id;
            final->categoria = categoria;
            final->precio = precio;
            final->nombre = nombre;
            final->src = src;
        }

        void Burbuja(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            SoloArt* inicio = this->cabeza;
            while(task == true){
                task = false;
                while(inicio != NULL && inicio->siguiente != NULL){
                    if(inicio->precio > inicio->siguiente->precio){
                        this->mover(inicio, inicio->siguiente);
                        task = true;
                    }
                    inicio = inicio->siguiente;
                }
                inicio = this->cabeza;
            }
        }
};