//para memorizar
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <iterator>
#include <algorithm>
#include <set>
//agregar las listas (faltan)
#include "./Structures/./DoubleLinked/./DoubleLinkedList.cpp"
#include "./Funciones/./json_parsing.h"
#include "./Funciones/./json_parsing.cpp"
#include "./json/./json.h"
//#include "./Structures/./ListL/./LinkedList.cpp"
//#include "./Structures/./ListL/./SLinkedList.cpp"
//#include "./Structures/./ListOfList/./List.h"
//para no sufrir con el agregar 
#include "./Structures/./ListL/./ListaListas.cpp"
#include "./Structures/./Pila/./Pila.cpp"
#include "./Structures/./Cola/./Cola.cpp"
//#include "./Structures/./Pila/./Pila.cpp"
using namespace std;
//Articulo* arti;
NodoDobleL* usuarioactivo = NULL;
DobleL* ListaUsuarios = new DobleL();
Cola* NuevoTutorial = new Cola();
SoloArt* acomprar = NULL;
ListaPila* Movimientos = new ListaPila();



void CargaMasiva(){
    //
    string ruta = "Pruevas.json";
    ifstream file(ruta);//ruta
    Json::Value obtenerarchivo;
    Json::Reader lector;

    lector.parse(file, obtenerarchivo);
    
    const Json::Value usuarios = obtenerarchivo["usuarios"];
    for(int i = 0; i < usuarios.size(); i++){
        //cout<<to_string(usuarios[i]["monedas"].asInt())<<endl;
        string nombreus = usuarios[i]["nick"].asString();
        string passus = usuarios[i]["password"].asString();
        int money = usuarios[i]["monedas"].asInt();
        //int money = atoi(tmoney.c_str());
        int edad = usuarios[i]["edad"].asInt();
        //int edad = atoi(tedad.c_str());
        ListaUsuarios->Insertar(nombreus, passus, edad, money);
    }
    const Json::Value articulos = obtenerarchivo["articulos"];
    for(int i = 0; i < articulos.size(); i++){
        string categoria = articulos[i]["categoria"].asString();
        AgregarCategoria(categoria);
    }
    Ajustar();
    for(int i = 0; i < articulos.size(); i++){
        int id = articulos[i]["id"].asInt();
        //int id = atoi(tid.c_str());
        string categoria = articulos[i]["categoria"].asString();
        int precio = articulos[i]["precio"].asInt();
        //int precio = atoi(tprecio.c_str());
        string nombre = articulos[i]["nombre"].asString();
        string src = articulos[i]["src"].asString();
        ListadoArticulos(id, categoria, precio, nombre, src);
    }
    const Json::Value TutorialPoint = obtenerarchivo["tutorial"];
    int ancho = TutorialPoint["ancho"].asInt();
    //int ancho = atoi(tancho.c_str());
    int alto = TutorialPoint["alto"].asInt();
    //int alto = atoi(talto.c_str());
    NuevoTutorial->agregardim(ancho, alto);
    const Json::Value Movements = TutorialPoint["movimientos"];
    for(int i = 0; i < Movements.size(); i++){
        int xval = Movements[i]["x"].asInt();
        //int xval = atoi(valx.c_str());
        int yval = Movements[i]["y"].asInt();
        //int yval = atoi(valy.c_str());
        NuevoTutorial->enque(xval, yval);
    }
    
    cout<<"Archivo Cargado con Exito"<<endl;

    
};

void Reportes(){
    //
};


