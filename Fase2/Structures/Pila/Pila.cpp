//lista de pilas

#include <fstream>
#include <iterator>
#include <iomanip>
#include <iostream>

using namespace std;

class NodoPila{
    public:
        //
        int id;
        int x;
        int y;
        NodoPila* abajo;
        NodoPila(int x, int y){
            this->x = x;
            this->y = y;
            this->abajo = NULL;
        }
};


class Pila{
    public:
        //
        int longitudpila;
        NodoPila* cima;
        Pila(){
            this->longitudpila = 0;
            this->cima = NULL;
        }
        void push(int x, int y){
            NodoPila* temp = new NodoPila(x, y);
            temp->id = 0;
            temp->abajo = this->cima;
            this->cima = temp;
        }
        void pop(){
            NodoPila* temp = this->cima;
            this->cima = NULL;
            this->cima = temp->abajo;
            temp = NULL;
        }
        void peek(){
            NodoPila* temp = this->cima;
            while(temp != NULL){
                cout<<to_string(temp->id)+"- " + to_string(temp->x) + ", " + to_string(temp->y)<<endl;
                temp = temp->abajo;
            }
        }

};


class NodoListaP{
    public:
        //
        int id;
        string nombre;
        NodoListaP* siguiente;
        Pila* abajo;
        Pila* retroceso;
        NodoListaP(string nombre){
            this->id = 0;
            this->nombre = nombre;
            this->siguiente = NULL;
            this->abajo = new Pila();
            this->retroceso = new Pila();
        }
        
};

class ListaPila{
    public:
        //
        NodoListaP* inicio;
        int longitud;
        bool transaccion_exitosa;
        ListaPila(){
            this->longitud = 0;
            this->transaccion_exitosa = false;
            this->inicio = NULL;
        }
        void insertar(string nombre){//por si piden que  se ingrese una lista de igual nombre hacer que no deje
            if(this->inicio == NULL){
                NodoListaP* lista = new NodoListaP(nombre);
                this->longitud++;
                lista->id  = this->longitud;
                int op;
                cout<<"cantidad de movimientos: ";
                cin>>op;
                lista->retroceso->longitudpila = op;
                for(int i = 0; i < op; i++){
                    int k, l;
                    cout<<"x: ";
                    cin>>k;
                    cout<<"y: ";
                    cin>>l;
                    lista->retroceso->push(k, l);
                    lista->abajo->push(k, l);
                    lista->retroceso->cima->id = i;
                    lista->abajo->cima->id = i;
                }
                
                lista->siguiente = this->inicio;
                this->transaccion_exitosa = true;
                this->inicio = lista;
            }else{
                bool poderono = false;
                NodoListaP* cabeza = inicio;
                while(cabeza != NULL){
                    if(cabeza->nombre == nombre){
                        cout<<"LISTA YA EXISTENTE"<<endl;
                        this->transaccion_exitosa = false;
                        poderono = false;
                        break;
                    }else{
                        poderono = true;
                    }
                    cabeza = cabeza->siguiente;
                }
                if(poderono == true){
                    NodoListaP* lista = new NodoListaP(nombre);
                    this->longitud++;
                    lista->id = this->longitud;
                    int op;
                    cout<<"cantidad de movimientos: ";
                    cin>>op;
                    lista->retroceso->longitudpila = op;
                    for(int i = 0; i < op; i++){
                        int k, l;
                        cout<<"x: ";
                        cin>>k;
                        cout<<"y: ";
                        cin>>l;
                        lista->retroceso->push(k, l);
                        lista->abajo->push(k, l);
                        lista->retroceso->cima->id = i;
                        lista->abajo->cima->id = i;
                    }
                    lista->siguiente = this->inicio;
                    this->transaccion_exitosa = true;
                    this->inicio = lista;
                    poderono = false;
                    return;
                }
                
                
            }
            
        }

        void eliminardePila(string nombre){
            if(this->inicio == NULL){
                return;
            }
            NodoListaP* lista = this->inicio;
            while(lista != NULL){
                if(lista->nombre == nombre){
                    if(lista->abajo != NULL){
                        Pila* temp = lista->abajo;
                        temp->pop();
                        break;
                    }
                }
                lista = lista->siguiente;
            }
        }

