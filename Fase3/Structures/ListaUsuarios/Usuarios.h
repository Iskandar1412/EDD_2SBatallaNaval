#include <fstream>
#include <stddef.h>
#include <iostream>
#include <iomanip>
//incluir string
//#include ".././TreeB/BTree.h"
#include "../../Funciones/sha256.h"
//PARA INTERACTUAR CON LA ARBOL AVL Lista_Usuario
//Interactuarl con Lista 
using namespace std;

class Nodo_Carrito{
    public:
        int id;
        int idvalor;
        string categoria;
        int precio;
        string nombre;
        int cantidad;
        int numero_compra;
        string horafecha;
        Nodo_Carrito* siguiente;
        //Nodo_Carrito* anterior;
        Nodo_Carrito() = default;
        Nodo_Carrito(int id, string nombre, string categoria, int precio, int cantidad, string horafecha){
            this->idvalor = 0;
            this->id = id;
            this->numero_compra = 1;
            this->categoria = categoria;
            this->precio = precio;
            this->nombre = nombre;
            this->horafecha = horafecha;
            this->cantidad = cantidad;
            this->siguiente = NULL;
            //this->anterior = NULL;
        }
};

class Lista_Carrito{
    public:
        Nodo_Carrito* cabeza;
        //Nodo_Carrito* final;
        int valormasbajo;
        int longitud;
        int numerocompra = 1;
        Lista_Carrito(){
            this->valormasbajo = 0;
            this->longitud = 0;
            this->cabeza = NULL;
            //this->final = NULL;
        }

        void agregar_carro(int id, string nombre, string categoria, int precio, int cantidad, string horafecha){
            this->longitud += 1;
            Nodo_Carrito* nodo = new Nodo_Carrito(id, nombre, categoria, precio, cantidad, horafecha);
            nodo->idvalor = this->longitud;
            nodo->numero_compra = this->numerocompra;
            if(this->cabeza == NULL){
                this->cabeza = nodo;
            }else{
                Nodo_Carrito* puntero = this->cabeza;
                while(puntero->siguiente != NULL){
                    puntero = puntero->siguiente;
                }
                puntero->siguiente = nodo;
            }
        }

        void EliminarCarrito(int pos){
            if(this->cabeza == NULL){
                return;
            }else{
                
                if(pos == 1){
                    Nodo_Carrito* temp = this->cabeza;
                    this->cabeza = this->cabeza->siguiente;
                    temp->siguiente = NULL;
                    this->longitud -= 1;
                }else{
                    Nodo_Carrito* temp = this->cabeza;
                    int contador = 1;
                    while(contador < (pos - 1)){
                        temp = temp->siguiente;
                        contador += 1;
                    }
                    Nodo_Carrito* aux = temp->siguiente;
                    temp->siguiente = aux->siguiente;
                    aux->siguiente = NULL;
                    this->longitud -= 1;
                }
            }
        }

        void buscarEliminarCompra(int id, int id_uduario){
            if(this->cabeza == NULL){
                return;
            }else{
                Nodo_Carrito* temp = this->cabeza;
                int contador = 1;
                while(temp != NULL){
                    if(temp->id == (id - id_uduario) && temp->numero_compra == this->numerocompra){
                        this->EliminarCarrito(contador);
                        break;
                    }
                    contador += 1;
                    temp = temp->siguiente;
                }
            }
        }

        void cancelarCompra(){
            if(this->cabeza == NULL){
                return;
            }else{
                Nodo_Carrito* temp = this->cabeza;
                int contador = 1;
                while(temp != NULL){
                    if(temp->numero_compra == this->numerocompra){
                        int val = contador;
                        while(val <= this->longitud + 20){
                            this->EliminarCarrito(contador);
                            val+=1;
                        }
                        continue;
                    }
                    contador += 1;
                    temp = temp->siguiente;
                }
            }
        }

        void aumentarCompra(){
            this->numerocompra += 1;
        }

