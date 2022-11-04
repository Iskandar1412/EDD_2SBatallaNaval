#include <fstream>
#include <stddef.h>
#include <iostream>
#include <iomanip>
#include <vector>

//incluir string
#include "../../Funciones/sha256.h"

using namespace std;

class Hashi{
    public:
        int m;
        int n;
        int min;
        int max;
        vector<int>ides;
        //int ides[13];
        vector<string>values;
        
        Hashi(){
            this->m = 13;
            this->n = 0;
            this->min = 20;
            this->max = 80;
            this->values;
            this->ides;
            this->Llenar();
        }

        int division(int k){
            return (k % this->m);
        }

        int linear(int k){
            return ((k + 1) % this->m);
        }

        void Llenar(){
            this->n = 0;
            this->ides[this->m];
            this->values[this->m];
            for(int i = 0; i < m; i++){
                //this->ides[i] = -1;
                this->ides.push_back(-1);
                this->values.push_back("");
            }
        }

        void limpiar(){
            vector<int>val;
            vector<string>statu;
            this->ides = val;
            this->values = statu;
            this->m = 13;
            this->Llenar();
        }

        void insert(int id, string nombre){
            int i = this->division(i);
            while(this->ides[i] != -1){
                i = this->linear(i);
            }
            this->ides[i] = id;
            this->values[i] = nombre;
            this->n++;
            this->rehashing();
        }

        void rehashing(){
            if((this->n * 100 / this->m) >= this->max){
                //int temp[this->m];
                //string temp2[this->m];
                vector<int>valint = this->ides;
                vector<string>valu = this->values;
                vector<int>vaciarint;
                vector<string>vaciarstr;
                this->ides = vaciarint;
                this->values = vaciarstr;
                //for(int i = 0; i < this->m; i++){
                //    temp[i] = this->ides[i];
                //    temp2[i] = this->values[i];
                //}
                int mprev = this->m;
                this->m = this->n * 100  / this->min;
                this->Llenar();
                for(int i = 0; i < mprev; i++){
                    if(valint[i] != -1){
                        this->insert(valint[i], valu[i]);
                    }
                }
            }else{
                //this->Mostrar();
                int s = 0;
            }
        }

        void Mostrar(){
            cout<<"[";
            for(int i = 0; i < this->m; i++){
                cout<<" ("+to_string(i) + ") " + to_string(this->ides[i]) + " - " +this->values[i];
            }
            cout<<"]" + to_string(this->n*100/this->m) + "%"<<endl;
        }

        void grapho(){
            string dot = "digraph G{\n\tgraph[ratio=fill];\n";
            dot += "\tnode[label=\"\", fontsize=15, shape=plaintext, fontcolor=\"blue\"];\n";
            dot += "\tarset [label=<\n\t\t<TABLE>\n\t\t\t<TR>\n";
            dot += "\t\t\t\t<TD><b>INDICE</b></TD>\n\t\t\t\t<TD><b>ID</b></TD>\n\t\t\t\t<TD><b>NOMBRE</b></TD>\n\t\t\t</TR>";
            for(int i = 0; i < this->m; i++){
                if(this->ides[i] != -1){
                    dot += "\n\t\t\t<TR>\n\t\t\t\t<TD>"+to_string(i)+"</TD>\n\t\t\t\t<TD>"+to_string(this->ides[i])+"</TD>\n\t\t\t\t<TD>"+this->values[i]+"</TD>\n\t\t\t</TR>";
                }
            }
            dot += "\n\t\t</TABLE>>, color=\"gray\"];\n}";
            //cout<<dot<<endl;
            ofstream file;
            file.open("Images/Hash.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg Images/Hash.dot -o Images/Hash.svg"));
            
        }
};