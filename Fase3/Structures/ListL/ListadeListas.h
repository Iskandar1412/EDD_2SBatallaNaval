
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <set>
#include <unordered_set>
using namespace std;



class Nodo_Article{
    public:
        int id;
        string categoria;
        int precio;
        string nombre;
        string src;
        Nodo_Article* siguiente;
        Nodo_Article* anterior;
        Nodo_Article() = default;
        Nodo_Article(int id,string categoria,int precio,string nombre,string src){
            this->id = id;
            this->categoria = categoria;
            this->precio = precio;
            this->nombre = nombre;
            this->src = src;
            this->siguiente = NULL;
            this->anterior = NULL;
        }
};

class ListaArt{
    public:
        Nodo_Article* cabeza;
        Nodo_Article* final;
        Nodo_Article* ArticuloSeleccionado;
        int valormasbajo;
        bool ArticuloEsta;
        ListaArt(){
            this->valormasbajo = 0;
            this->cabeza = NULL;
            this->final = NULL;
            this->ArticuloEsta = false;
            this->ArticuloSeleccionado = NULL;
        }

        void  add(int id, string categoria, int precio, string nombre, string src){
            if(this->cabeza == NULL){
                Nodo_Article* nodo = new Nodo_Article(id, categoria, precio, nombre, src);
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                bool poderono = false;
                Nodo_Article* temp = cabeza;
                while(temp != NULL){
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
                    Nodo_Article* aux = new Nodo_Article(id, categoria, precio, nombre, src);
                    this->final->siguiente = aux;
                    aux->anterior = this->final;
                    this->final = aux;
                }
                return;
            }
        }

        void DisplayART(){
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }else{
                Nodo_Article* temp = this->cabeza;
                cout<<setw(5)<<"ID"<<setw(20)<<"Nombre"<<setw(20)<<"Precio"<<endl<<endl;
                while(temp != NULL){
                    cout<<setw(5)<<temp->id<<setw(20)<<temp->nombre<<setw(20)<<temp->precio<<endl;
                    temp = temp->siguiente;
                }
            }
            cout<<endl;
        }

        

        void mover(Nodo_Article* inicio, Nodo_Article* final){
            int ide = inicio->id;
            string catego = inicio->categoria;
            int prec = inicio->precio;
            string sr = inicio->src;
            string name = inicio->nombre;
            inicio->id = final->id;
            inicio->categoria = final->categoria;
            inicio->nombre = final->nombre;
            inicio->precio = final->precio;
            inicio->src = final->src;
            final->id = ide;
            final->categoria = catego;
            final->precio = prec;
            final->nombre = name;
            final->src = sr;
        }

        string subgraph(string nombrecat){
            
            if(this->cabeza == NULL){
                return "";
            }else{
                string dot = "subgraph{\n";
                dot += "node[shape=box];\n";
                
                Nodo_Article* aux = this->cabeza;
                //cout<<aux->id;
                while(aux != NULL){
                    dot += "n"+to_string(aux->id)+"[label=\""+aux->nombre+"\"];\n";
                    aux = aux->siguiente;
                }
                Nodo_Article* temp = this->cabeza;
                while(temp != NULL && temp->siguiente != NULL){
                    dot += "n"+to_string(temp->id)+"->n"+to_string(temp->siguiente->id)+";\n";
                    temp = temp->siguiente;
                }
                dot = dot + nombrecat + "->n"+to_string(valormasbajo)+";}\n";
                return dot;
            }
            
            

        }

        void Bubble(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            Nodo_Article* intro = this->cabeza;
            while(task == true){
                task = false;
                while(intro != NULL && intro->siguiente != NULL){
                    if(intro->id > intro->siguiente->id){
                        this->mover(intro, intro->siguiente);
                        task = true;
                    }
                    intro = intro->siguiente;
                }
                intro = this->cabeza;
            }
            this->valormasbajo = this->cabeza->id;
        }
};

