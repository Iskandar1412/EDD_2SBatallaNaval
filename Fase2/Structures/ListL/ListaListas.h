
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <set>
#include <unordered_set>
#include "ListaSoloMostrar.h"
using namespace std;


struct NodoArticulo{
    int id;
    string categoria;
    int precio;
    string nombre;
    string src;
    NodoArticulo* abajo;
};
//NODO PARA AJUSTAR
//NODO PARA AJUSTAR
//NODO PARA AJUSTAR
//NODO PARA AJUSTAR

struct NodosoloM{
    string categoria;
    NodosoloM* next;
};

NodosoloM* cabezasolom;

void MostrarListasoloM(){
    NodosoloM* temp = cabezasolom;
    cout<<"SOLOMOSTRAR"<<endl;
    while (temp != NULL){
        cout<<temp->categoria<<endl;
        temp = temp->next;
    }
};

void ListasoloMAgreg(string categoryata){
    NodosoloM* temp = new NodosoloM();
    temp->categoria = categoryata;
    temp->next = cabezasolom;
    cabezasolom = temp;
};

void RemoverDuplicados(){
    NodosoloM* anterior = NULL;
    NodosoloM* actual = cabezasolom;
    unordered_set<string>set;
    while(actual != NULL){
        if(set.find(actual->categoria) != set.end()){
            anterior->next = actual->next;
        }else{
            set.insert(actual->categoria);
            anterior = actual;
        }
        actual = anterior->next;
    }
}


//Version 2
//Version 2
//Version 2
//Version 2
//Version 2
//Version 2
//Version 2

class NodoV2{
    public:
        string category;
        NodoV2* siguiente;
        NodoV2* anterior;
        NodoV2(string category){
            this->category = category;
            this->anterior = NULL;
            this->siguiente = NULL;
        }
};



class ListaV2{
    public:
        NodoV2* inicio;
        NodoV2* final;
        int longitud;
        ListaV2(){
            this->longitud = 0;
            this->inicio = NULL;
            this->final = NULL;
        }

        void agregar(string category){
            NodoV2* temp = new NodoV2(category);
            if(this->inicio == NULL){
                this->inicio = temp;
                this->final = temp;
                this->longitud++;
            }else{
                temp->siguiente = inicio;
                inicio->anterior = temp;
                inicio = temp;
                this->longitud++;
            }
        }

        void agregarfinal(string category){
            NodoV2* temp = new NodoV2(category);
            //temp->category = category;
            if(this->final != NULL){
                this->inicio = temp;
                this->final = temp;
                this->longitud++;
            }else{
                temp->anterior = this->final;
                this->final->siguiente = temp;
                this->final = temp;
                this->longitud++;
            }
        }

        void imprimiriniciofin(){
            NodoV2* temp = this->inicio;
            cout<<this->longitud<<endl;;
            while(temp != NULL){
                cout<<temp->category<<endl;
                temp = temp->siguiente;
            }
        }

        void imprimirfininicio(){
            NodoV2* temp = this->final;
            cout<<this->longitud<<endl;;
            while(temp != NULL){
                cout<<temp->category<<endl;
                temp = temp->anterior;
            }
        }

        void eliminarrepetidos(){
            NodoV2* temp;
            NodoV2* aux;
            temp = this->inicio;
            while(temp != NULL){
                aux = temp->siguiente;
                while(aux != NULL){
                    if(temp->category == aux->category){
                        if(aux == this->final){
                            this->final = aux->anterior;
                            this->final->siguiente = NULL;
                            this->longitud--;
                        }else{
                            (aux->anterior)->siguiente = aux->siguiente;
                            (aux->siguiente)->anterior = aux->anterior;
                            this->longitud--;
                        }
                    }
                    aux = aux->siguiente;
                }
                temp = temp->siguiente;
            }
        }

        string ObtenerDato(){
            if(this->inicio != NULL){
                NodoV2* temp = this->inicio;
                while(temp != NULL){
                    return temp->category;
                    temp = temp->siguiente;
                }
            }else{
                return NULL;
            }
        }
};

ListaV2* ListaPrueva = new ListaV2();

//Version 2
//Version 2
//Version 2
//Version 2
//Version 2

//NODO PARA AJUSTAR
//NODO PARA AJUSTAR
//NODO PARA AJUSTAR
//NODO PARA AJUSTAR



LArt* listasolomost = new LArt();
struct NodoCategoria{
    string categoria;
    NodoCategoria* siguiente;
    NodoArticulo* abajo;
};
NodoCategoria* cabecera;

vector<string> cate{};

struct NodoL{
    int id;
    string categoria;
    int precio; 
    string nombre;
    string src;
    NodoL* siguiente;
};
NodoL* cabeceraLI = NULL;
void ListaFull(){
    NodoL* lista = cabeceraLI;

};