        void vaciarCarrito(){
            int val = 1;
            //cout<<this->longitud<<endl<<this->cabeza->idvalor<<endl;
            while(val <= this->longitud + 100){
                this->EliminarCarrito(1);
                val += 1;
            }
            //this->DisplayCarrito();
        }

        void DisplayCarrito(){
            if(this->cabeza == NULL){
                cout<<"lista vacia"<<endl;
            }else{
                Nodo_Carrito* temp = this->cabeza;
                cout<<setw(5)<<"ID"<<setw(20)<<"Nombre"<<setw(20)<<"Precio"<<endl<<setw(10)<<"Cantidad"<<endl<<endl;
                while(temp != NULL){
                    cout<<setw(5)<<temp->id<<setw(20)<<temp->nombre<<setw(20)<<temp->precio<<setw(10)<<temp->cantidad<<setw(30)<<temp->horafecha<<endl;
                    temp = temp->siguiente;
                }
            }
            cout<<endl;
        }

        string sub(string nombre){
            if(this->cabeza == NULL){
                return "";
            }else{
                string dot = "subgraph{\n";
                dot += "node[shape=box];\n";
                Nodo_Carrito* aux = this->cabeza;
                while(aux != NULL){
                    dot += "n"+to_string(aux->id)+"[label=\""+aux->nombre+"\"];\n";
                    aux = aux->siguiente;
                }
                Nodo_Carrito* temp = this->cabeza;
                while(temp != NULL && temp->siguiente != NULL){
                    dot += "n"+to_string(temp->id)+"->n"+to_string(temp->siguiente->id)+";\n";
                    temp = temp->siguiente;
                }
                dot = dot + nombre+"->n"+to_string(valormasbajo)+";\n}\n";
                return dot;
            }
        }

        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------

        void mover(Nodo_Carrito* inicio, Nodo_Carrito* final){
            int id = inicio->id;
            string categoria = inicio->categoria;
            int precio = inicio->precio;
            string nombre =inicio->nombre;
            inicio->id = final->id;
            inicio->categoria = final->categoria;
            inicio->precio = final->precio;
            inicio->nombre = final->nombre;
            final->id = id;
            final->categoria = categoria;
            final->precio = precio;
            final->nombre = nombre;
        }

        void Ordenar(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            Nodo_Carrito* temp = this->cabeza;
            while(task == true){
                task = false;
                while(temp != NULL && temp->siguiente != NULL){
                    if(temp->id > temp->siguiente->id){
                        this->mover(temp, temp->siguiente);
                        task = true;
                    }
                    temp = temp->siguiente;
                }
                temp = this->cabeza;
            }
            this->valormasbajo = this->cabeza->id;
        }

        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
        //---------------------------Ordenamiento---------------------------
};

class Nodo_ListaUsuario{
    public:
        //
        SHA256* sha;
        string nick;
        int id;
        string password;
        int edad;
        int monedas;
        int cantidad_jugadas;
        int cantidad_comprada;
        string WalletUSR;
        string LlaveWallet;
        string encrypt;
        Nodo_ListaUsuario* siguiente;
        Nodo_ListaUsuario* anterior;
        Lista_Carrito* carrito;
        //Lista_Carrito* Wallet;
        //AVLTree* ArbolAVL;
        Nodo_ListaUsuario(int id, string nick, string password, int edad, int monedas, string WalletUSR){
            this->id = id;
            this->nick = nick;
            this->password = password;
            this->edad = edad;
            this->cantidad_comprada = 1;
            this->monedas = monedas;
            this->WalletUSR = WalletUSR;
            this->LlaveWallet = "";
            this->cantidad_jugadas = 0;
            //this->ArbolAVL = new AVLTree();
            this->carrito = new Lista_Carrito();
            //this->Wallet = new Lista_Carrito();
            this->encrypt = sha->cifrar(password);
            this->siguiente = NULL;
            this->anterior = NULL;
        }
};

