#include <fstream>
#include <stddef.h>
#include <math.h>
#include <iostream>
#include <iomanip>
#include "../../Funciones/sha256.h"
using namespace std;

class DataNode{
    public:
        string value;
        DataNode(string value){
            this->value = value;
        }
};

class HashNode{
    public:
        string hash;
        string value;
        HashNode* left;
        HashNode* right;
        HashNode(string hash){
            this->hash = hash;
            this->value = "";
            this->left = NULL;
            this->right = NULL;
        }
};

class Merkle{
    public:
        HashNode* tophash;
        int index;
        vector<string>datablock;
        SHA256 sha;
        Merkle(){
            this->tophash = NULL;
            this->index = 0;
            this->datablock;
        }

        void add(string value){
            this->datablock.push_back(value);
        }

        void createTree(int exp){
            //this->tophash = new HashNode(0);
            this->tophash = new HashNode("0");
            this->_createTree(this->tophash, exp);
        }

        void _createTree(HashNode* temp, int exp){
            if(exp > 0){
                temp->left = new HashNode("0");
                temp->right = new HashNode("0");
                this->_createTree(temp->left, exp - 1);
                this->_createTree(temp->right, exp - 1);
            }
        }

        void genhash(HashNode* temp, int exp){
                //cout<<this->datablock[0];
            if(temp != NULL){
                this->genhash(temp->left, exp);
                this->genhash(temp->right, exp);
                if(temp->left == NULL && temp->right == NULL){
                    temp->value = this->datablock[exp - (this->index--)];
                    temp->hash = sha.cifrar(temp->value);
                }else{
                    temp->hash = sha.cifrar(temp->left->hash+temp->right->hash);
                }
            }
        }

        void preorder(HashNode* temp){
            this->preorder(temp->left);
            this->preorder(temp->right);
        }

        void auth(){
            int exp = 1;
            while(pow(2,exp) < this->datablock.size()){
                exp += 1;
            }
            //cout<<exp<<endl;
            for(int i = this->datablock.size(); i < pow(2, exp); i++){
                this->datablock.push_back(to_string(i));
            }
            this->index = pow(2, exp);
            this->createTree(exp);
            this->genhash(this->tophash, pow(2, exp));
            //cout<<"HOLACOMO"+this->tophash->hash<<endl;
            //this->preorder(this->tophash);
        }

        string ramas_dot(HashNode* nodo){
            string dot = "";
            if((nodo->left == NULL) && (nodo->right == NULL)){
                dot += "N" + nodo->hash + "[label=\""+nodo->hash+"\"];\n";
                if(nodo->value != ""){
                    dot += "N" + nodo->hash + nodo->value + "[label=\""+nodo->value+"\"];\n";
                    dot += "N" + nodo->hash + " -> N" + nodo->hash + nodo->value + ";\n";
                }
            }else{
                dot += "N" + nodo->hash + "[label = \""+nodo->hash+"\"];\n";
            }if(nodo->left != NULL){
                dot += ramas_dot(nodo->left) + "N" + nodo->hash + ":C0 -> N" + nodo->left->hash +";\n";
            }if(nodo->right != NULL){
                dot += ramas_dot(nodo->right) + "N" + nodo->hash + ":C1 -> N" + nodo->right->hash + ";\n";
            }
            return dot;
        }

        void dotget(){
            //string dot = "digraph G{\nnode[shape=box];\n";
            //HashNode* temp = this->tophash;
            string dot = "";
            dot += "digraph G{\nlabel=\"\";\nfontname=\"Arial Black\";\nfontsize=\"15pt\";\nnode[shape=box, style=filled, fillcolor=black, fontcolor=white];\n" + this->ramas_dot(this->tophash) + "\n}";
            //cout<<"tophash: " + this->tophash->hash<<endl;
            //cout<<dot<<endl;
            ofstream file;
            file.open("Images/Merkle.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg Images/Merkle.dot -o Images/Merkle.svg"));
            
        }

        void eliminar(){
            vector<string>data;
            this->datablock = data;
            this->tophash->right = NULL;
            this->tophash->left = NULL;
            this->tophash = NULL;
            delete(tophash);
            //cout<<this->datablock.size()<<endl;
        }

};