void Ajustar(){
    /*
    for(int i = 0; i < cate.size(); i++){
        cout<<cate[i] + " ";
    }
    cout<<endl;
    cout<<endl;
    */
    sort(cate.begin(), cate.end());
    auto last = unique(cate.begin(), cate.end());
    cate.erase(last, cate.end());
    
    //for(int i = cate.size() - 1; i >= 0; i--){
    //    //cout<<cate[i] + " ";
    //    NodoCategoria* temp = new NodoCategoria();
    //    NodoCategoria* aux = cabecera;
    //    temp->categoria = cate[i];
    //    temp->siguiente = cabecera;
    //    cabecera = temp;
    //}
    //RemoverDuplicados();
    ListaPrueva->eliminarrepetidos();
    NodoV2* ex = ListaPrueva->inicio;
    for(int i = 0; i < ListaPrueva->longitud; i++){
        NodoCategoria* temp = new NodoCategoria();
        NodoCategoria* aux = cabecera;
        temp->categoria = ex->category;
        //cout<<ListaPrueva->ObtenerDato()<<endl;
        temp->siguiente = cabecera;
        cabecera = temp;
        ex = ex->siguiente;
    }

    listasolomost->Burbuja();//la lista solo a mostrar
    //cout<<"LISTAPRUEVA"<<endl;
    //ListaPrueva->imprimirfininicio();
    //MostrarListasoloM();
    //cout<<endl;
};

void AgregarCategoria(string categoria){
    ListaPrueva->agregar(categoria);
    ListasoloMAgreg(categoria);
    cate.push_back(categoria);
    //Ajustar();
};

void ListadoArticulos(int id, string categoria, int precio, string nombre, string src){
    //AgregarCategoria(categoria);
    listasolomost->Insertar(id, categoria, precio, nombre, src);
    NodoCategoria* category = cabecera;
    while(category != NULL){
        if(category->categoria == categoria){
            NodoArticulo *temp = new NodoArticulo();
            temp->id = id;
            temp->categoria = categoria;
            temp->nombre = nombre;
            temp->precio = precio;
            temp->src = src;
            NodoArticulo *poner = category->abajo;
            category->abajo = temp;
            temp->abajo = poner;
            break;
        }
        category = category->siguiente;
    }
    if(category == NULL){
        cout<<"Categoria no Encontrada"<<endl;
    }
};

void MostrarLista(){
    NodoCategoria* temp = cabecera;
    while(temp != NULL){
        cout<<temp->categoria<<endl;
        temp = temp->siguiente;
    }
};

void MostrarCategorias(){
    listasolomost->Burbuja();
    listasolomost->Display();
    /*
    NodoCategoria *category = cabecera;
    cout<<"Categoria: "<<endl;
    while(category != NULL){
        NodoArticulo *temp = category->abajo;
        while(temp != NULL){
            cout<<setw(5)<<to_string(temp->id)<<setw(35)<<temp->nombre<<setw(15)<<temp->categoria<<setw(10)<<temp->precio<<endl;
            temp = temp->abajo;
        }
        category = category->siguiente;
    }*/
};

SoloArt* obtenercomprar(int id){
    SoloArt* objeto = listasolomost->acomprar(id);
    return objeto;
};

string sublist(NodoArticulo* temp, string nombre){
    std::string valor = "subgraph{\n";
    NodoArticulo* aux = temp;
    NodoArticulo* temporal = temp;
    valor = valor + "node[shape=box];\n";
    string valorinicial = "n"+to_string(temp->id);
    while(aux != NULL){
        valor = valor + "n"+to_string(aux->id)+"[label=\""+aux->nombre+"\"];\n";
        aux = aux->abajo;
    }
    
    while(temporal->abajo != NULL){
        valor = valor + "n"+to_string(temporal->id)+"->n"+to_string(temporal->abajo->id)+";\n";
        temporal = temporal->abajo;
    }
    valor = valor + nombre + "->" + valorinicial+";}\n";
    return valor;
};

void Grafo(){
    string dot = "digraph G{\n";
    dot = dot + "label=\"ListaListas\";\n";
    dot = dot + "node[shape=box];\n";

    
    
    NodoCategoria* category = cabecera;
    while(category != NULL){
        if(category->abajo != NULL){
                NodoArticulo* temp = category->abajo;
                dot = dot + sublist(temp, category->categoria);
            }   
        category = category->siguiente;
    }
    
    //
    NodoCategoria* cate = cabecera;
    dot = dot + "{rank=same;\n";
    int car = 0;
    
    //while(cate->siguiente != NULL){
        //if(cate->categoria != cate->siguiente->categoria){
    //        dot = dot + cate->categoria + "->" + cate->siguiente->categoria + ";\n";
        //}
    //    cate = cate->siguiente;
    //}

    while(car < ListaPrueva->longitud - 1){
        //if(cate->categoria != cate->siguiente->categoria){
            dot = dot + cate->categoria + "->" + cate->siguiente->categoria + ";\n";
        //}
        car++;
        cate = cate->siguiente;
    }

    dot = dot + "}\n}";
    ofstream file;
    file.open("ListaListas.dot");
    file<<dot;
    file.close();
    system(("dot -Tsvg ListaListas.dot -o Images/ListaListas.svg"));
    //system(("ListaListas.svg"));//No estoy seguro si dejarselo
    //cout<<dot<<endl;
};

