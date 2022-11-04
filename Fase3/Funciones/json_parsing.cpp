/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/cppFiles/file.cc to edit this template
 */


/*
IINCLUDES NO BORRAR PENDEJO
*/
#include <iostream>
#include "../json/json.h"
#include "../json/json-forwards.h"
#include "jsoncpp.cpp"
#include <string>
// #include <char>
#include <fstream>
#include "json_parsing.h"   




using namespace std;
/*
IINCLUDES NO BORRAR PENDEJO
*/

class Persona {
 private:
  std::string nombre;
  int edad;
  int monedas;
  std::string password;

  void metodoPrivado() { std::cout << "Llamada privada dentro de la clase\n"; }

 public:
  // Constructor sin argumentos
  Persona() {
    std::cout << "Se llama al constructor sin argumentos\n";
    this->metodoPrivado();
  }
  // Constructor con nombre y edad
  Persona(std::string nombre, int edad,int monedas,std::string password) {
    this->edad = edad;
    this->nombre = nombre;
    this->monedas = monedas;
    this->password = password;
  }

  int getEdad() { return this->edad; }
  void setEdad(int edad) { this->edad = edad; }

  std::string getNombre() { return this->nombre; }
  void setNombre(std::string nombre) { this->nombre = nombre; }

  int getMonedas(){ return this->monedas;};
  void setMonedas(int monedas) { this->monedas = monedas; }

  std::string getPassword() { return this->password; }
  void setPassword(std::string nombre) { this->password = password; }
  
};





void json_parsing::lector(){
    
    Persona listPersonasTemp[1000];
    // Usando el fstream para tomar la ruta del archivo
    ifstream file("DATOS.json");
    Json::Value actualJson;
    Json::Reader reader;
    
    // Usando Reader para parsear el Json osea leerlo
    reader.parse(file, actualJson);
    
    // Ahora obtendremos la data del JSON
    //cout << "Total JSON data: \n" << actualJson << endl;
    
    // Ahora obtendremos los datos INDIVIDUALMENTE
    // Numero de elementos dentro del JSON
    //cout << "Objeto de la Rama Principal de JSON: " << actualJson.size() << endl;
    
    
    const Json::Value users = actualJson["usuarios"];
   
    for(int i = 0; i < users.size(); i = i + 1){
        //listaUsuarios->
        /* 
        * SIRVE NO BORRAR
        cout << i << endl;
        cout << users[i]["nick"] << endl;
        * SIRVE NO BORRAR
        */

        string nick = users[i]["nick"].asString();
        
        string edadTemp = (users[i]["edad"].asString());
        int edad = std::atoi(edadTemp.c_str());

        string monTemp = (users[i]["monedas"].asString());
        int monedas = std::atoi(monTemp.c_str());
        
        string password = users[i]["password"].asString();

        // cout << edad << endl;
        Persona usuario(nick,edad,monedas,password);

        cout << usuario.getNombre() << " "  << usuario.getEdad() << " " << usuario.getMonedas() << " " << usuario.getPassword() << endl;
        

    }
    
    
    // return listPersonasTemp;
}

