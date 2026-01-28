///////////////////////////////////////////////////////////
//  forme.cpp
//  Implementation of the Class CForme
//  Created on:      20-janv.-2026 10:20:36
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#include "forme.h"
using namespace std;

CForme::CForme(){
	nom = "forme inconnue";
}



CForme::~CForme(){

}

/**
 * constructeur qui initialise le nom de la forme
 */
CForme::CForme(string _nom){
	nom = _nom;
}


/**
 * Affiche le nom de la forme
 */
void CForme::afficher(){
	cout << "Forme : " << nom << endl;
}


double CForme::surface(){
	return 0;
}