        void mostrar(){
            if(this->inicio == NULL){
                return;
            }
            NodoListaP* temp = this->inicio;
            while(temp != NULL){
                cout<<"Nombre Movimiento: "+temp->nombre<<endl;
                cout<<"Movimientos: "<<endl;
                if(temp->abajo != NULL){
                    Pila* aux = temp->abajo;
                    aux->peek();
                }
                temp = temp->siguiente;
            }
        }

        void MostrarSoloNMovimientos(){
            if(this->inicio != NULL){
                return;
            }
            int i = 0;
            NodoListaP* temp = this->inicio;
            while(temp != NULL){
                cout<<to_string(i) + "- Nombre Movimiento: "+temp->nombre + "; ";
                i++;
                temp = temp->siguiente;
            }
        }

        string subgraph(NodoListaP* aux){
            string valor = "subgraph{\n";
            valor += "\tnode[shape=plaintext];\n";
            valor += "\tn"+to_string(aux->id)+"_sub[label=<\n";
            valor += "\t<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">\n";
            valor += "\t<TR><TD bgcolor=\"gray\">Movement</TD></TR>\n";
            NodoPila* templar = aux->abajo->cima;
            while(templar != NULL){
                valor += "\t<TR><TD>("+to_string(templar->x)+", "+ to_string(templar->y)+")</TD></TR>\n";
                templar = templar->abajo;
            }
            valor += "\t</TABLE>>];\n";
            valor += "n" + to_string(aux->id) + "->n" + to_string(aux->id)+"_sub}\n";
            return valor;
        }

        void Grapho(){
            if(this->inicio == NULL){
                return;
            }
            string dot = "digraph G{\nlabel=\"Lista de Pilas\";\nnode[shape=box];\n";

            NodoListaP* temp = this->inicio;
            while(temp != NULL){
                dot += "n" + to_string(temp->id) + "[label=\""+temp->nombre+"\"];\n";
                
                if(temp->abajo != NULL){
                    NodoListaP* aux = temp;
                    dot += subgraph(aux);
                    
                }
                temp = temp->siguiente;
            }
            NodoListaP* auxiliar = this->inicio;
            dot += "{rank=same;\n";
            while(auxiliar->siguiente != NULL){
                dot += "n" + to_string(auxiliar->id) + "->n" + to_string(auxiliar->siguiente->id) + ";\n";
                auxiliar = auxiliar->siguiente;
            }
            dot += "}\n}\n";
            ofstream file;
            file.open("ListaPila.dot");
            file<<dot;
            file.close();
            system("dot -Tsvg ListaPila.dot -o Images/ListaPila.svg");
            //cout<<dot<<endl;
        }

        string subreg(NodoListaP* aux){
            string valor = "";
            for(int i = 0; i < aux->retroceso->longitudpila; i++){
                NodoPila* temp = aux->retroceso->cima;
                valor += "subgraph{\nnode[shape=plaintext];\n";
                valor += "n"+to_string(i)+"_sub[label=<\n";
                valor += "<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">\n";
                valor += "<TR><TD bgcolor=\"gray\">Regresion "+ to_string(i)+"</TD></TR>\n";
                while(temp != NULL){
                    valor += "<TR><TD>("+to_string(temp->x) + ", "+to_string(temp->y)+")</TD></TR>\n";
                    temp = temp->abajo;
                }
                valor += "</TABLE>>];\n\n";
                valor += "}\n";
                aux->retroceso->pop();
            }
            valor += "{rank=same;\n";
            for(int i = 0; i < aux->retroceso->longitudpila - 1; i++){
                valor += "n"+ to_string(i) + "_sub->n"+ to_string(i+1)+"_sub;\n";
            }
            
            return valor;
        }

        void Regresion(string nombre){
            if(this->inicio == NULL){
                return;
            }
            string dot = "digraph G{\n\n";
            NodoListaP* temp = this->inicio;
            while(temp != NULL){
                if(temp->nombre == nombre){
                    //cout<<"aquieesta"<<endl;
                    dot += "label=\"("+nombre+") Pila Regresion\";\n";
                    dot += subreg(temp);
                    dot += "}\n";
                    
                }
                temp = temp->siguiente;
            }
            dot += "\n}\n";
            ofstream file;
            file.open("Regresion.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg Regresion.dot -o Images/Regresion.svg"));        
        }


};



