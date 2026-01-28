///////////////////////////////////////////////////////////
//  OctogoneRegulier.cpp
//  Implementation of the Class OctogoneRegulier
//  Created on:      20-janv.-2026 10:20:48
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#include "OctogoneRegulier.h"
using namespace std;

COctogoneRegulier::COctogoneRegulier(){
	nom = "octogone regulier inconnu";
	cote = 5;
}



COctogoneRegulier::~COctogoneRegulier(){

}

/**
 * Affiche le nom de la forme
 */
void COctogoneRegulier::afficher(){
	CForme::afficher();
	cout << "Cote : " << cote << endl;
	cout << "Surface : " << surface() << endl;
}


/**
 * constructeur qui initialise le nom de la forme
 */
COctogoneRegulier::COctogoneRegulier(string _nom, int _cote){
	nom = _nom;
	cote = _cote;
}

double COctogoneRegulier::surface(){
	surface = 2 * (1 + sqrt(2)) * cote * cote;
	return 0;
}