#include <fstream>
#include <stddef.h>
#include <iostream>
using namespace std;

//TUTORIAL
class NodoCola{
    public:
        //
        int x, y;
        NodoCola* siguiente;
        NodoCola(int x, int y){
            this->x = x;
            this->y = y;
            this->siguiente = NULL;
        }
};

class Cola{
    public:
        //
        int m, alto;
        NodoCola* siguiente;
        NodoCola* cabeza;
        int Xcola;
        int Ycola;
        Cola(){
            this->m = 0;
            this->Xcola = 0;
            this->Ycola = 0;
            this->alto = 0;
            this->siguiente = NULL;
            this->cabeza = NULL;
        }

        void agregardim(int m){
            this->m = m;
        }

        void enque(int x, int y){
            //
            NodoCola* temp = new NodoCola(x, y);
            if(this->siguiente == NULL){
                this->cabeza = temp;
                this->siguiente = this->cabeza;
            }else{
                NodoCola* aux = this->siguiente;
                while(aux->siguiente != NULL){
                    aux = aux->siguiente;
                }
                aux->siguiente = temp;
            }
        }
        //destruir nodo.siguiente = NULL
        void dequeue(){
            if(this->siguiente){
                NodoCola* aux = this->cabeza;
                this->cabeza = this->siguiente->siguiente;
            }
        }

        int obtenerXcola(){
            int xcola = 0;
            if(this->siguiente != NULL){
                this->Xcola = this->siguiente->x;
                xcola = this->Xcola;
                return this->Xcola;
            }
            return xcola;
        }

        int obtenerYcola(){
            int ycola = 0;
            if(this->siguiente != NULL){
                this->Ycola = this->siguiente->y;
                ycola = this->Ycola;
                return this->Ycola;
            }
            return ycola;
        }

        void peek(){
            if(this->cabeza == NULL){
                return;
            }
            NodoCola* temp = this->cabeza;
            cout<<"Tutorial"<<endl;
            cout<<"      Tablero: "<<endl;
            cout<<"          m: " + to_string(this->m)<<endl;
            cout<<"      Movimientos: "<<endl;
            cout<<"          ";
            while(temp->siguiente != NULL){
                cout<<"("+to_string(temp->x)+", "+to_string(temp->y)+") -> ";
                temp = temp->siguiente;
            }
            cout<<"("+to_string(temp->x)+", "+to_string(temp->y)+")";
            cout<<endl;
        }

        void GraphoCola(){
            NodoCola* temp = this->cabeza;
            string dot = "digraph G{\nnode[shape=record];\nlabel=\"Tutorial (Cola de Movimientos)\"\n";
            int i = 0;
            dot += "struct[shape=record, label=\"";
            while(temp->siguiente != NULL){
                dot +=  "<f"+to_string(i)+">X: "+to_string(temp->x)+"\\n\\Y: "+to_string(temp->y)+"|";
                i++;
                temp = temp->siguiente;
            }
            dot +=  "<f"+to_string(i)+">X: "+to_string(temp->x)+"\\n\\Y: "+to_string(temp->y)+"\"];\n";
            dot += "}\n";
            ofstream file;
            file.open("ColaTutorial.dot");
            file<<dot;
            file.close();
            system(("dot -Tpng ColaTutorial.dot -o ColaTutorial.png"));
            //cout<<dot<<endl;
        }
};