//Lista para usuario
class Lista_Usuario{//LISTA
    public:
        //
        //int valor;
        int contadorB;
        int contador_regresos;
        Nodo_ListaUsuario* cabeza;
        Nodo_ListaUsuario* final;
        bool jugador2llamado;
        bool secionIniciada;
        Nodo_ListaUsuario* usuario_secundario;
        Nodo_ListaUsuario* usuario_act;
        Lista_Usuario(){
            //this->valor = 0;
            this->contadorB = 0;
            this->contador_regresos = 0;
            this->cabeza = NULL;
            this->final = NULL;
            this->usuario_act = NULL;
            this->usuario_secundario = NULL;
            this->jugador2llamado = false;
            this->secionIniciada = false;
        }

        void add(int id, string nombre, string password, int edad, int monedas, string WalletUSR){
            //nodo->id = this->valor++;
            if(this->cabeza == NULL){
                Nodo_ListaUsuario* nodo = new Nodo_ListaUsuario(id, nombre, password, edad, monedas, WalletUSR);
                this->cabeza = nodo;
                this->final = nodo;
                return;
            }else{
                bool poderono = false;
                Nodo_ListaUsuario* temp = cabeza;
                while(temp  != NULL){
                    if(temp->id == id){
                        //cout<<"ID Existente :v"<<endl;
                        poderono = false;
                        break;
                    }else{
                        poderono = true;
                    }
                    temp = temp->siguiente;
                }
                if(poderono == true){
                    Nodo_ListaUsuario* nodo = new Nodo_ListaUsuario(id, nombre, password, edad, monedas, WalletUSR);
                    this->final->siguiente = nodo;
                    nodo->anterior = this->final;
                    this->final = nodo;
                }
                return;
            }
        }

        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------

