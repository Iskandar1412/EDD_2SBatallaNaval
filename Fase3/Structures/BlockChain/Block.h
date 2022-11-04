#include <fstream>
#include <stddef.h>
#include <iostream>
#include <chrono>
#include <iomanip>
#include <ctime>
//#include <json/writer.h>
#include "../../Funciones/sha256.h"
 
using namespace std;
class Bloque{
    public:
        int ID;
        string Timestap;
        int Nonce;
        string PreHash;
        string RootMerkle;
        string Hash;
        SHA256* sha;
        Bloque(){
            this->ID = 0;
            this->Timestap = "";
            this->Nonce = 0;
            this->PreHash = "";
            this->RootMerkle = "";
            this->Hash = "";
        }

        string SetDataTime(){
            time_t t = time(nullptr);
            tm* now = localtime(&t);

            char buffer[128];
            strftime(buffer, sizeof(buffer), "%d:%m:%y::%X", now);
            return buffer;
        }

        void crearBloque(string MerkleRoot, int cantidadceros, string cerosStr){
            this->RootMerkle = MerkleRoot;
            bool flag = true;
            
            this->Timestap = this->SetDataTime();
            string cambiar_datos = to_string(this->ID) + this->Timestap + this->PreHash + this->RootMerkle;
            while(flag){
                string aux = (cambiar_datos + to_string(this->Nonce));
                this->Hash = sha->cifrar(aux);
                if(this->Hash.substr(0, cantidadceros) == cerosStr){
                    this->PreHash = this->Hash;
                    flag = false;
                }
                this->Nonce += 1;
            }
            this->ID += 1;
        }
};

class NodoBlock{
    public:
        int IDBlock;
        string Hash;
        int Nonce;
        string PreHash;
        string MerkleRoot;
        string data;
        string data_noajustado;
        string fecha;
        NodoBlock* siguiente;
        NodoBlock(int _IDBlock, int _Nonce, string _Hash, string _PreHash, string _MerkleRoot, string _data, string _fecha, string data_noajustado){
            this->IDBlock = _IDBlock;
            this->Nonce = _Nonce;
            this->Hash = _Hash;
            this->PreHash = _PreHash;
            this->MerkleRoot = _MerkleRoot;
            this->data_noajustado = data_noajustado;
            this->data = _data;
            this->fecha = _fecha;
            this->siguiente = NULL;
        }
};

class BlockChain{
    public:
        NodoBlock* raiz;
        NodoBlock* ultimo;
        Bloque* bloque;
        string previoushash;
        BlockChain(){
            this->previoushash = "";
            this->raiz = NULL;
            this->ultimo = NULL;
            this->bloque = new Bloque();
        }

        void insertar(string data, string merkleroot, int cantidadceros, string cerosStr, string data_sinarreglar){
            if(this->raiz == NULL){
                this->bloque->crearBloque(merkleroot, cantidadceros, cerosStr);
                this->previoushash = this->bloque->Hash;
                NodoBlock* temp = new NodoBlock(this->bloque->ID, this->bloque->Nonce, this->bloque->Hash, cerosStr, this->bloque->RootMerkle, data, this->bloque->Timestap, data_sinarreglar);
                this->raiz = temp;
                this->ultimo = temp;
            }else{
                this->bloque->crearBloque(merkleroot, cantidadceros, cerosStr);
                this->bloque->PreHash = this->previoushash;
                NodoBlock* temp = new NodoBlock(this->bloque->ID, this->bloque->Nonce, this->bloque->Hash, this->previoushash, this->bloque->RootMerkle, data, this->bloque->Timestap, data_sinarreglar);
                this->previoushash = this->bloque->PreHash;
                temp->PreHash = this->previoushash;
                this->previoushash = temp->Hash;
                this->ultimo->siguiente = temp;
                this->ultimo = temp;
            }
        }

        void recargarBloques(int id, string timestap, int nonce, string data, string prehash, string merkleroot, string hash, string data_sinarreglar){
            if(this->raiz == NULL){
                this->bloque->crearBloque("", 4, "0000");
                NodoBlock* temp = new NodoBlock(temp->IDBlock, nonce, hash, prehash, merkleroot, data, timestap, data_sinarreglar);
                temp->IDBlock = id;
                temp->fecha = timestap;
                temp->Nonce = nonce;
                temp->data = data;
                temp->PreHash = prehash;
                temp->MerkleRoot = merkleroot;
                temp->Hash = hash;
                this->raiz = temp;
                this->ultimo = temp;
            }else{
                this->bloque->crearBloque("", 4, "0000");
                this->bloque->PreHash = this->previoushash;
                NodoBlock* temp = new NodoBlock(temp->IDBlock, nonce, hash, prehash, merkleroot, data, timestap, data_sinarreglar);
                this->previoushash = prehash;
                temp->PreHash = prehash;
                temp->IDBlock = id;
                temp->fecha = timestap;
                temp->Nonce = nonce;
                temp->data = data;
                temp->PreHash = prehash;
                temp->MerkleRoot = merkleroot;
                temp->Hash = hash;
                this->ultimo->siguiente = temp;
                this->ultimo = temp;
            }
        }

        void toJson(){
            
            if(this->raiz == NULL){
                return;
            }else{
                NodoBlock* temp = this->raiz;
                while(temp != NULL){
                    string json = "";
                    json += "{\n\"INDEX\":"+to_string(temp->IDBlock)+",\n\"TIMESTAMP\":\""+temp->fecha+"\",\n\"NONCE\":"+to_string(temp->Nonce)+",\n\"DATA\":"+temp->data_noajustado+"\n\"PREVIOUSHASH\":\""+temp->PreHash+"\",\n\"ROOTMERKLE\":\""+temp->MerkleRoot+"\",\n\"HASH\":\""+temp->Hash+"\"\n}\n";
                    ofstream file;
                    file.open("Bloques/bloque"+to_string(temp->IDBlock)+".json");
                    file<<json;
                    file.close();
                    temp = temp->siguiente;
                }
                
            }
        }

        void graphosBlock(){
            string dot = "digraph G{\nbgcolor=none;\nrankdir=LR;\nlabel=\"\";\nnode[shape=box];\nnodesep=1;\n";
            dot += "node[fontname=\"Arial\", color=\"black\", fontcolor=\"gray\", style=\"filled\", margin=0.5];\nedge[color=\"red\"];\n";
            NodoBlock* temp = this->raiz;
            string nodes = "";
            string conexiones = "";
            int Nnode = 0;
            while(temp != NULL){
                nodes += "N" + to_string(Nnode) + "[label=\"ID: " + to_string(temp->IDBlock) + "\\nTIMESTAP: "+temp->fecha+"\\nNONCE: "+to_string(temp->Nonce)+"\\nDATA: "+temp->data+"\\nPREVIOUSHASH: "+temp->PreHash+"\\nROOTMERKLE: "+temp->MerkleRoot+"\\nHASH: "+temp->Hash+"\"];\n";
                if(temp->siguiente != NULL){
                    int aux = Nnode + 1;
                    conexiones += "N" + to_string(Nnode) + " -> N" + to_string(aux) + ";\n";
                }
                temp = temp->siguiente;
                Nnode += 1;
            }
            dot += "//Se agregan los nodos UsU\n";
            dot += nodes + "\n";
            dot += "//Se agregan conexiones UsU\n";
            dot += "\n" + conexiones + "\n}";
            ofstream file;
            file.open("Images/BlockChain.dot");
            //cout<<dot<<endl;
            file<<dot;
            file.close();
            system(("dot -Tsvg Images/BlockChain.dot -o Images/BlockChain.svg"));
        }
};