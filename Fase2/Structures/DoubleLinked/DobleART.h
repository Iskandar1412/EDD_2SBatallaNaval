#include <stddef.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>


//incluir string
#include <iomanip>
#include <cstring>

using namespace std;


class DobleART_N{
    public:
        //
        
        string nombre;
        int id;
        string src;
        int precio;
        string categoria;
        DobleART_N* siguiente;
        DobleART_N* anterior;
        DobleART_N(int id, string categoria, string nombre, int precio, string src){
            this->id = id;
            this->nombre = nombre;
            this->src = src;
            this->precio = precio;
            this->categoria = categoria;
            this->siguiente = NULL;
            this->anterior = NULL;

        }
};

class DobleLART{//LISTA
    public:
        //
        //int valor;
        DobleART_N* cabeza;
        DobleART_N* final;
        DobleART_N* ArticuloSeleccionado;
        bool articuloesta;
        DobleLART(){
            //this->valor = 0;
            this->articuloesta = false;
            this->ArticuloSeleccionado = NULL;
            this->cabeza = NULL;
            this->final = NULL;
        }
        void add(int id, string categoria, string nombre, int precio, string src){
            
            //nodo->id = this->valor++;
            if(this->cabeza == NULL){
                DobleART_N* nodo = new DobleART_N(id, categoria, nombre, precio, src);
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                bool poderono = false;
                DobleART_N* temp = cabeza;
                while(temp  != NULL){
                    if(temp->id == id){
                        cout<<"ID Existente :v"<<endl;
                        poderono = false;
                        break;
                    }else{
                        poderono = true;
                    }
                    temp = temp->siguiente;
                    
                }
                if(poderono == true){
                    DobleART_N* nodo = new DobleART_N(id, categoria, nombre, precio, src);
                    this->final->siguiente = nodo;
                    nodo->anterior = this->final;
                    this->final = nodo;

                }
                return;
            }
        }
        void Display(){
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }else{
                DobleART_N* temp = this->cabeza;
                
                cout<<setw(10)<<"ID" <<setw(20)<<"Nombre"  <<setw(10)<<"precio"<<endl;
                cout<<endl;
                while(temp != NULL){
                    cout<<setw(10)<<temp->id<<setw(20)<<temp->nombre<<setw(10)<<to_string(temp->precio)<<endl;
                    
                    temp = temp->siguiente; 
                }
            }
            cout<<endl;
        }

        

        bool BuscarArticulo(int id){
            if(this->cabeza == NULL){
                return false;
            }else{
                DobleART_N* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->id == id){
                        this->ArticuloSeleccionado = temp;
                        this->articuloesta = true;
                        return true;
                        break;
                    }
                    temp = temp->siguiente;
                }
                this->articuloesta = false;
                return false;
            }
        }

        int precioArticuloSeleccionado(){
            int precio = 0;
            if(this->ArticuloSeleccionado == NULL){
                cout<<"Articulo no Existente"<<endl;
            }else{
                precio = this->ArticuloSeleccionado->precio;
            }
            return precio;
        }

        int IDArticuloSeleccionado(){
            int id_seleccion = 0;
            if(this->ArticuloSeleccionado == NULL){
                cout<<"Articulo no Existente"<<endl;
            }else{
                id_seleccion = this->ArticuloSeleccionado->id;
            }
            return id_seleccion;
        }

        string nombreArticuloSeleccionado(){
            string nombre = "";
            if(this->ArticuloSeleccionado == NULL){
                cout<<"Articulo no Existente"<<endl;
            }else{
                nombre = this->ArticuloSeleccionado->nombre;
            }
            return nombre;
        }

        string srcArticuloSeleccionado(){
            string src = "";
            if(this->ArticuloSeleccionado == NULL){
                cout<<"Articulo no Existente"<<endl;
            }else{
                src = this->ArticuloSeleccionado->src;
            }
            return src;
        }

        string categoriaArticuloSeleccionado(){
            string categoria = "";
            if(this->ArticuloSeleccionado == NULL){
                cout<<"Articulo no Existente"<<endl;
            }else{
                categoria = this->ArticuloSeleccionado->categoria;
            }
            return categoria;
        }


        void mover(DobleART_N* inicio, DobleART_N* final){
            int ide = inicio->id;
            string nom = inicio->nombre;
            string pas = inicio->src;
            int ed = inicio->precio;
            string cate = inicio->categoria;
            inicio->id = final->id;
            inicio->nombre = final->nombre;
            inicio->src = final->src;
            inicio->precio = final->precio;
            inicio->categoria = final->categoria;
            final->id = ide;
            final->nombre = nom;
            final->src = pas;
            final->precio = ed;
            final->categoria = cate;
        }

        void Bubble(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            DobleART_N* inicio = this->cabeza;
            while(task == true){
                //
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