        void Display(){
            //this->Bubble();
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                cout<<setw(10)<<"ID" <<setw(20)<<"Nombre" <<setw(80)<< "Contraseña" <<setw(10)<<"Edad"<<endl;
                cout<<endl;
                while(temp != NULL){
                    cout<<setw(10)<<temp->id<<setw(20)<<temp->nick<<setw(80)<<temp->encrypt<<setw(10)<<to_string(temp->edad)<<endl;
                    if(temp->carrito != NULL){
                        Lista_Carrito* aux = temp->carrito;
                        aux->Ordenar();
                        aux->DisplayCarrito();
                    }
                    temp = temp->siguiente; 
                }
            }
            cout<<endl;
        }

        void DisplayCarrito(){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->carrito->DisplayCarrito();
            }
        }

        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------
        //----------------------------Mostrar Todo---------------------------

        //------------------------Limpiaar Carro------------------------
        //------------------------Limpiaar Carro------------------------
        //------------------------Limpiaar Carro------------------------
        
        void LimpiarCarro(){
            if(this->usuario_act == NULL){
                return;
            }else{
                if(this->usuario_act->carrito->cabeza == NULL){
                    return;
                }else{
                    this->usuario_act->carrito->vaciarCarrito();
                }
            }
        }

        void eliminarprodDelCarro(int id){
            if(this->usuario_act == NULL){
                return;
            }else{
                if(this->usuario_act->carrito->cabeza == NULL){
                    return;
                }else{
                    this->usuario_act->carrito->buscarEliminarCompra(id, this->usuario_act->id);
                }
            }
        }

        //------------------------Limpiaar Carro------------------------
        //------------------------Limpiaar Carro------------------------
        //------------------------Limpiaar Carro------------------------

        //-------------------------Quitar Producto-------------------------
        //-------------------------Quitar Producto-------------------------
        //-------------------------Quitar Producto-------------------------
        //-------------------------Quitar Producto-------------------------

        void quitarProducto(int id_producto){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->carrito->buscarEliminarCompra(id_producto, this->usuario_act->id);
            }
        }

        //-------------------------Quitar Producto-------------------------
        //-------------------------Quitar Producto-------------------------
        //-------------------------Quitar Producto-------------------------
        //-------------------------Quitar Producto-------------------------

        //-------------------------Aumentar Compras----------------------
        //-------------------------Aumentar Compras----------------------
        //-------------------------Aumentar Compras----------------------

        void aumentarNumeroCompra(){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->carrito->aumentarCompra();
                this->usuario_act->cantidad_comprada += 1;
            }
        }


        //-------------------------Aumentar Compras----------------------
        //-------------------------Aumentar Compras----------------------
        //-------------------------Aumentar Compras----------------------

        //---------------------Agregando Wallet------------------------
        //---------------------Agregando Wallet------------------------
        //---------------------Agregando Wallet------------------------
        
        void AgregarWalletUsuario(string walletUsuario){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->WalletUSR = walletUsuario;
            }
        }

        void AgregarKeyWallet(string keywallet){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->LlaveWallet = keywallet;
            }
        }

        //---------------------Agregando Wallet------------------------
        //---------------------Agregando Wallet------------------------
        //---------------------Agregando Wallet------------------------

        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------

        void AgregarCompra(int id, string nombre, string categoria, int precio, int cantidad, string horafecha){
            if(this->usuario_act == NULL){
                return;
            }else{
                this->usuario_act->carrito->agregar_carro(id, nombre, categoria, precio, cantidad, horafecha);
                //this->usuario_act->ArbolAVL->add(Compra(id, nombre, cantidad));
                return;
            }
        }

        

        void RestandoMonedas(int precio, int cantidad){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas - (cantidad*precio);
            }
        }

        void RestandoPerCompra(int total){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas - total;
            }
        }

        void RestarporPerder(){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas - 50;
            }
        }

        void RestarJugador2porPerder(){
            if(this->usuario_secundario == NULL){
                return;
            }else{
                usuario_secundario->monedas = usuario_secundario->monedas - 50;
            }
        }

        void ModificarMonedasUsuario2(){
            if(this->usuario_secundario == NULL){
                return;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == usuario_secundario->nick && temp->password == usuario_secundario->password && temp->id == usuario_secundario->id){
                        temp->monedas = usuario_secundario->monedas;
                        break;
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void ModificarMonedas(){
            if(this->usuario_act == NULL){
                return;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == usuario_act->nick && temp->password == usuario_act->password && temp->id == usuario_act->id){
                        temp->monedas = usuario_act->monedas;
                        break;
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void GanarHundirjugador2(){
            if(this->usuario_secundario == NULL){
                return;
            }else{
                usuario_secundario->monedas = usuario_secundario->monedas + 20;
            }
        }

        void GanarPorHundir(){
            if(this->usuario_act == NULL){
                return;
            }else{
                usuario_act->monedas = usuario_act->monedas + 20;
            }
        }

        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        //------------------------Parte Monedas------------------------
        
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------

        void aumentarPartidasJugador2(){
            if(this->usuario_secundario == NULL){
                return;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == usuario_act->nick && temp->password == usuario_act->password && temp->id == usuario_act->id){
                        temp->cantidad_jugadas = temp->cantidad_jugadas + 1;
                        break;
                    }
                    temp = temp->siguiente;
                }
            }
        }

        void aumentarPartidasJugadas(){
            if(this->usuario_act == NULL){
                return;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == usuario_act->nick && temp->password == usuario_act->password && temp->id == usuario_act->id){
                        //usuario_act->cantidad_jugadas = usuario_act->cantidad_jugadas + 1;
                        temp->cantidad_jugadas = temp->cantidad_jugadas + 1;
                    }
                    temp = temp->siguiente;
                }
            }
        }

        int obtenerjugadasjugador2(){
            int cantidad;
            if(this->usuario_secundario == NULL){
                cout<<endl;
            }else{
                cantidad = usuario_secundario->cantidad_jugadas;
            }
            return cantidad;
        }

        int obtenercantidadjugadas(){
            int cantidad;
            if(this->usuario_act == NULL){
                cout<<endl;
            }else{
                cantidad = usuario_act->cantidad_jugadas;
            }
            return cantidad;
        }
        
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------
        //------------------------Parte Jugadas------------------------

        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------

        bool InicioSecion(string nick, string password){
            if(this->cabeza == NULL){
                return false;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->nick == nick && temp->password == password){
                        this->usuario_act = temp;
                        this->secionIniciada = true;
                        return true;
                        break;
                    }
                    temp = temp->siguiente;
                }
                this->secionIniciada = false;
                return false;
            }
        }

        bool LlamarJugador2(int id){
            if(this->cabeza == NULL){
                return false;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->id == id){
                        this->usuario_secundario = temp;
                        this->jugador2llamado = true;
                        //cout<<temp->id<<endl<<temp->nick<<endl<<temp->monedas<<endl;
                        return true;
                        break;
                    }
                    temp = temp->siguiente;
                }
                this->jugador2llamado = false;
                return false;
            }
        }
        
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------
        //------------------LLamadas a usuarios------------------

        void modificarUsuario(int id, string nick, string password, int edad, int money){
            SHA256* sha;
            if(this->cabeza == NULL){
                //cout<<"Lista Vacia"<<endl;
            }else{
                Nodo_ListaUsuario* temp = this->cabeza;
                while(temp != NULL){
                    if(temp->id == this->usuario_act->id && temp->nick == this->usuario_act->nick && temp->password == this->usuario_act->password){
                        this->usuario_act->id = id;
                        this->usuario_act->nick = nick;
                        this->usuario_act->password = password;
                        this->usuario_act->edad = edad;
                        this->usuario_act->monedas = money;
                        temp->id = id;
                        temp->nick = nick;
                        temp->password = password;
                        temp->edad = edad;
                        temp->monedas = money;
                        temp->encrypt = sha->cifrar(password);
                        break;
                    }
                    temp = temp->siguiente;
                    
                }
            }
        }

        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        
        void salirjugador2(){
            this->jugador2llamado = false;
            this->usuario_secundario = NULL;
        }

        void cerrarSecion(){
            this->secionIniciada = false;
            this->usuario_act = NULL;
            this->jugador2llamado = false;
            this->usuario_secundario = NULL;
        }

        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------
        //------------------Salida Jugadores------------------

        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        
        string nombrejugador2(){
            string nombre = "";
            if(this->usuario_secundario == NULL){
                cout<<endl;
            }else{
                nombre = this->usuario_secundario->nick;
            }
            return nombre;
        }

        string nombreUsuario(){
            string nombre = "";
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                nombre = this->usuario_act->nick;
            }
            return nombre;
        }

        int idUsuario2(){
            int idusuario = 0;
            if(this->usuario_secundario == NULL){
                cout<<endl;
            }else{
                idusuario = this->usuario_secundario->id;
            }
            return idusuario;
        }

        int idUsuario(){
            int idusuario = 0;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                idusuario = this->usuario_act->id;
            }
            return idusuario;
        }

        int edadUsuario(){
            int edad = 0;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingressado"<<endl;
            }else{
                edad = this->usuario_act->edad;
            }
            return edad;
        }

        int monedasjugador2(){
            int monedas;
            if(this->usuario_secundario == NULL){
                cout<<endl;
            }else{
                monedas = this->usuario_secundario->monedas;
                //cout<<monedas;
            }
            return monedas;
        }

        int monedasUsuario(){
            int monedas;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                monedas = this->usuario_act->monedas;
            }
            return monedas;
        }

        string passEncrypt(){
            string contrasenia;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                contrasenia = this->usuario_act->encrypt;
            }
            
            return contrasenia;
        }

        string passjugador2(){
            string contra;
            if(this->usuario_secundario == NULL){
                cout<<endl;
            }else{
                contra = this->usuario_secundario->password;
            }
            return contra;
        }

        string passUsuario(){
            string contrasenia;
            if(this->usuario_act == NULL){
                cout<<"Usuario NO Ingresado"<<endl;
            }else{
                contrasenia = this->usuario_act->password;
            }
            
            return contrasenia;
        }
        
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------
        //--------------------Regresiones--------------------

        void eliminarUsuario(int id){
            Nodo_ListaUsuario* temp = NULL;
            if(this->cabeza == NULL){
                cout<<"Lista Vacia"<<endl;
            }
            if(this->cabeza->id == id){
                temp = this->cabeza;
                this->cabeza = this->cabeza->siguiente;
                if(this->cabeza != NULL){
                    this->cabeza->anterior = NULL;
                }else{
                    this->final = NULL;
                }
                delete temp;
            }else if(this->final->id == id){
                temp = this->final;
                this->final = this->final->anterior;
                if(this->final != NULL){
                    this->final->siguiente = NULL;
                }else{
                    this->cabeza = NULL;
                }
                delete temp;
            }else{
                temp = this->cabeza;
                while(temp != NULL && temp->id != id){
                    temp = temp->siguiente;
                }
                if(temp == NULL){
                    cout<<"No se encontro"<<endl;
                }else{
                    temp->anterior->siguiente = temp->siguiente;
                    if(temp->siguiente != NULL){
                        temp->siguiente->anterior = temp->anterior;
                    }
                    delete temp;
                }
            }

        }

        void GraficarArbolUsuarioActivo(){
            if(this->usuario_act == NULL){
                return;
            }else{
                //this->usuario_act->ArbolAVL->GraphCU(this->usuario_act->nick);
                return;
            }
        }

        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------

        void mover(Nodo_ListaUsuario* inicio, Nodo_ListaUsuario* final){
            int ide = inicio->id;
            string nom = inicio->nick;
            string pas = inicio->password;
            int ed = inicio->edad;
            int mon = inicio->monedas;
            string wallusr = inicio->WalletUSR;
            Lista_Carrito* carrito = inicio->carrito;
            inicio->id = final->id;
            inicio->nick = final->nick;
            inicio->password = final->password;
            inicio->edad = final->edad;
            inicio->WalletUSR = final->WalletUSR;
            inicio->monedas = final->monedas;
            inicio->carrito = final->carrito;
            final->id = ide;
            final->nick = nom;
            final->password = pas;
            final->WalletUSR = wallusr;
            final->edad = ed;
            final->monedas = mon;
            final->carrito = carrito;
        }

        void Bubble(){
            if(this->cabeza == NULL){
                return;
            }
            bool task = true;
            Nodo_ListaUsuario* inicio = this->cabeza;
            while(task == true){
                //
                task = false;
                while(inicio != NULL && inicio->siguiente != NULL){
                    if(inicio->id > inicio->siguiente->id){
                        this->mover(inicio, inicio->siguiente);
                        task = true;
                    }
                    inicio = inicio->siguiente;
                }
                inicio = this->cabeza;
            }
        }

        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------
        //----------------------------Ordenamiento----------------------------

        void GrafoDoble(){
            Nodo_ListaUsuario *temp = this->cabeza;
            string dot = "digraph G{\nnode[shape=box];\nedge[dir=both];\nlabel=\"Lista de Usuarios\";\n";
            while(temp != NULL){
                dot += to_string(temp->id)+temp->nick+temp->password+"[label=\"Nombre: "+temp->nick+"\\nPassword: "+temp->encrypt+"\\nEdad: " + to_string(temp->edad) + +"\\nMonedas: " + to_string(temp->monedas) + "\"];\n";
                
                temp = temp->siguiente;
            }
            dot += "\n{rank=same\n";
            Nodo_ListaUsuario *aux = this->cabeza;
            
            while(aux->siguiente != NULL){
                dot += to_string(aux->id)+ aux->nick+aux->password+"->"+to_string(aux->siguiente->id)+aux->siguiente->nick+aux->siguiente->password+";\n";
                aux = aux->siguiente;
            }
            dot += this->cabeza->nick+this->cabeza->password+"->"+this->final->nick+this->final->password+";\n";
            dot += "}\n}\n";
            ofstream file;
            file.open("ListaCUCO.dot");
            file<<dot;
            file.close();
            system(("dot -Tsvg ListaCUCO.dot -o Images/ListaCUCO.svg"));
        }
};