void MenuInicio(){
    while(usuarioactivo != NULL){
        cout<<"************* BATTLESHIP *************"<<endl;
        cout<<"    MENU - "+ usuarioactivo->nick + "  -  Monedas: " + to_string(usuarioactivo->monedas)  <<endl;
        cout<<"-*                                  *-"<<endl;
        cout<<"B*  1. Editar Informacion           *B"<<endl;
        cout<<"A*  2. Eliminar Cuenta              *A"<<endl;
        cout<<"T*  3. Ver Tutorial                 *T"<<endl;
        cout<<"T*  4. Ver Articulos de Tienda      *T"<<endl;
        cout<<"L*  5. Realizar Movimientos         *L"<<endl;        
        cout<<"E*  6. Cerrar Secion                *E"<<endl;        
        cout<<"-*                                  *-"<<endl;
        cout<<"**************************************"<<endl;
        cout<<"************* BATTLESHIP *************"<<endl;
        int op, n;
        cout<<"opción a elegir: ";
        cin>>op;
        if(op == 1){//MODIFICACION USUARIO
            cout<<endl;
            cout<<"***---------->MODIFICACION USUARIO<----------***"<<endl;
            cout<<endl;
            cout<<"    " + usuarioactivo->nick + "      Monedas: " + to_string(usuarioactivo->monedas)<<endl;
            cout<<endl;
            string nombre, nombrenuevo, passnueva, pass;
            int edad, money;
            nombre = usuarioactivo->nick;
            pass = usuarioactivo->password;
            cout<<"Ingrese Nuevo Nombre: ";
            cin>>nombrenuevo;
            cout<<"Ingrese Nueva Contraseña: ";
            cin>>passnueva;
            cout<<"Ingrese Nueva Edad: ";
            cin>>edad;
            cout<<"Ingrese Cantidad de Monedas: ";
            cin>>money;
            ListaUsuarios->modificarUsuario(nombre, nombrenuevo, pass, passnueva, edad, money);
            usuarioactivo->edad = edad;
            usuarioactivo->nick = nombrenuevo;
            usuarioactivo->monedas = money;
            usuarioactivo->password = passnueva;
            cout<<endl;
            cout<<"USUARIO MODIFICADO BV"<<endl;
            cout<<endl;
            
        }else if(op == 2){//ELIMINACION USUARIO (CUENTA)
            //
            int op;
            cout<<"***---------->ELIMINACION USUARIO<----------***"<<endl;
            cout<<"(tomar en cuenta que no se recuperaran sus datos)"<<endl;
            cout<<"¿Desea Eliminar su Cuenta?: 1(SI) 2(NO): ";
            cin>>op;
            if(op == 1){
                string nombre = usuarioactivo->nick;
                ListaUsuarios->eliminarUsuario(nombre);
                cout<<"Usuario Eliminado / Volviendo al Menu Principal"<<endl;
                usuarioactivo = NULL;
            }
            cout<<endl;
        }else if(op == 3){//VER TUTORIAL
            //
            cout<<endl;
            cout<<"***---------------->TUTORIA<----------------***"<<endl;
            cout<<endl;
            NuevoTutorial->peek();
            cout<<endl;
        }else if(op == 4){//VER ARTICULOS DE TIENDA
            //
            cout<<endl;
            cout<<"***---------->TIENDA DE ARTICULOS<----------***"<<endl;
            cout<<endl;
            cout<<"    " + usuarioactivo->nick + "      Monedas: " + to_string(usuarioactivo->monedas)<<endl;
            cout<<endl;
            MostrarCategorias();
            int id, cant;
            cout<<"Objeto a comprar (ID): ";
            cin>>id;
            SoloArt* temporal;
            temporal = obtenercomprar(id);
            if(temporal != NULL){
                if(usuarioactivo->monedas < temporal->precio){
                    cout<<"No se puede comprar"<<endl;
                }else{
                    cout<<"Objeto a Comprar: " +temporal->nombre + " $" +to_string(temporal->precio) + " - Monedas: $" +to_string(usuarioactivo->monedas)+"-"+to_string(temporal->precio)+" = " +to_string(usuarioactivo->monedas-temporal->precio) <<endl;
                    usuarioactivo->monedas = usuarioactivo->monedas - temporal->precio;
                    cout<<endl;
                }
            }

        }else if(op == 5){//REALIZAR MOVIMIENTOS
            cout<<endl;
            cout<<"***------->REALIZACION DE MOVIMIENTOS<-------***"<<endl;
            cout<<endl;
            cout<<"    " + usuarioactivo->nick + "      Monedas: " + to_string(usuarioactivo->monedas)<<endl;
            cout<<endl;
            string nombrelistado;
            cout<<"Ingresar nombre para guardar la lista de movimientos (Sin Espacios): ";
            cin>>nombrelistado;
            Movimientos->insertar(nombrelistado);
            cout<<endl;
            if(Movimientos->transaccion_exitosa == true){
                cout<<"Monedas por creacion de movimientos: "+ to_string(usuarioactivo->monedas) + " + 10 = " + to_string(usuarioactivo->monedas + 10)<<endl;
                usuarioactivo->monedas = usuarioactivo->monedas+10;
            }
            cout<<endl;
            Movimientos->mostrar();
            cout<<endl;
        }else if(op == 6){//SALIR A MENU PRINCIPAL
            cout<<endl;
            string nombre, password;
            int edad, monedas;
            nombre = usuarioactivo->nick;
            password = usuarioactivo->password;
            edad = usuarioactivo->edad;
            monedas = usuarioactivo->monedas;
            ListaUsuarios->modificarUsuario(nombre, nombre, password, password, edad, monedas);
            cout<<"Adios " + usuarioactivo->nick + " (:'v )"<<endl;
            cout<<endl;
            usuarioactivo = NULL;
        }else{
            return;
        }
    }
};



