#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

main()
{
    ifstream datosEntrada; 
    ofstream datosSalida; 
    string linea, lineaf="";
    int tam, pos, cont;
    datosEntrada.open("tarea2Entrada.txt");
    datosSalida.open("datosSalida.txt"); 
    while(!datosEntrada.eof()){  
        getline(datosEntrada, linea); 
        tam = linea.length();
        lineaf="";
        pos = tam-1;
        cont=0;
        while (pos<tam and pos>=0) {
            lineaf = linea.substr(pos,1) + lineaf;            
            pos--;
            cont++;
            if (cont==3 && pos>=0){
                lineaf.insert(0,",");
                cont=0;
            }
        }         
        datosSalida << lineaf << endl; 
    }
        
    cout << "Fin" << endl; 
    datosEntrada.close();
    datosSalida.close();
    return 0;
}