class Nodo_List_A{
    public:
        string categoria;
        Nodo_List_A* siguiente;
        Nodo_List_A* anterior;
        ListaArt* abajo;
        Nodo_List_A(string categoria){
            this->categoria = categoria;
            this->abajo = new ListaArt();
            this->siguiente = NULL;
            this->anterior = NULL;
        }
};

class ListaListas{
    public:
        Nodo_List_A* cabeza;
        Nodo_List_A* final;
        Nodo_List_A* Seleccionado;
        Nodo_Article* articulo;
        ListaListas(){
            this->cabeza = NULL;
            this->final = NULL;
            this->Seleccionado = NULL;
            this->articulo = NULL;
        }

        void AgregarCate(string categoria){
            if(this->cabeza == NULL){
                Nodo_List_A* nodo = new Nodo_List_A(categoria);
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                bool poderono = false;
                Nodo_List_A* temp = cabeza;
                while(temp != NULL){
                    if(temp->categoria == categoria){
                        //cout<<"Categoria Existente :v"<<endl;
                        poderono = false;
                        break;
                    }else{
                        poderono = true;
                    }
                    temp = temp->siguiente;
                }
                if(poderono == true){
                    Nodo_List_A* aux = new Nodo_List_A(categoria);
                    this->final->siguiente = aux;
                    aux->anterior = this->final;
                    this->final = aux;
                }
                return;
            }
        }

        void mover(Nodo_List_A* inicio, Nodo_List_A* final){
            string categoria = inicio->categoria;
            ListaArt* abajo = inicio->abajo;
            inicio->categoria = final->categoria;
            inicio->abajo = final->abajo;
            final->categoria = categoria;
            final->abajo = abajo;

        }
        void Burbuja(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            Nodo_List_A* aux = this->cabeza;
            while(task == true){
                task = false;
                while(aux != NULL && aux->siguiente != NULL){
                    if(aux->categoria > aux->siguiente->categoria){
                        this->mover(aux, aux->siguiente);
                        task = true;
                    }
                    aux = aux->siguiente;
                }
                aux = this->cabeza;
            }
        }

        void agregarArticulo(int id, string categoria, string nombre, int precio, string src){
            if(this->cabeza == NULL){
                return;
            }else{
                Nodo_List_A* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->categoria == categoria){
                        temp->abajo->add(id, categoria, precio, nombre, src);
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void Display(){
            this->Burbuja();
            if(this->cabeza == NULL){
                cout<<"ListaVacia :v"<<endl;
            }else{
                Nodo_List_A* temp = this->cabeza;
                while(temp != NULL){
                    cout<<temp->categoria<<endl;
                    if(temp->abajo != NULL){
                        ListaArt* aux = temp->abajo;
                        aux->Bubble();
                        aux->DisplayART();
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void Display2(){
            this->Burbuja();
            if(this->cabeza == NULL){
                return;
            }else{
                Nodo_List_A* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->abajo != NULL){
                        ListaArt* aux = temp->abajo;
                        aux->Bubble();
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void Graph(){
            string dot = "digraph G{\n";
            dot = dot + "label=\"ListaListas\";\n";
            dot = dot + "node[shape=box];\n";

            Nodo_List_A* categ = this->cabeza;
            while(categ != NULL){
                if(categ->abajo != NULL){
                    ListaArt* temp = categ->abajo;
                    string nombrecat = categ->categoria;
                    //string idecategoria = "n1";
                    //cout<<temp->cabeza->id;
                    //string idecategoria = "n"+to_string(temp->cabeza->id);
                    dot = dot + temp->subgraph(nombrecat);
                     
                    free(temp);
                }
                categ = categ->siguiente;
            }
            Nodo_List_A* cate = cabeza;
            dot = dot + "{rank=same;\n";
            while(cate != NULL && cate->siguiente != NULL){
                dot = dot + cate->categoria + "->" + cate->siguiente->categoria + ";\n";
                
                cate = cate->siguiente;
            }

            dot = dot +  "}\n}";
            ofstream file;
            file.open("ListaListas.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg ListaListas.dot -o Images/ListaListas.svg"));

            

        }


};