int main(int argc, char** argv){
    /*
    AgregarCategoria("Legendario");
    AgregarCategoria("Legendario");
    AgregarCategoria("Normal");
    AgregarCategoria("Normal");
    AgregarCategoria("Legendario");
    AgregarCategoria("Epico");
    AgregarCategoria("Epico");
    AgregarCategoria("Normal");
    AgregarCategoria("Barbaro");
    AgregarCategoria("Comun");
    AgregarCategoria("Normal");
    AgregarCategoria("Normal");
    AgregarCategoria("Barbaro");
    AgregarCategoria("Barbaro");
    AgregarCategoria("Barbaro");
    Ajustar();
    */
    
    while(true){
        
        cout<<"********* BATTLESHIP *********"<<endl;
        cout<<"************ MENU ************"<<endl;
        cout<<"B*                          *-"<<endl;
        cout<<"A*  1. Carga Masiva         *B"<<endl;
        cout<<"T*  2. Registrar Usuario    *A"<<endl;
        cout<<"T*  3. Login                *T"<<endl;
        cout<<"L*  4. Reportes             *T"<<endl;
        cout<<"E*  5. Salir                *L"<<endl;        
        cout<<"E*  6. Mostrar Todo         *L"<<endl;        
        cout<<"-*                          *E"<<endl;
        cout<<"******************************"<<endl;
        cout<<"********* BATTLESHIP *********"<<endl;
        int op, n;
        cout<<"opción a elegir: ";
        cin>>op;
        if(op == 1){
            //CARGA MASIVA
            cout<<endl;
            cout<<"***-------->CARGA MASIVA DE ARCHIVO<--------***"<<endl;
            CargaMasiva();
            cout<<endl;
        }else if(op == 2){
            //REGISTRAR USUARIO
            cout<<endl;
            cout<<"***------->REGISTRO DE USUARIO NUEVO<-------***"<<endl;
            string nick, pass;
            int monedas, edad;
            cout<<"Ingrese Nombre: ";
            cin>>nick;
            cout<<"Password: ";
            cin>>pass;
            cout<<"Ingrese Cantidad (Monedas): ";
            cin>>monedas;
            cout<<"Ingrese Edad: ";
            cin>>edad;
            ListaUsuarios->Insertar(nick, pass, edad, monedas);
            cout<<endl;
            cout<<"USUARIO INGRESADO CORRECTAMENTE"<<endl;
            cout<<endl;
            
        }else if(op == 3){
            //LOGIN
            cout<<endl;
            cout<<"***------------>INICIAR SECION<------------***"<<endl;
            string nick, pass;
            cout<<"Ingrese Nombre: ";
            cin>>nick;
            cout<<"Password: ";
            cin>>pass;
            NodoDobleL* confirmacion = ListaUsuarios->InicioSecion(nick, pass);
            if(confirmacion != NULL){
                usuarioactivo = confirmacion;
                cout<<"Bienvenido: " + confirmacion->nick + " :D"<<endl;
                MenuInicio();
                cout<<endl;
            }
            
        }else if(op == 4){
            //REPORTES
            ListaUsuarios->Bubble();
            Ajustar();

            cout<<endl;
            cout<<"***---------->GENERACION REPORTES<----------***"<<endl;
            cout<<endl;
            string nombreparapila;
            Movimientos->mostrar();
            cout<<"Ingrese nombre para generar regresion de pila: ";
            cin>>nombreparapila;
            cout<<endl;
            cout<<"Graficando Regresion de " + nombreparapila<<endl;
            Movimientos->Regresion(nombreparapila);//Grafica para tutorial
            cout<<"Graficando Tutorial (Cola)"<<endl;
            NuevoTutorial->GraphoCola();//Grafica para tutorial
            cout<<"Graficando Articulos (Lista de Listas)"<<endl;
            Grafo();//Grafica para Listade Listas
            cout<<"Graficando Usuarios (C. Double Linked List)"<<endl;
            ListaUsuarios->GrafoDoble();//Grafica para Usuarios
            cout<<"Graficando Lista de Movimientos (Lista de Pilas)"<<endl;
            Movimientos->Grapho();//Grafica Lista de Pilas
            
        }else if(op == 5){
            //SALIR
            cout<<endl;
            cout<<"***----------->SALIR DEL PROGRAMA<-----------***"<<endl;
            cout<<"Laboratorio Estructura de Datos Sección C       "<<endl;
            cout<<"Proyecto ¿Unico? - Fase 1                       "<<endl;
            cout<<"Aux. Wilfred Perez                              "<<endl;
            break;
        }else if(op == 6){
            cout<<"Listado de Usuarios"<<endl;
            ListaUsuarios->Bubble();
            ListaUsuarios->Display();
            cout<<"Listado de Articulos"<<endl;
            MostrarCategorias();
            //NuevoTutorial->peek();
            //cout<<endl;
        }else{
            break;
        }
          
    }
    return 0;
};








    //FUNCIONA COLA
