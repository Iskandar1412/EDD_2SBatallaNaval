#include <stddef.h>
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
        int ancho, alto;
        NodoCola* siguiente;
        NodoCola* cabeza;
        Cola(){
            this->ancho = 0;
            this->alto = 0;
            this->siguiente = NULL;
            this->cabeza = NULL;
        }

        void agregardim(int ancho, int alto){
            this->ancho = ancho;
            this->alto = alto;
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

        void dequeue(){
            if(this->siguiente != NULL){
                this->siguiente = this->siguiente->siguiente;
            }
        }

        void peek(){
            if(this->cabeza == NULL){
                return;
            }
            NodoCola* temp = this->cabeza;
            cout<<"Tutorial"<<endl;
            cout<<"      Tablero: "<<endl;
            cout<<"          Ancho: " + to_string(this->ancho)<<endl;
            cout<<"          Alto:  " + to_string(this->alto)<<endl;
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
            system(("dot -Tsvg ColaTutorial.dot -o Images/ColaTutorial.svg"));
            //cout<<dot<<endl;
        }
};