/*
    Cola* colanueva = new Cola();
    colanueva->agregardim(5, 7);
    colanueva->enque(5, 6);
    colanueva->enque(7, 9);
    colanueva->enque(3, 5);
    colanueva->enque(9, 5);
    colanueva->enque(3, 6);
    colanueva->enque(24, 5);
    colanueva->peek();

    colanueva->GraphoCola();
*/
    //FUNCIONA LA REGRESION
    /*
    ListaPila* pilanueva = new ListaPila();
    pilanueva->insertar("joto");
    pilanueva->insertar("ELMASTER");
    pilanueva->insertar("SUPREMO");
    pilanueva->mostrar();
    pilanueva->Grapho();
    pilanueva->Regresion("ELMASTER");
    */
    //FUNCIONA LA LISTA DE LISTAS
    /*
    AgregarCategoria("Legendario");
    AgregarCategoria("Legendario");
    AgregarCategoria("Normal");
    AgregarCategoria("Normal");
    AgregarCategoria("Legendario");
    AgregarCategoria("Epico");
    AgregarCategoria("Epico");
    AgregarCategoria("Normal");
    AgregarCategoria("Barbaro");
    AgregarCategoria("Comun");
    AgregarCategoria("Normal");
    AgregarCategoria("Normal");
    AgregarCategoria("Barbaro");
    AgregarCategoria("Barbaro");
    AgregarCategoria("Barbaro");
    Ajustar();
    ListadoArticulos(5, "Comun", 500, "Kor", "SD");
    ListadoArticulos(7, "Legendario", 500, "SET", "SD");
    ListadoArticulos(77, "Epico", 500, "Minga", "SD");
    ListadoArticulos(1, "Legendario", 500, "DERSTA", "SD");
    ListadoArticulos(565, "Barbaro", 500, "DERSTA", "SD");
    ListadoArticulos(9, "Legendario", 500, "DERSTA", "SD");
    ListadoArticulos(1085, "Legendario", 200, "Arma S", "CS");
    ListadoArticulos(450, "Normal", 209, "No Podersoa", "CS");
    ListadoArticulos(6494, "Legendario", 600, "Arma ", "CS");
    ListadoArticulos(58, "Legendario", 20, "Arco del Fin", "CS");
    ListadoArticulos(129, "Barbaro", 50, "NoSe", "CS");
    ListadoArticulos(165, "Barbaro", 10, "LSKD", "CS");
    ListadoArticulos(192, "Normal", 20, "DFADFADF", "CS");
    MostrarCategorias();
    */
    //Grafo();
    
    //FUNCIONA LA GRAFICADA Y ARREGLO DE USUARIOS
/*
    DobleL* listadoble = new DobleL();
    listadoble->Insertar("jose", "Lalala", 55, 12);
    listadoble->Insertar("sdf", "fe", 45, 12);
    listadoble->Insertar("kis", "ass", 25, 12);
    listadoble->Insertar("jos", "Lalala", 80, 12);
    listadoble->Insertar("minda", "Lalala", 150, 12);
    listadoble->Bubble();
    listadoble->Display();
    listadoble->modificarUsuario("jos", "Kier", "sdfsdf", 45, 999);
    listadoble->Display();
    listadoble->Bubble();
    listadoble->eliminarUsuario("minda");
    listadoble->Display();
    listadoble->GrafoDoble();
*/
